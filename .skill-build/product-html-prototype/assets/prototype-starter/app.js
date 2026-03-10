const tabs = Array.from(document.querySelectorAll(".stage-tab"));
const panels = Array.from(document.querySelectorAll(".stage-panel"));

for (const tab of tabs) {
  tab.addEventListener("click", () => {
    const target = tab.dataset.tab;

    for (const item of tabs) {
      item.classList.toggle("is-active", item === tab);
    }

    for (const panel of panels) {
      panel.classList.toggle("is-active", panel.dataset.panel === target);
    }
  });
}

const timeNode = document.getElementById("live-time");

if (timeNode) {
  const updateTime = () => {
    const formatter = new Intl.DateTimeFormat("en", {
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    });

    timeNode.textContent = formatter.format(new Date());
  };

  updateTime();
  window.setInterval(updateTime, 60_000);
}
