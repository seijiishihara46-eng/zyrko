(() => {
  'use strict';

  // ── elements ──────────────────────────────────────────────────────────────
  const canvas       = document.getElementById('hush-canvas');
  const ctx          = canvas.getContext('2d');
  const voidCore     = document.getElementById('void-core');
  const cursorDot    = document.getElementById('cursor-dot');
  const letters      = [...document.querySelectorAll('.zyro-letter')];
  const obsField     = document.getElementById('observer-field');
  const mfField      = document.getElementById('manifestation-field');
  const navBtns      = [...document.querySelectorAll('.nav-label')];

  // ── state ─────────────────────────────────────────────────────────────────
  let mouseX         = window.innerWidth  / 2;
  let mouseY         = window.innerHeight / 2;
  let velMouseX      = mouseX;
  let velMouseY      = mouseY;
  let velTime        = 0;
  let currentStage   = 0;
  let wasInProx      = false;
  let stageTimeouts  = [];
  const traces       = [];

  // lerped values — avoid CSS transitions on JS-driven properties
  let smoothScale    = 1;
  let smoothBg       = 5;
  let smoothBorder   = 0.07;
  let smoothObsOp    = 0.15;
  let smoothMfOp     = 0;

  // ── parallax config ───────────────────────────────────────────────────────
  // baseX/Y: offset from viewport center in px
  // depth:   0 = fully anchored to void, higher = drifts more with cursor
  const MAX_SHIFT = 32;
  const parallaxEls = [
    { el: document.getElementById('zyro-field'),      baseX:    0, baseY: -132, depth: 0.06 },
    { el: document.getElementById('void-wrap'),       baseX:    0, baseY:    0, depth: 0    },
    { el: document.getElementById('void-label-wrap'), baseX:    0, baseY:  106, depth: 0.04 },
    { el: obsField,                                   baseX: -212, baseY:  -72, depth: 0.16 },
    { el: mfField,                                    baseX:    0, baseY:  154, depth: 0.05 },
  ];

  // ── HUSH ring ─────────────────────────────────────────────────────────────
  const HUSH_R = 198; // px radius from void center

  function voidCenter() {
    const r = voidCore.getBoundingClientRect();
    return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
  }

  // ── canvas resize ─────────────────────────────────────────────────────────
  function resizeCanvas() {
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  // ── letter init ───────────────────────────────────────────────────────────
  // Each letter begins slightly displaced; dwell stage 1+ drifts them to alignment.
  const scatterOffsets = [
    { x: -8, y: -7 },
    { x:  5, y:  7 },
    { x: -4, y: -5 },
    { x:  7, y:  4 },
  ];

  letters.forEach((l, i) => {
    l.style.opacity    = '0';
    l.style.transform  = `translate(${scatterOffsets[i].x}px, ${scatterOffsets[i].y}px)`;
    l.style.transition =
      `opacity ${1.6 + i * 0.22}s ease, transform ${2.1 + i * 0.18}s ease`;
  });

  // ── proximity ─────────────────────────────────────────────────────────────
  function getProximity() {
    const c    = voidCenter();
    const dist = Math.hypot(mouseX - c.x, mouseY - c.y);
    return Math.max(0, 1 - dist / 310);
  }

  // ── dwell stages ──────────────────────────────────────────────────────────
  //  0  default           — ZYRO invisible, observer dim
  //  1  1.8 s in prox     — ZYRO drifts into alignment, partially visible
  //  2  4.5 s in prox     — ZYRO fully aligned, observer brightens
  //  3  9.0 s in prox     — manifestation emerges
  const STAGE_DELAYS    = [1800, 4500, 9000];
  const LETTER_OPACITY  = [0, 0.42, 0.88, 1.0];
  const OBS_OPACITY     = [0.15, 0.22, 0.40, 0.42];
  const MF_OPACITY      = [0, 0, 0, 1];

  function applyStage(s) {
    if (s === currentStage) return;
    currentStage = s;

    letters.forEach((l, i) => {
      l.style.opacity   = String(LETTER_OPACITY[s]);
      l.style.transform = s >= 1
        ? 'translate(0, 0)'
        : `translate(${scatterOffsets[i].x}px, ${scatterOffsets[i].y}px)`;
    });
  }

  function enterProximity() {
    stageTimeouts.forEach(clearTimeout);
    stageTimeouts = STAGE_DELAYS.map((delay, i) =>
      setTimeout(() => applyStage(i + 1), delay)
    );
  }

  function exitProximity() {
    stageTimeouts.forEach(clearTimeout);
    stageTimeouts = [setTimeout(() => applyStage(0), 3200)];
  }

  // ── velocity trace (HUSH ring) ────────────────────────────────────────────
  // A trace is added when cursor moves with enough speed near the HUSH boundary.
  // Each trace is an arc at the cursor's angle from the void center; it decays.
  function checkTrace(x, y) {
    const now = Date.now();
    const dt  = now - velTime;
    if (dt < 18) return;

    const speed = Math.hypot(x - velMouseX, y - velMouseY) / dt;
    velMouseX = x; velMouseY = y; velTime = now;

    const c    = voidCenter();
    const dist = Math.hypot(x - c.x, y - c.y);

    // Only trace when cursor moves near the boundary (within 2× ring radius)
    if (speed > 0.15 && dist < HUSH_R * 1.9) {
      traces.push({
        angle:     Math.atan2(y - c.y, x - c.x),
        intensity: Math.min(speed * 0.55, 0.17),
        time:      now,
      });
    }
  }

  // ── rAF loop ──────────────────────────────────────────────────────────────
  function loop() {
    const p   = getProximity();
    const now = Date.now();
    const c   = voidCenter();

    // ── lerped continuous values ──
    const LERP = 0.07;
    smoothScale   += (1 + p * 0.04  - smoothScale)   * LERP;
    smoothBg      += (5 + p * 7     - smoothBg)       * LERP;
    smoothBorder  += (0.07 + p * 0.2 - smoothBorder)  * LERP;
    smoothObsOp   += (OBS_OPACITY[currentStage] - smoothObsOp) * 0.04;
    smoothMfOp    += (MF_OPACITY[currentStage]  - smoothMfOp)  * 0.025;

    // apply
    voidCore.style.transform    = `scale(${smoothScale.toFixed(4)})`;
    voidCore.style.borderColor  = `rgba(255,255,255,${smoothBorder.toFixed(4)})`;
    const b = Math.round(smoothBg);
    document.body.style.backgroundColor = `rgb(${b},${b},${b})`;
    obsField.style.opacity  = smoothObsOp.toFixed(4);
    mfField.style.opacity   = smoothMfOp.toFixed(4);

    // cursor color
    cursorDot.style.background = p > 0.3
      ? `rgba(154,154,154,${(0.35 + p * 0.45).toFixed(3)})`
      : 'var(--text-dim)';

    // ── dwell threshold ──
    const inProx = p > 0.2;
    if (inProx && !wasInProx) { wasInProx = true;  enterProximity(); }
    if (!inProx && wasInProx) { wasInProx = false; exitProximity();  }

    // ── parallax ──
    const cx = window.innerWidth  / 2;
    const cy = window.innerHeight / 2;
    const nx = (mouseX - cx) / Math.max(cx, 1);  // -1 to +1
    const ny = (mouseY - cy) / Math.max(cy, 1);

    parallaxEls.forEach(({ el, baseX, baseY, depth }) => {
      const px = baseX + nx * MAX_SHIFT * depth;
      const py = baseY + ny * MAX_SHIFT * depth;
      el.style.transform =
        `translate(calc(-50% + ${px.toFixed(2)}px), calc(-50% + ${py.toFixed(2)}px))`;
    });

    // ── canvas: HUSH ring + traces ──
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // base ring — always barely present
    ctx.beginPath();
    ctx.arc(c.x, c.y, HUSH_R, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(255,255,255,0.014)';
    ctx.lineWidth   = 1;
    ctx.stroke();

    // decaying arc traces
    for (let i = traces.length - 1; i >= 0; i--) {
      const t   = traces[i];
      const age = (now - t.time) / 2400;   // 0 → 1 over 2.4 s
      if (age >= 1) { traces.splice(i, 1); continue; }

      const alpha = t.intensity * (1 - age) * (1 - age); // quadratic decay
      const arc   = 0.6; // radians (≈ 34°)
      ctx.beginPath();
      ctx.arc(c.x, c.y, HUSH_R, t.angle - arc / 2, t.angle + arc / 2);
      ctx.strokeStyle = `rgba(175,175,175,${alpha.toFixed(4)})`;
      ctx.lineWidth   = 1;
      ctx.stroke();
    }

    requestAnimationFrame(loop);
  }

  // ── mouse ─────────────────────────────────────────────────────────────────
  document.addEventListener('mousemove', e => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursorDot.style.left = mouseX + 'px';
    cursorDot.style.top  = mouseY + 'px';
    checkTrace(mouseX, mouseY);
  });

  // ── nav ───────────────────────────────────────────────────────────────────
  navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      navBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      setTimeout(() => btn.classList.remove('active'), 2000);

      const target = btn.dataset.target;

      if (target === 'void') {
        // Briefly brighten the void border
        smoothBorder = 0.38;
      }
      if (target === 'observer') {
        // Briefly surface the observer field
        smoothObsOp = 0.68;
      }
      if (target === 'manifestation' && currentStage >= 3) {
        smoothMfOp = 1;
      }
    });
  });

  // ── start ─────────────────────────────────────────────────────────────────
  loop();

})();
