const clone = (value) => JSON.parse(JSON.stringify(value));

const storage = {
  read(key, fallback = []) {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : clone(fallback);
    } catch (error) {
      console.warn(`Unable to read storage key "${key}"`, error);
      return clone(fallback);
    }
  },
  write(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.warn(`Unable to write storage key "${key}"`, error);
    }
  },
};

const STORAGE_KEYS = {
  guestbook: "persistenceGardenGuestbook",
  streaks: "persistenceGardenStreaks",
  patterns: "persistenceGardenPatterns",
};

const zoneNav = document.querySelector(".zone-nav");
const zoneButtons = Array.from(document.querySelectorAll(".zone-nav__btn"));
const zones = Array.from(document.querySelectorAll(".zone"));
const heroEnter = document.querySelector(".hero__enter");
const heroSigil = document.querySelector(".hero__sigil");
const discoveriesSection = document.getElementById("discoveries");
const prefersReducedMotion = window.matchMedia(
  "(prefers-reduced-motion: reduce)"
);
let motionSafe = !prefersReducedMotion.matches;
let discoveriesUnlocked = false;
let discoveryClickCount = 0;
let discoveryTimeoutId;

function activateZone(targetId) {
  zones.forEach((zone) => {
    const isActive = zone.id === targetId;
    zone.classList.toggle("is-active", isActive);
    zone.toggleAttribute("hidden", !isActive);
    zone.setAttribute("aria-hidden", String(!isActive));
  });

  zoneButtons.forEach((button) => {
    button.classList.toggle("is-active", button.dataset.target === targetId);
  });
}

function bindZoneButton(button) {
  if (!button) return;
  button.addEventListener("click", () => {
    activateZone(button.dataset.target);
  });
}

zoneButtons.forEach((button) => {
  bindZoneButton(button);
});

if (heroEnter) {
  heroEnter.addEventListener("click", () => {
    const target = heroEnter.dataset.target || "patterns";
    activateZone(target);
    document
      .getElementById(target)
      ?.scrollIntoView({ behavior: "smooth", block: "start" });
  });
}

function discoverGlow() {
  if (!discoveriesSection) return;
  discoveriesSection.classList.add("is-revealed");
  if (motionSafe) {
    window.setTimeout(() => {
      discoveriesSection.classList.remove("is-revealed");
    }, 1800);
  } else {
    discoveriesSection.classList.remove("is-revealed");
  }
}

function revealDiscoveries() {
  if (discoveriesUnlocked || !discoveriesSection) return;
  discoveriesUnlocked = true;

  discoveriesSection.removeAttribute("hidden");
  discoveriesSection.setAttribute("aria-hidden", "false");

  const secretButton = document.createElement("button");
  secretButton.type = "button";
  secretButton.className = "zone-nav__btn";
  secretButton.dataset.target = "discoveries";
  secretButton.textContent = "Hidden Discoveries";

  if (zoneNav) {
    zoneNav.appendChild(secretButton);
  }

  zoneButtons.push(secretButton);
  bindZoneButton(secretButton);

  requestAnimationFrame(() => {
    activateZone("discoveries");
    discoverGlow();
  });
}

function handleDiscoveryTap() {
  if (discoveriesUnlocked) return;

  discoveryClickCount += 1;

  if (discoveryTimeoutId) {
    window.clearTimeout(discoveryTimeoutId);
  }

  discoveryTimeoutId = window.setTimeout(() => {
    discoveryClickCount = 0;
  }, 4000);

  if (discoveryClickCount >= 3) {
    discoveryClickCount = 0;
    revealDiscoveries();
  }
}

heroSigil?.addEventListener("click", handleDiscoveryTap);
heroSigil?.addEventListener("keydown", (event) => {
  if (event.key === "Enter" || event.key === " ") {
    event.preventDefault();
    handleDiscoveryTap();
  }
});

const defaultZone =
  zones.find((zone) => zone.classList.contains("is-active"))?.id || "patterns";
activateZone(defaultZone);

const guestbookState = storage.read(STORAGE_KEYS.guestbook);
const streakState = storage.read(STORAGE_KEYS.streaks);
const patternState = storage.read(STORAGE_KEYS.patterns);

const guestbookForm = document.getElementById("guestbook-form");
const guestbookList = document.getElementById("guestbook");
const guestbookEmpty = document.getElementById("guestbook-empty");

function formatDate(timestamp) {
  return new Date(timestamp).toLocaleString(undefined, {
    dateStyle: "medium",
    timeStyle: "short",
  });
}

function renderGuestbook() {
  if (!guestbookList) return;

  guestbookList.innerHTML = "";

  if (guestbookState.length === 0) {
    guestbookEmpty?.removeAttribute("hidden");
    guestbookList.appendChild(guestbookEmpty);
    return;
  }

  guestbookEmpty?.setAttribute("hidden", "true");

  guestbookState
    .slice()
    .sort((a, b) => Number(b.timestamp) - Number(a.timestamp))
    .forEach((entry, index) => {
      const wrapper = document.createElement("article");
      wrapper.className = "guestbook-entry";

      const header = document.createElement("div");
      header.className = "guestbook-entry__header";

      const nameEl = document.createElement("span");
      nameEl.className = "guestbook-entry__name";
      nameEl.textContent = entry.name;

      const timeEl = document.createElement("time");
      timeEl.className = "guestbook-entry__time";
      timeEl.dateTime = new Date(entry.timestamp).toISOString();
      timeEl.textContent = formatDate(entry.timestamp);

      header.append(nameEl, timeEl);

      const messageEl = document.createElement("p");
      messageEl.className = "guestbook-entry__message";
      messageEl.textContent = entry.message;

      wrapper.append(header, messageEl);
      guestbookList.appendChild(wrapper);

      if (motionSafe) {
        wrapper.style.setProperty("--reveal-delay", `${index * 70}ms`);
        requestAnimationFrame(() => {
          wrapper.classList.add("is-visible");
        });
      } else {
        wrapper.classList.add("is-visible");
      }
    });
}

function celebrateFormSuccess(form, message) {
  if (!form) return;
  let success = form.querySelector(".form-success");

  if (!success) {
    success = document.createElement("div");
    success.className = "form-success";
    success.setAttribute("role", "status");
    success.setAttribute("aria-live", "polite");
    form.appendChild(success);
  }

  if (success.dataset.timeout) {
    window.clearTimeout(Number(success.dataset.timeout));
  }

  success.textContent = message;
  success.classList.remove("is-visible");
  void success.offsetWidth; // restart transition
  success.classList.add("is-visible");

  const timeoutId = window.setTimeout(() => {
    success.classList.remove("is-visible");
    success.dataset.timeout = "";
  }, 2600);

  success.dataset.timeout = String(timeoutId);
}

guestbookForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  const form = event.target;
  const formData = new FormData(form);

  const name = formData.get("name")?.toString().trim() ?? "";
  const message = formData.get("message")?.toString().trim() ?? "";

  if (!name || !message) return;

  guestbookState.push({
    id: crypto.randomUUID(),
    name,
    message,
    timestamp: Date.now(),
  });

  storage.write(STORAGE_KEYS.guestbook, guestbookState);
  form.reset();
  renderGuestbook();
  celebrateFormSuccess(form, "Your words now shimmer in the garden.");
});

renderGuestbook();

const streakForm = document.getElementById("streak-form");
const streakList = document.getElementById("streak-list");
const streakEmpty = document.getElementById("streak-empty");

function renderStreaks() {
  if (!streakList) return;

  streakList.innerHTML = "";

  if (streakState.length === 0) {
    streakEmpty?.removeAttribute("hidden");
    streakList.appendChild(streakEmpty);
    return;
  }

  streakEmpty?.setAttribute("hidden", "true");

  streakState
    .slice()
    .sort((a, b) => Number(b.updatedAt) - Number(a.updatedAt))
    .forEach((streak) => {
      const wrapper = document.createElement("article");
      wrapper.className = "streak-entry";
      wrapper.dataset.id = streak.id;

      const meta = document.createElement("div");
      meta.className = "streak-entry__meta";

      const nameEl = document.createElement("strong");
      nameEl.textContent = streak.name;

      const focusEl = document.createElement("span");
      focusEl.textContent = streak.focus;

      const updatedEl = document.createElement("span");
      updatedEl.textContent = `Last recorded ${formatDate(streak.updatedAt)}`;

      meta.append(nameEl, focusEl, updatedEl);

      const daysEl = document.createElement("div");
      daysEl.className = "streak-entry__days";
      daysEl.textContent = streak.count;

      const actions = document.createElement("div");
      actions.className = "streak-entry__actions";

      const incrementBtn = document.createElement("button");
      incrementBtn.type = "button";
      incrementBtn.dataset.action = "increment";
      incrementBtn.textContent = "+1 day";

      const removeBtn = document.createElement("button");
      removeBtn.type = "button";
      removeBtn.dataset.action = "remove";
      removeBtn.textContent = "Archive";

      actions.append(incrementBtn, removeBtn);
      wrapper.append(meta, daysEl, actions);
      streakList.appendChild(wrapper);
    });
}

streakForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  const form = event.target;
  const data = new FormData(form);

  const name = data.get("name")?.toString().trim() ?? "";
  const focus = data.get("focus")?.toString().trim() ?? "";
  const count = Number(data.get("count"));

  if (!name || !focus || Number.isNaN(count) || count < 1) {
    return;
  }

  streakState.push({
    id: crypto.randomUUID(),
    name,
    focus,
    count,
    updatedAt: Date.now(),
  });

  storage.write(STORAGE_KEYS.streaks, streakState);
  form.reset();
  renderStreaks();
  celebrateFormSuccess(form, "Streak recorded. Keep shining.");
});

streakList?.addEventListener("click", (event) => {
  const target = event.target;
  if (!(target instanceof HTMLButtonElement)) return;

  const entry = target.closest(".streak-entry");
  if (!entry) return;

  const id = entry.dataset.id;
  const streak = streakState.find((item) => item.id === id);

  if (!streak) return;

  if (target.dataset.action === "increment") {
    streak.count += 1;
    streak.updatedAt = Date.now();
    storage.write(STORAGE_KEYS.streaks, streakState);
    renderStreaks();
  }

  if (target.dataset.action === "remove") {
    const index = streakState.findIndex((item) => item.id === id);
    if (index > -1) {
      streakState.splice(index, 1);
      storage.write(STORAGE_KEYS.streaks, streakState);
      renderStreaks();
    }
  }
});

renderStreaks();

const patternCanvas = document.getElementById("pattern-canvas");
const patternColor = document.getElementById("pattern-color");
const patternSize = document.getElementById("pattern-size");
const patternClear = document.getElementById("pattern-clear");

function createDotElement(dot, { isNew = false } = {}) {
  const span = document.createElement("span");
  span.className = "pattern-dot";
  span.style.left = `${dot.x}%`;
  span.style.top = `${dot.y}%`;
  span.style.width = `${dot.size}px`;
  span.style.height = `${dot.size}px`;
  span.style.background = dot.color;
  span.title = `Placed ${formatDate(dot.timestamp)}`;
  span.dataset.id = dot.id;
  if (isNew) {
    span.classList.add("is-new");
    span.addEventListener(
      "animationend",
      () => {
        span.classList.remove("is-new");
      },
      { once: true }
    );
  }
  return span;
}

function renderPattern() {
  if (!patternCanvas) return;
  patternCanvas.innerHTML = "";

  patternState
    .slice()
    .sort((a, b) => Number(a.timestamp) - Number(b.timestamp))
    .forEach((dot) => {
      patternCanvas.appendChild(createDotElement(dot));
    });
}

function spawnCanvasRipple({ x, y, color }) {
  if (!patternCanvas || !motionSafe) return;

  const ripple = document.createElement("span");
  ripple.className = "canvas-ripple";
  ripple.style.left = `${x}%`;
  ripple.style.top = `${y}%`;
  ripple.style.setProperty("--ripple-color", color);

  const rect = patternCanvas.getBoundingClientRect();
  const size = Math.max(rect.width, rect.height) * 0.6;
  ripple.style.setProperty("--ripple-size", `${size}px`);

  ripple.addEventListener(
    "animationend",
    () => {
      ripple.remove();
    },
    { once: true }
  );

  patternCanvas.appendChild(ripple);
}

patternCanvas?.addEventListener("click", (event) => {
  if (!patternCanvas) return;

  const rect = patternCanvas.getBoundingClientRect();
  const x = ((event.clientX - rect.left) / rect.width) * 100;
  const y = ((event.clientY - rect.top) / rect.height) * 100;

  const color =
    patternColor instanceof HTMLInputElement && patternColor.value
      ? patternColor.value
      : "#7ac9ff";
  const size =
    patternSize instanceof HTMLInputElement && patternSize.value
      ? Number(patternSize.value)
      : 12;

  const dot = {
    id: crypto.randomUUID(),
    x: Math.max(2, Math.min(98, Number(x.toFixed(2)))),
    y: Math.max(4, Math.min(96, Number(y.toFixed(2)))),
    color,
    size,
    timestamp: Date.now(),
  };

  patternState.push(dot);
  storage.write(STORAGE_KEYS.patterns, patternState);
  spawnCanvasRipple({ x: dot.x, y: dot.y, color });
  patternCanvas.appendChild(createDotElement(dot, { isNew: true }));
});

patternClear?.addEventListener("click", () => {
  if (!patternState.length) return;
  if (!window.confirm("Clear the shared pattern canvas?")) return;
  patternState.splice(0, patternState.length);
  storage.write(STORAGE_KEYS.patterns, patternState);
  renderPattern();
});

renderPattern();

const patternShare = document.getElementById("pattern-share");

function exportPatternImage() {
  if (!patternCanvas) return;

  const rect = patternCanvas.getBoundingClientRect();
  const width = Math.max(320, Math.round(rect.width));
  const height = Math.max(240, Math.round(rect.height));
  const scale = Math.min(window.devicePixelRatio || 1, 2);

  const canvas = document.createElement("canvas");
  canvas.width = width * scale;
  canvas.height = height * scale;

  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  ctx.scale(scale, scale);

  const backgroundGradient = ctx.createLinearGradient(0, 0, width, height);
  backgroundGradient.addColorStop(0, "rgba(14, 22, 35, 0.95)");
  backgroundGradient.addColorStop(1, "rgba(8, 14, 26, 0.88)");
  ctx.fillStyle = backgroundGradient;
  ctx.fillRect(0, 0, width, height);

  ctx.save();
  ctx.globalAlpha = 0.24;
  ctx.fillStyle = "rgba(122, 201, 255, 0.4)";
  ctx.fillRect(0, height - 24, width, 24);
  ctx.restore();

  patternState
    .slice()
    .sort((a, b) => Number(a.timestamp) - Number(b.timestamp))
    .forEach((dot) => {
      const x = (Number(dot.x) / 100) * width;
      const y = (Number(dot.y) / 100) * height;
      const radius = Number(dot.size) / 2;

      ctx.save();
      ctx.shadowColor = "rgba(122, 201, 255, 0.35)";
      ctx.shadowBlur = 12;
      ctx.shadowOffsetX = 0;
      ctx.shadowOffsetY = 6;
      ctx.fillStyle = dot.color || "#7ac9ff";
      ctx.beginPath();
      ctx.arc(x, y, radius, 0, Math.PI * 2);
      ctx.closePath();
      ctx.fill();
      ctx.restore();
    });

  ctx.fillStyle = "rgba(122, 201, 255, 0.75)";
  ctx.font = "16px 'Inter', system-ui, sans-serif";
  ctx.textBaseline = "bottom";
  ctx.fillText("The Persistence Garden — Shared Pattern", 16, height - 8);

  const link = document.createElement("a");
  link.href = canvas.toDataURL("image/png");
  link.download = `persistence-pattern-${Date.now()}.png`;
  link.click();
}

patternShare?.addEventListener("click", exportPatternImage);

const patternVisuals = Array.from(document.querySelectorAll(".pattern-visual"));
let patternObserver;

function initPatternVisuals() {
  if (!patternVisuals.length) return;

  if (patternObserver) {
    patternObserver.disconnect();
    patternObserver = undefined;
  }

  if (!motionSafe || !("IntersectionObserver" in window)) {
    patternVisuals.forEach((visual) => visual.classList.add("is-active"));
    return;
  }

  patternVisuals.forEach((visual) => visual.classList.remove("is-active"));

  patternObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        entry.target.classList.toggle("is-active", entry.isIntersecting);
      });
    },
    {
      threshold: 0.35,
    }
  );

  patternVisuals.forEach((visual) => patternObserver?.observe(visual));
}

initPatternVisuals();

const manageMotionPreference = (event) => {
  motionSafe = !event.matches;
  if (!motionSafe) {
    document.querySelector(".particle-field")?.remove();
  } else {
    initParticles();
  }
  initPatternVisuals();
};

if (typeof prefersReducedMotion.addEventListener === "function") {
  prefersReducedMotion.addEventListener("change", manageMotionPreference);
} else if (typeof prefersReducedMotion.addListener === "function") {
  prefersReducedMotion.addListener(manageMotionPreference);
}

function initParticles() {
  if (!motionSafe) return;
  if (document.querySelector(".particle-field")) return;

  const container = document.createElement("div");
  container.className = "particle-field";
  container.setAttribute("aria-hidden", "true");

  const total = 26;
  for (let index = 0; index < total; index += 1) {
    const particle = document.createElement("span");
    const size = 4 + Math.random() * 6;
    const duration = 16 + Math.random() * 14;
    const delay = Math.random() * duration * -1;

    particle.style.left = `${Math.random() * 100}%`;
    particle.style.top = `${Math.random() * 100}%`;
    particle.style.setProperty("--size", `${size}px`);
    particle.style.setProperty("--duration", `${duration}s`);
    particle.style.setProperty("--delay", `${delay}s`);
    particle.style.setProperty(
      "--offset-x",
      `${(Math.random() - 0.5) * 180}px`
    );
    particle.style.setProperty(
      "--offset-y",
      `${(Math.random() - 0.8) * 220}px`
    );

    container.appendChild(particle);
  }

  document.body.insertBefore(container, document.body.firstChild);
}

initParticles();

const visitorCounter = document.getElementById("visitor-counter");
const VISITOR_ID_KEY = "persistenceGardenVisitorId";
const VISITOR_TOTAL_KEY = "persistenceGardenVisitorTotal";
const VISITOR_BASELINE = 1280;

function initVisitorCounter() {
  if (!visitorCounter) return;

  let visitorNumber = VISITOR_BASELINE;
  let storedTotal = VISITOR_BASELINE;

  try {
    const storedId = Number(localStorage.getItem(VISITOR_ID_KEY));
    const total = Number(localStorage.getItem(VISITOR_TOTAL_KEY));

    storedTotal =
      Number.isFinite(total) && total >= VISITOR_BASELINE
        ? total
        : VISITOR_BASELINE + Math.floor(Math.random() * 120);

    visitorNumber =
      Number.isFinite(storedId) && storedId >= VISITOR_BASELINE
        ? storedId
        : storedTotal + 1;

    if (visitorNumber > storedTotal) {
      storedTotal = visitorNumber;
    }

    localStorage.setItem(VISITOR_ID_KEY, String(visitorNumber));
    localStorage.setItem(VISITOR_TOTAL_KEY, String(storedTotal));
  } catch (error) {
    console.warn("Visitor counter unavailable", error);
  }

  const strong = visitorCounter.querySelector("strong");
  if (strong) {
    strong.textContent = `#${visitorNumber.toLocaleString()}`;
  }

  requestAnimationFrame(() => {
    visitorCounter.classList.add("is-visible");
  });
}

initVisitorCounter();
