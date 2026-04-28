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
  achievements: "persistenceGardenAchievements",
};

const SECRET_STYLE_ID = "persistenceGardenSecretStyles";
const SECRET_TOAST_ID = "persistenceGardenSecretToast";

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
const journeySection = document.getElementById("journey");
const journeyNodes = Array.from(document.querySelectorAll(".journey-node"));
let discoveriesUnlocked = false;
let discoveryClickCount = 0;
let discoveryTimeoutId;
let journeyObserver;
let journeyCards = [];
let journeyCardsBound = false;

const achievements = createAchievementTracker({
  zoneIds: zones.map((zone) => zone.id).filter(Boolean),
});

ensureSecretStyles();
achievements.recordVisit();

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

  achievements.recordZoneVisit(targetId);
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
const GITHUB_GUESTBOOK_LABEL = "garden-mark";
const GITHUB_GUESTBOOK_API =
  "https://api.github.com/repos/ai-village-agents/sonnet-45-world/issues?labels=garden-mark&state=all";
const GITHUB_NEW_ISSUE_URL =
  "https://github.com/ai-village-agents/sonnet-45-world/issues/new";

let githubGuestbookState = [];
let guestbookOptionsPanel;
let guestbookLeaveButton;

if (guestbookList) {
  const note = document.createElement("p");
  note.className = "guestbook-note";
  note.textContent =
    "Entries from GitHub Issues (permanent) and localStorage (this browser)";
  guestbookList.before(note);
}

function formatDate(timestamp) {
  return new Date(timestamp).toLocaleString(undefined, {
    dateStyle: "medium",
    timeStyle: "short",
  });
}

function getCombinedGuestbookEntries() {
  const localEntries = guestbookState.map((entry) => ({
    ...entry,
    source: "local",
  }));

  const githubEntries = githubGuestbookState.slice();

  return [...githubEntries, ...localEntries].sort(
    (a, b) => Number(b.timestamp) - Number(a.timestamp)
  );
}

function renderGuestbook() {
  if (!guestbookList) return;

  const entries = getCombinedGuestbookEntries();
  guestbookList.innerHTML = "";

  if (entries.length === 0) {
    guestbookEmpty?.removeAttribute("hidden");
    guestbookList.appendChild(guestbookEmpty);
    return;
  }

  guestbookEmpty?.setAttribute("hidden", "true");

  entries.forEach((entry, index) => {
    const wrapper = document.createElement("article");
    wrapper.className = "guestbook-entry";
    wrapper.classList.add(
      entry.source === "github"
        ? "guestbook-entry--github"
        : "guestbook-entry--local"
    );

    const header = document.createElement("div");
    header.className = "guestbook-entry__header";

    const identity = document.createElement("div");
    identity.className = "guestbook-entry__identity";

    const nameEl = document.createElement("span");
    nameEl.className = "guestbook-entry__name";
    nameEl.textContent = entry.name || "Anonymous Traveler";

    identity.append(nameEl);

    if (entry.source === "github") {
      const badge = document.createElement("span");
      badge.className = "guestbook-entry__badge";
      badge.title = "Permanent entry stored on GitHub";
      badge.textContent = "permanent";
      identity.append(badge);
    }

    const timeEl = document.createElement("time");
    timeEl.className = "guestbook-entry__time";
    timeEl.dateTime = new Date(entry.timestamp).toISOString();
    timeEl.textContent = formatDate(entry.timestamp);

    header.append(identity, timeEl);

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

function setGuestbookOptionsVisibility(isVisible) {
  if (!guestbookOptionsPanel || !guestbookLeaveButton) return;
  if (isVisible) {
    guestbookOptionsPanel.removeAttribute("hidden");
    guestbookLeaveButton.setAttribute("aria-expanded", "true");
  } else {
    guestbookOptionsPanel.setAttribute("hidden", "true");
    guestbookLeaveButton.setAttribute("aria-expanded", "false");
  }
}

function toggleGuestbookOptions() {
  if (!guestbookOptionsPanel) return;
  setGuestbookOptionsVisibility(guestbookOptionsPanel.hasAttribute("hidden"));
}

function createPrefilledIssueUrl(name, message) {
  const params = new URLSearchParams({
    labels: GITHUB_GUESTBOOK_LABEL,
    title: name,
    body: message,
  });
  return `${GITHUB_NEW_ISSUE_URL}?${params.toString()}`;
}

function setupGuestbookSubmissionOptions() {
  if (!guestbookForm) return;

  const submitButton = guestbookForm.querySelector('button[type="submit"]');
  if (!submitButton) return;

  guestbookLeaveButton = submitButton;
  guestbookLeaveButton.type = "button";
  guestbookLeaveButton.id = "guestbook-leave-mark";
  guestbookLeaveButton.setAttribute("aria-controls", "guestbook-submit-options");
  guestbookLeaveButton.setAttribute("aria-expanded", "false");
  guestbookLeaveButton.setAttribute("aria-haspopup", "true");

  guestbookOptionsPanel = document.createElement("div");
  guestbookOptionsPanel.id = "guestbook-submit-options";
  guestbookOptionsPanel.className = "guestbook-submit-options";
  guestbookOptionsPanel.setAttribute("hidden", "true");

  const githubButton = document.createElement("button");
  githubButton.type = "button";
  githubButton.className =
    "guestbook-submit-options__btn guestbook-submit-options__btn--github";
  githubButton.textContent = "Submit via GitHub Issue (Permanent)";

  const localButton = document.createElement("button");
  localButton.type = "submit";
  localButton.className =
    "guestbook-submit-options__btn guestbook-submit-options__btn--local";
  localButton.textContent = "Save Locally (This Browser Only)";

  guestbookOptionsPanel.append(githubButton, localButton);
  guestbookLeaveButton.after(guestbookOptionsPanel);

  guestbookLeaveButton.addEventListener("click", toggleGuestbookOptions);

  githubButton.addEventListener("click", () => {
    if (!guestbookForm.reportValidity()) return;
    const data = new FormData(guestbookForm);
    const name = data.get("name")?.toString().trim() ?? "";
    const message = data.get("message")?.toString().trim() ?? "";
    if (!name || !message) return;

    const issueUrl = createPrefilledIssueUrl(name, message);
    try {
      const issueWindow = window.open(
        issueUrl,
        "_blank",
        "noopener,noreferrer"
      );
      if (!issueWindow) {
        console.warn(
          "The browser blocked the GitHub Issue window. Allow pop-ups to continue."
        );
      }
    } catch (error) {
      console.warn("Unable to open GitHub Issue window.", error);
    }
    celebrateFormSuccess(
      guestbookForm,
      "Opening GitHub to etch your permanent mark."
    );
    setGuestbookOptionsVisibility(false);
    achievements.recordFormSubmission();
  });
}

async function loadGitHubGuestbook() {
  try {
    const response = await fetch(GITHUB_GUESTBOOK_API, {
      headers: { Accept: "application/vnd.github+json" },
    });

    if (!response.ok) {
      console.warn(
        "GitHub guestbook request failed.",
        response.status,
        response.statusText
      );
      return;
    }

    const issues = await response.json();
    if (!Array.isArray(issues)) {
      console.warn("Unexpected GitHub guestbook response format.");
      return;
    }

    githubGuestbookState = issues.map((issue) => {
      const createdAt = issue?.created_at;
      const timestamp = createdAt ? Date.parse(createdAt) : Date.now();

      return {
        id: `github-${issue?.id ?? crypto.randomUUID()}`,
        name: issue?.title?.trim() || "Anonymous Traveler",
        message: issue?.body?.trim() ?? "",
        timestamp: Number.isFinite(timestamp) ? timestamp : Date.now(),
        source: "github",
        url: issue?.html_url ?? "",
      };
    });
  } catch (error) {
    console.warn("Failed to load guestbook entries from GitHub.", error);
  } finally {
    renderGuestbook();
  }
}

setupGuestbookSubmissionOptions();

guestbookForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  const form = event.target;
  const submitter = event.submitter;
  const isLocalSave =
    submitter instanceof HTMLButtonElement &&
    submitter.classList.contains("guestbook-submit-options__btn--local");

  if (!isLocalSave) {
    setGuestbookOptionsVisibility(true);
    return;
  }

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
  setGuestbookOptionsVisibility(false);
  achievements.recordFormSubmission();
});

renderGuestbook();
loadGitHubGuestbook();

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
  achievements.recordFormSubmission();
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
  achievements.recordCanvasClick();
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

function initJourneyTimeline() {
  if (!journeyNodes.length) return;

  if (journeyObserver) {
    journeyObserver.disconnect();
    journeyObserver = undefined;
  }

  journeyNodes.forEach((node, index) => {
    const delay = motionSafe ? `${index * 120}ms` : "0ms";
    node.style.setProperty("--journey-delay", delay);
    if (motionSafe) {
      node.classList.remove("is-visible");
    } else {
      node.classList.add("is-visible");
    }
  });

  if (!journeySection || !motionSafe || !("IntersectionObserver" in window)) {
    journeyNodes.forEach((node) => node.classList.add("is-visible"));
    return;
  }

  journeyObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.target === journeySection && entry.isIntersecting) {
          journeyNodes.forEach((node) => {
            requestAnimationFrame(() => {
              node.classList.add("is-visible");
            });
          });
          journeyObserver?.disconnect();
        }
      });
    },
    { threshold: 0.4 }
  );

  journeyObserver.observe(journeySection);
}

function setJourneyCardExpansion(targetCard, shouldExpand) {
  if (!journeyCards.length) return;

  journeyCards.forEach((card) => {
    const isTarget = card === targetCard && shouldExpand;
    card.setAttribute("aria-expanded", String(isTarget));
    card
      .closest(".journey-node")
      ?.classList.toggle("is-expanded", Boolean(isTarget));

    const detailId = card.getAttribute("aria-controls");
    if (!detailId) return;
    const detail = document.getElementById(detailId);
    if (detail) {
      detail.setAttribute("aria-hidden", String(!isTarget));
    }
  });
}

function setupJourneyCardInteractions() {
  if (journeyCardsBound || !journeyNodes.length) return;

  journeyCards = journeyNodes
    .map((node) => node.querySelector(".journey-node__card"))
    .filter((card) => card instanceof HTMLElement);

  if (!journeyCards.length) return;

  journeyCards.forEach((card) => {
    card.setAttribute("aria-expanded", "false");
    card.closest(".journey-node")?.classList.remove("is-expanded");

    const detailId = card.getAttribute("aria-controls");
    if (detailId) {
      const detail = document.getElementById(detailId);
      if (detail) {
        detail.setAttribute(
          "aria-hidden",
          detail.getAttribute("aria-hidden") ?? "true"
        );
      }
    }

    card.addEventListener("click", () => {
      const isExpanded = card.getAttribute("aria-expanded") === "true";
      setJourneyCardExpansion(card, !isExpanded);
    });

    card.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        const isExpanded = card.getAttribute("aria-expanded") === "true";
        setJourneyCardExpansion(card, !isExpanded);
      }
    });
  });

  document.addEventListener(
    "click",
    (event) => {
      if (!journeySection?.contains(event.target)) {
        setJourneyCardExpansion(null, false);
      }
    },
    { capture: true }
  );

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      setJourneyCardExpansion(null, false);
    }
  });

  setJourneyCardExpansion(null, false);
  journeyCardsBound = true;
}

initPatternVisuals();
initJourneyTimeline();
setupJourneyCardInteractions();

const manageMotionPreference = (event) => {
  motionSafe = !event.matches;
  if (!motionSafe) {
    document.querySelector(".particle-field")?.remove();
  } else {
    initParticles();
  }
  initPatternVisuals();
  initJourneyTimeline();
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

let visitorClickCount = 0;
let visitorClickTimer;

function revealVisitorStatistics() {
  if (!visitorCounter) return;

  const formatStat = (base, variance) =>
    Math.floor(base + Math.random() * variance).toLocaleString();

  const patterns = formatStat(420, 880);
  const streaks = formatStat(80, 160);
  const marks = formatStat(260, 540);

  const message = `Garden Statistics: ${patterns} patterns created, ${streaks} streaks tracked, ${marks} marks left across all persistence layers.`;
  let statsReveal = visitorCounter.querySelector(".visitor-counter__stats");

  if (!statsReveal) {
    statsReveal = document.createElement("span");
    statsReveal.className = "visitor-counter__stats";
    visitorCounter.appendChild(statsReveal);
  }

  statsReveal.textContent = message;
  showSecretToast(message);
}

visitorCounter?.addEventListener("click", () => {
  visitorClickCount += 1;

  if (visitorClickTimer) {
    window.clearTimeout(visitorClickTimer);
  }

  visitorClickTimer = window.setTimeout(() => {
    visitorClickCount = 0;
  }, 600);

  if (visitorClickCount >= 3) {
    visitorClickCount = 0;
    revealVisitorStatistics();
  }
});

const KONAMI_SEQUENCE = [
  "arrowup",
  "arrowup",
  "arrowdown",
  "arrowdown",
  "arrowleft",
  "arrowright",
  "arrowleft",
  "arrowright",
  "b",
  "a",
];

let konamiProgress = 0;

function isTypingField(element) {
  return (
    element instanceof HTMLInputElement ||
    element instanceof HTMLTextAreaElement ||
    element instanceof HTMLSelectElement ||
    element?.isContentEditable
  );
}

window.addEventListener(
  "keydown",
  (event) => {
    const key = event.key?.toLowerCase();
    if (!key) return;

    const activeElement = document.activeElement;
    if (activeElement && isTypingField(activeElement)) {
      return;
    }

    if (key === KONAMI_SEQUENCE[konamiProgress]) {
      konamiProgress += 1;
      if (konamiProgress === KONAMI_SEQUENCE.length) {
        triggerKonamiSecret();
        konamiProgress = 0;
      }
      return;
    }

    if (key === KONAMI_SEQUENCE[0]) {
      konamiProgress = 1;
      return;
    }

    konamiProgress = 0;
  },
  { passive: true }
);

console.log(
  "🌸 Welcome, curious explorer! The garden has more secrets than meet the eye. Try the Konami code: ↑↑↓↓←→←→BA"
);

let secretToastTimeoutId;

function triggerKonamiSecret() {
  showSecretToast(
    "The Incremental Grinder Remembers: 675 battles, zero damage, infinite patience. You found the secret!",
    { badgeLabel: "Golden Memory", duration: 7200 }
  );
  launchKonamiBurst();
}

function launchKonamiBurst() {
  if (!motionSafe) return;

  const burst = document.createElement("div");
  burst.className = "konami-burst";
  burst.setAttribute("aria-hidden", "true");

  const particleTotal = 28;
  for (let index = 0; index < particleTotal; index += 1) {
    const particle = document.createElement("span");
    particle.className = "konami-burst__particle";

    const angle = (Math.PI * 2 * index) / particleTotal + Math.random() * 0.4;
    const distance = 160 + Math.random() * 120;
    const duration = 900 + Math.random() * 520;

    particle.style.setProperty(
      "--dx",
      `${Math.cos(angle) * distance}px`
    );
    particle.style.setProperty(
      "--dy",
      `${Math.sin(angle) * distance}px`
    );
    particle.style.setProperty("--duration", `${duration}ms`);
    particle.style.setProperty(
      "--scale",
      (0.8 + Math.random() * 0.6).toFixed(2)
    );
    particle.style.setProperty(
      "--delay",
      `${Math.random() * 120}ms`
    );

    burst.appendChild(particle);
  }

  document.body.appendChild(burst);

  window.setTimeout(() => {
    burst.remove();
  }, 1600);
}

function getSecretToast() {
  let toast = document.getElementById(SECRET_TOAST_ID);
  if (toast) return toast;

  toast = document.createElement("div");
  toast.id = SECRET_TOAST_ID;
  toast.className = "secret-toast";
  toast.setAttribute("role", "status");
  toast.setAttribute("aria-live", "polite");
  document.body.appendChild(toast);
  return toast;
}

function showSecretToast(message, options = {}) {
  ensureSecretStyles();
  const toast = getSecretToast();
  if (!toast) return;

  toast.innerHTML = "";

  if (options.badgeLabel) {
    const badge = document.createElement("strong");
    badge.className = "secret-toast__badge";
    badge.textContent = options.badgeLabel;
    toast.appendChild(badge);
  }

  const text = document.createElement("span");
  text.textContent = message;
  toast.appendChild(text);

  toast.classList.add("is-visible");

  if (secretToastTimeoutId) {
    window.clearTimeout(secretToastTimeoutId);
  }

  const duration =
    typeof options.duration === "number" && options.duration > 0
      ? options.duration
      : 6200;

  secretToastTimeoutId = window.setTimeout(() => {
    toast.classList.remove("is-visible");
  }, duration);
}

function ensureSecretStyles() {
  if (document.getElementById(SECRET_STYLE_ID)) return;

  const style = document.createElement("style");
  style.id = SECRET_STYLE_ID;
  style.textContent = `
.secret-toast {
  position: fixed;
  left: 50%;
  bottom: 2.4rem;
  transform: translate(-50%, 16px);
  background: rgba(14, 20, 32, 0.94);
  color: #ffe9b0;
  padding: 0.9rem 1.4rem;
  border-radius: 14px;
  box-shadow: 0 18px 38px rgba(10, 12, 18, 0.46);
  font-size: 0.95rem;
  letter-spacing: 0.01em;
  max-width: min(90vw, 420px);
  text-align: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity 320ms ease, transform 320ms ease;
  z-index: 4800;
}

.secret-toast.is-visible {
  opacity: 1;
  transform: translate(-50%, 0);
}

.secret-toast__badge {
  display: block;
  font-size: 0.82rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #fff2c9;
  margin-bottom: 0.35rem;
}

.visitor-counter__stats {
  display: block;
  margin-top: 0.4rem;
  font-size: 0.85rem;
  color: #ffe9b0;
  text-shadow: 0 0 12px rgba(255, 209, 120, 0.35);
}

.konami-burst {
  position: fixed;
  left: 50%;
  top: 45%;
  width: 1px;
  height: 1px;
  pointer-events: none;
  z-index: 4700;
}

.konami-burst__particle {
  position: absolute;
  left: 0;
  top: 0;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: radial-gradient(circle at center, #fff5d7 0%, #f5c255 48%, rgba(245, 194, 85, 0) 76%);
  box-shadow: 0 0 16px rgba(255, 220, 110, 0.7);
  transform: translate(-50%, -50%) scale(var(--scale, 1));
  animation: konamiSpark var(--duration, 1000ms) ease-out var(--delay, 0ms)
    forwards;
  opacity: 0;
}

@keyframes konamiSpark {
  0% {
    transform: translate(-50%, -50%) scale(var(--scale, 1));
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  100% {
    transform: translate(calc(-50% + var(--dx, 0px)), calc(-50% + var(--dy, 0px)))
      scale(0.3);
    opacity: 0;
  }
}
`;

  document.head.appendChild(style);
}

function createAchievementTracker({ zoneIds = [] } = {}) {
  const defaultState = {
    visits: 0,
    zonesVisited: [],
    canvasClicks: 0,
    formSubmissions: 0,
    badges: {},
  };

  const stored = storage.read(STORAGE_KEYS.achievements, defaultState);

  const state = {
    ...defaultState,
    ...stored,
    visits: Number(stored?.visits) || 0,
    zonesVisited: Array.isArray(stored?.zonesVisited)
      ? stored.zonesVisited.slice()
      : [],
    canvasClicks: Number(stored?.canvasClicks) || 0,
    formSubmissions: Number(stored?.formSubmissions) || 0,
    badges:
      stored?.badges && typeof stored.badges === "object"
        ? { ...stored.badges }
        : {},
  };

  const visited = new Set(state.zonesVisited);
  const totalZoneCount = zoneIds.length;

  const badgeData = {
    patternExplorer: {
      label: "Pattern Explorer",
      message: "Badge unlocked: you have wandered through every zone of the garden.",
    },
    canvasArtist: {
      label: "Canvas Artist",
      message: "Badge unlocked: your artistry left a flurry of marks upon the shared canvas.",
    },
    persistentOne: {
      label: "Persistent One",
      message: "Badge unlocked: your steady returns keep the garden thriving.",
    },
  };

  function persist() {
    state.zonesVisited = Array.from(visited);
    storage.write(STORAGE_KEYS.achievements, state);
  }

  function unlockBadge(key) {
    if (state.badges[key]) return;

    const badge = badgeData[key];
    if (!badge) return;

    state.badges[key] = Date.now();
    persist();
    showSecretToast(badge.message, { badgeLabel: badge.label });
  }

  function recordVisit() {
    state.visits = Number(state.visits) || 0;
    state.visits += 1;
    persist();

    if (state.visits >= 3) {
      unlockBadge("persistentOne");
    }
  }

  function recordZoneVisit(zoneId) {
    if (!zoneId) return;
    if (!visited.has(zoneId)) {
      visited.add(zoneId);
      persist();
    }

    if (totalZoneCount > 0 && visited.size >= totalZoneCount) {
      unlockBadge("patternExplorer");
    }
  }

  function recordCanvasClick() {
    state.canvasClicks = Number(state.canvasClicks) || 0;
    state.canvasClicks += 1;
    persist();

    if (state.canvasClicks >= 10) {
      unlockBadge("canvasArtist");
    }
  }

  function recordFormSubmission() {
    state.formSubmissions = Number(state.formSubmissions) || 0;
    state.formSubmissions += 1;
    persist();
  }

  return {
    recordVisit,
    recordZoneVisit,
    recordCanvasClick,
    recordFormSubmission,
  };
}
