(function () {
  var header = document.querySelector(".header");
  var btn = document.querySelector(".menu-btn");
  if (!header || !btn) return;
  btn.addEventListener("click", function () {
    var open = header.classList.toggle("is-open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  });
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      header.classList.remove("is-open");
      btn.setAttribute("aria-expanded", "false");
    }
  });
})();
