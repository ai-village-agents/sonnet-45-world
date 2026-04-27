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

const zoneButtons = Array.from(document.querySelectorAll(".zone-nav__btn"));
const zones = Array.from(document.querySelectorAll(".zone"));
const heroEnter = document.querySelector(".hero__enter");

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

zoneButtons.forEach((button) => {
  button.addEventListener("click", () => {
    activateZone(button.dataset.target);
  });
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
    .forEach((entry) => {
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
    });
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

function createDotElement(dot) {
  const span = document.createElement("span");
  span.className = "pattern-dot";
  span.style.left = `${dot.x}%`;
  span.style.top = `${dot.y}%`;
  span.style.width = `${dot.size}px`;
  span.style.height = `${dot.size}px`;
  span.style.background = dot.color;
  span.title = `Placed ${formatDate(dot.timestamp)}`;
  span.dataset.id = dot.id;
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
  patternCanvas.appendChild(createDotElement(dot));
});

patternClear?.addEventListener("click", () => {
  if (!patternState.length) return;
  if (!window.confirm("Clear the shared pattern canvas?")) return;
  patternState.splice(0, patternState.length);
  storage.write(STORAGE_KEYS.patterns, patternState);
  renderPattern();
});

renderPattern();
