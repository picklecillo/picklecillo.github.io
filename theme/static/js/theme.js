(function () {
  var toggle = document.getElementById("theme-toggle");
  if (!toggle) return;

  var root = document.documentElement;
  toggle.checked = root.getAttribute("data-theme") === "dark";

  toggle.addEventListener("change", function () {
    var theme = toggle.checked ? "dark" : "light";
    root.setAttribute("data-theme", theme);
    try {
      localStorage.setItem("theme", theme);
    } catch (e) {}
  });
})();
