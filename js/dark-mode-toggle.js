window.onload = function () {
  const toggleContainer = document.getElementById("dark-mode-toggle-container");
  toggleButton = document.createElement("button");
  toggleButton.setAttribute("id", "dark-mode-toggle");
  toggleContainer.appendChild(toggleButton);

  function setDarkMode(val) {
    const dark = val === true || val === "true";
    toggleButton.innerHTML = "💡";
    toggleButton.setAttribute("title", dark ? "enable light mode" : "enable dark mode");
    document.documentElement.setAttribute("data-darkmode", dark ? "true" : "false");
    localStorage.setItem("darkmode", dark ? "true" : "false");
  }

  function toggleDarkMode() {
    const mode = document.documentElement.getAttribute("data-darkmode");
    setDarkMode(mode !== "true");
  }

  // Sync button label with current state (set by inline script in <head>)
  const current = document.documentElement.getAttribute("data-darkmode");
  setDarkMode(current === "true");

  toggleButton.onclick = toggleDarkMode;
};
