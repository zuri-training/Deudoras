// selectors
let mobileNav = document.getElementById("mobile-nav");
let btnClose = document.getElementById("close");
let btnOpen = document.querySelector(".mobileBtnOpen");

// scripting

btnOpen.addEventListener("click", () => (mobileNav.style.display = "block"));
btnClose.addEventListener("click", () => (mobileNav.style.display = "none"));
