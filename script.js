(() => {
  'use strict';

  // ── elements ──────────────────────────────────────────────────────────────
  const canvas    = document.getElementById('hush-canvas');
  const ctx       = canvas.getContext('2d');
  const voidCore  = document.getElementById('void-core');
  const cursorDot = document.getElementById('cursor-dot');
  const letters   = [...document.querySelectorAll('.zyro-letter')];
  const obsField  = document.getElementById('observer-field');
  const mfField   = document.getElementById('manifestation-field');
  const navEl     = document.querySelector('nav');
  const marker    = document.querySelector('.page-marker');

  // ── mouse ─────────────────────────────────────────────────────────────────
  let mouseX = window.innerWidth  / 2;
  let mouseY = window.innerHeight / 2;

  // ── observer state ────────────────────────────────────────────────────────
  // 'distant' | 'adjacent' | 'absorbed'
  // Transitions:
  //   distant  → adjacent : enters proximity zone
  //   adjacent → absorbed : sustained cursor stillness (stability) while in prox
  //   absorbed → adjacent : cursor moves or leaves prox
  //   adjacent → distant  : leaves proximity
  let observerState = 'distant';
  let letterStage   = 0;
  let stageTimeouts = [];
  let stableAccum   = 0;     // ms cursor has been stable while adjacent
  let lastLoop      = Date.now();

  // ── velocity window (stability) ───────────────────────────────────────────
  // Rolling average of cursor speed samples.
  // stability() → 0 = moving, 1 = completely still.
  const VEL_BUF  = [];
  const VEL_SIZE = 30;
  let vLX = mouseX, vLY = mouseY, vLT = Date.now();

  function sampleVelocity(x, y) {
    const now = Date.now();
    const dt  = now - vLT;
    if (dt < 14) return;
    const speed = Math.hypot(x - vLX, y - vLY) / dt;
    vLX = x; vLY = y; vLT = now;
    VEL_BUF.push(speed);
    if (VEL_BUF.length > VEL_SIZE) VEL_BUF.shift();
  }

  function stability() {
    if (VEL_BUF.length < 8) return 0;
    const avg = VEL_BUF.reduce((s, v) => s + v, 0) / VEL_BUF.length;
    return Math.max(0, 1 - avg / 0.5);
  }

  // ── lerped display values ─────────────────────────────────────────────────
  let smoothScale  = 1;
  let smoothBg     = 5;
  let smoothBorder = 0.07;
  let smoothObsOp  = 0.15;
  let smoothMfOp   = 0;
  let smoothNavOp  = 1;

  // ── visual targets per state ──────────────────────────────────────────────
  // Proximity adds continuous modulation on top of each target.
  // absorbed goes darker (bg → 2), not brighter — the observer has collapsed in.
  const TARGETS = {
    distant:  { scale: 1.00, bg:  5, border: 0.07, obsOp: 0.15, mfOp: 0.00, navOp: 1.00 },
    adjacent: { scale: 1.04, bg: 10, border: 0.14, obsOp: 0.40, mfOp: 0.00, navOp: 1.00 },
    absorbed: { scale: 1.06, bg:  2, border: 0.52, obsOp: 0.03, mfOp: 1.00, navOp: 0.14 },
  };

  // ── parallax config ───────────────────────────────────────────────────────
  const MAX_SHIFT  = 32;
  const parallaxEls = [
    { el: document.getElementById('zyro-field'),      baseX:    0, baseY: -132, depth: 0.06 },
    { el: document.getElementById('void-wrap'),       baseX:    0, baseY:    0, depth: 0    },
    { el: document.getElementById('void-label-wrap'), baseX:    0, baseY:  106, depth: 0.04 },
    { el: obsField,                                   baseX: -212, baseY:  -72, depth: 0.16 },
    { el: mfField,                                    baseX:    0, baseY:  154, depth: 0.05 },
  ];

  // ── HUSH ring ─────────────────────────────────────────────────────────────
  const HUSH_R = 198;
  const traces = [];
  let trMouseX = mouseX, trMouseY = mouseY, trTime = 0;

  function voidCenter() {
    const r = voidCore.getBoundingClientRect();
    return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
  }

  function resizeCanvas() {
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  // ── ZYRO letters ──────────────────────────────────────────────────────────
  const scatterOffsets = [
    { x: -8, y: -7 }, { x: 5, y: 7 }, { x: -4, y: -5 }, { x: 7, y: 4 },
  ];
  letters.forEach((l, i) => {
    l.style.opacity    = '0';
    l.style.transform  = `translate(${scatterOffsets[i].x}px, ${scatterOffsets[i].y}px)`;
    l.style.transition = `opacity ${1.6 + i * 0.22}s ease, transform ${2.1 + i * 0.18}s ease`;
  });

  const LETTER_OPACITY = [0, 0.42, 0.88, 1.0];

  function applyLetterStage(s) {
    letterStage = s;
    letters.forEach((l, i) => {
      l.style.opacity   = String(LETTER_OPACITY[s]);
      l.style.transform = s >= 1
        ? 'translate(0, 0)'
        : `translate(${scatterOffsets[i].x}px, ${scatterOffsets[i].y}px)`;
    });
  }

  // ── proximity ─────────────────────────────────────────────────────────────
  function getProximity() {
    const c = voidCenter();
    return Math.max(0, 1 - Math.hypot(mouseX - c.x, mouseY - c.y) / 310);
  }

  // ── state transitions ─────────────────────────────────────────────────────
  const MARKER_TEXT = {
    distant:  'in formation',
    adjacent: 'observing',
    absorbed: 'threshold',
  };

  function transitionTo(next) {
    if (next === observerState) return;
    const prev = observerState;
    observerState = next;

    stageTimeouts.forEach(clearTimeout);
    stageTimeouts = [];

    if (next === 'adjacent') {
      if (prev === 'distant') {
        stageTimeouts.push(setTimeout(() => applyLetterStage(1), 1800));
        stageTimeouts.push(setTimeout(() => applyLetterStage(2), 4500));
      }
    } else if (next === 'absorbed') {
      applyLetterStage(3);
    } else if (next === 'distant') {
      stageTimeouts.push(setTimeout(() => applyLetterStage(0), 3200));
    }

    if (marker) marker.textContent = MARKER_TEXT[next];
  }

  // ── rAF loop ──────────────────────────────────────────────────────────────
  function loop() {
    const now  = Date.now();
    const dt   = now - lastLoop;
    lastLoop   = now;

    const p    = getProximity();
    const stab = stability();
    const c    = voidCenter();

    // ── state machine ──────────────────────────────────────────────────────
    if (observerState === 'distant') {
      stableAccum = 0;
      if (p > 0.22) transitionTo('adjacent');

    } else if (observerState === 'adjacent') {
      if (p < 0.14) {
        transitionTo('distant');
        stableAccum = 0;
      } else if (stab > 0.72) {
        stableAccum += dt;
        if (stableAccum >= 5500) transitionTo('absorbed');
      } else {
        // decay when moving — stillness must be continuous, not cumulative
        stableAccum = Math.max(0, stableAccum - dt * 0.4);
      }

    } else if (observerState === 'absorbed') {
      if (p < 0.14 || stab < 0.22) {
        transitionTo('adjacent');
        stableAccum = 0;
      }
    }

    // ── lerp toward state targets ──────────────────────────────────────────
    const T    = TARGETS[observerState];
    const LERP = 0.07;

    smoothScale  += (T.scale  + p * 0.02  - smoothScale)  * LERP;
    smoothBg     += (T.bg     + p * 4     - smoothBg)      * LERP;
    smoothBorder += (T.border + p * 0.08  - smoothBorder)  * LERP;
    smoothObsOp  += (T.obsOp  - smoothObsOp)               * 0.04;
    smoothMfOp   += (T.mfOp   - smoothMfOp)                * 0.025;
    smoothNavOp  += (T.navOp  - smoothNavOp)               * 0.028;

    // apply
    voidCore.style.transform    = `scale(${smoothScale.toFixed(4)})`;
    voidCore.style.borderColor  = `rgba(255,255,255,${smoothBorder.toFixed(4)})`;
    const b = Math.round(smoothBg);
    document.body.style.backgroundColor = `rgb(${b},${b},${b})`;
    obsField.style.opacity  = smoothObsOp.toFixed(4);
    mfField.style.opacity   = smoothMfOp.toFixed(4);
    navEl.style.opacity     = smoothNavOp.toFixed(4);

    // cursor shrinks and nearly vanishes in absorbed state
    const isAbsorbed = observerState === 'absorbed';
    cursorDot.style.background = isAbsorbed
      ? `rgba(100,100,100,${(0.10 + p * 0.06).toFixed(3)})`
      : p > 0.3
        ? `rgba(154,154,154,${(0.35 + p * 0.45).toFixed(3)})`
        : 'var(--text-dim)';
    cursorDot.style.transform =
      `translate(-50%,-50%) scale(${isAbsorbed ? 0.55 : 1})`;

    // ── parallax ──────────────────────────────────────────────────────────
    const cx = window.innerWidth  / 2;
    const cy = window.innerHeight / 2;
    const nx = (mouseX - cx) / Math.max(cx, 1);
    const ny = (mouseY - cy) / Math.max(cy, 1);

    parallaxEls.forEach(({ el, baseX, baseY, depth }) => {
      const px = baseX + nx * MAX_SHIFT * depth;
      const py = baseY + ny * MAX_SHIFT * depth;
      el.style.transform =
        `translate(calc(-50% + ${px.toFixed(2)}px), calc(-50% + ${py.toFixed(2)}px))`;
    });

    // ── canvas: HUSH ring + traces ─────────────────────────────────────────
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // ring becomes the dominant frame in absorbed state
    const ringBase = isAbsorbed ? 0.048 : 0.014;
    ctx.beginPath();
    ctx.arc(c.x, c.y, HUSH_R, 0, Math.PI * 2);
    ctx.strokeStyle = `rgba(255,255,255,${ringBase})`;
    ctx.lineWidth   = 1;
    ctx.stroke();

    for (let i = traces.length - 1; i >= 0; i--) {
      const t   = traces[i];
      const age = (now - t.time) / 2400;
      if (age >= 1) { traces.splice(i, 1); continue; }
      const alpha = t.intensity * (1 - age) * (1 - age);
      const arc   = 0.6;
      ctx.beginPath();
      ctx.arc(c.x, c.y, HUSH_R, t.angle - arc / 2, t.angle + arc / 2);
      ctx.strokeStyle = `rgba(175,175,175,${alpha.toFixed(4)})`;
      ctx.lineWidth   = 1;
      ctx.stroke();
    }

    requestAnimationFrame(loop);
  }

  // ── trace check ───────────────────────────────────────────────────────────
  function checkTrace(x, y) {
    const now = Date.now();
    const dt  = now - trTime;
    if (dt < 18) return;
    const speed = Math.hypot(x - trMouseX, y - trMouseY) / dt;
    trMouseX = x; trMouseY = y; trTime = now;
    const c    = voidCenter();
    const dist = Math.hypot(x - c.x, y - c.y);
    if (speed > 0.15 && dist < HUSH_R * 1.9) {
      traces.push({
        angle:     Math.atan2(y - c.y, x - c.x),
        intensity: Math.min(speed * 0.55, 0.17),
        time:      now,
      });
    }
  }

  document.addEventListener('mousemove', e => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursorDot.style.left = mouseX + 'px';
    cursorDot.style.top  = mouseY + 'px';
    sampleVelocity(mouseX, mouseY);
    checkTrace(mouseX, mouseY);
  });

  // ── start ─────────────────────────────────────────────────────────────────
  loop();

})();
