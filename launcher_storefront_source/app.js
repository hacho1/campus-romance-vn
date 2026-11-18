(() => {
  "use strict";

  const releaseFeed = "releases/latest.json";
  const launcherPath = "downloads/CampusRomanceLauncher.exe";
  const release = document.getElementById("release");
  const releaseStatus = document.getElementById("release-status");
  const details = document.getElementById("release-details");
  const retry = document.getElementById("release-retry");
  const download = document.getElementById("download-launcher");
  const downloadBlock = document.querySelector(".download-block");
  const downloadStatus = document.getElementById("download-status");

  async function loadRelease() {
    release.dataset.releaseState = "loading";
    releaseStatus.hidden = false;
    releaseStatus.textContent = "최신 버전을 확인하고 있어요.";
    details.hidden = true;
    retry.hidden = true;
    try {
      const response = await fetch(releaseFeed, { cache: "no-store", signal: AbortSignal.timeout(12000) });
      if (!response.ok) throw new Error("Release metadata unavailable");
      const data = await response.json();
      if (data.schema !== 1 || data.product !== "campus-romance" || typeof data.version !== "string" || !data.version.trim()) {
        throw new Error("Unexpected release metadata");
      }
      document.getElementById("release-version").textContent = "버전 " + data.version.slice(0, 40);
      const build = document.getElementById("release-build");
      const releaseScope = "CH01–07 공통 루트 / 로만 R01–R06";
      build.textContent = data.build == null ? releaseScope : "빌드 " + String(data.build).slice(0, 40) + " / " + releaseScope;
      const notes = document.getElementById("release-notes");
      notes.replaceChildren();
      const entries = Array.isArray(data.release_notes) ? data.release_notes.filter(note => typeof note === "string").slice(0, 12) : [];
      for (const note of entries) {
        const item = document.createElement("li");
        item.textContent = note.slice(0, 600);
        notes.append(item);
      }
      if (!entries.length) {
        const item = document.createElement("li");
        item.textContent = "이 버전의 변경 사항은 아직 등록되지 않았어요.";
        notes.append(item);
      }
      release.dataset.releaseState = "ready";
      releaseStatus.hidden = true;
      details.hidden = false;
    } catch {
      release.dataset.releaseState = "error";
      releaseStatus.textContent = "최신 버전 정보를 불러오지 못했어요. 잠시 후 다시 확인해 주세요.";
      retry.hidden = false;
    }
  }

  async function checkDownload() {
    try {
      const response = await fetch(launcherPath, { method: "HEAD", cache: "no-store", signal: AbortSignal.timeout(12000) });
      const type = response.headers.get("content-type") || "";
      if (!response.ok || type.includes("text/html")) throw new Error("Launcher unavailable");
      downloadBlock.dataset.downloadState = "ready";
      download.removeAttribute("aria-disabled");
      downloadStatus.textContent = "PC에 저장한 뒤 실행해 주세요.";
    } catch {
      downloadBlock.dataset.downloadState = "unavailable";
      download.setAttribute("aria-disabled", "true");
      downloadStatus.textContent = "런처 파일을 준비하고 있어요. 준비가 끝나면 여기에서 받을 수 있습니다.";
    }
  }
  download.addEventListener("click", event => {
    if (download.getAttribute("aria-disabled") === "true") event.preventDefault();
  });
  retry.addEventListener("click", loadRelease);

  const screens = [
    { src: "assets/game-main-menu.png", alt: "다섯 사람의 일러스트와 게임 시작 메뉴", caption: "같은 봄이 시작되는 메인 화면" },
    { src: "assets/game-student-profile.png", alt: "사진과 소개, 비밀 메모가 담긴 로만의 프로필", caption: "사진과 메모로 채워지는 우리의 페이지" },
    { src: "assets/game-met-people.png", alt: "큰 인물 사진과 소개가 나란히 놓인 스키와 협합의 페이지", caption: "축제를 준비하며 만난 학생들" }
  ];
  let selected = 0;
  const selectedScreen = document.getElementById("selected-screen");
  const caption = document.getElementById("screen-caption");
  const choices = Array.from(document.querySelectorAll(".screen-choice"));
  choices.forEach((button, index) => button.addEventListener("click", () => {
    selected = index;
    selectedScreen.src = screens[index].src;
    selectedScreen.alt = screens[index].alt;
    caption.textContent = screens[index].caption;
    choices.forEach((choice, choiceIndex) => choice.setAttribute("aria-pressed", String(choiceIndex === index)));
    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      selectedScreen.animate([{ opacity: 0.35 }, { opacity: 1 }], { duration: 180, easing: "ease-out" });
    }
  }));
  const dialog = document.getElementById("screen-dialog");
  document.getElementById("screen-open").addEventListener("click", () => {
    const current = screens[selected];
    const image = document.getElementById("dialog-screen");
    image.src = current.src;
    image.alt = current.alt;
    document.getElementById("dialog-caption").textContent = current.caption;
    dialog.showModal();
  });
  dialog.addEventListener("click", event => {
    if (event.target === dialog) {
      const bounds = dialog.getBoundingClientRect();
      if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
    }
  });

  if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const entranceTargets = document.querySelectorAll("h1 span, .hero-description, .download-block, .about h2, .about p, .screens h2, .screens > p, .gallery, .install-heading, .install-steps li, .release-heading");
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("seen-entry");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.15 });
    entranceTargets.forEach(target => observer.observe(target));
  }

  loadRelease();
  checkDownload();
})();
