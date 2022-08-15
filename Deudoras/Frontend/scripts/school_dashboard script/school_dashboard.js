// selectors
let mobileNav = document.getElementById("mobile-nav");
let btnClose = document.getElementById("close");
let btnOpen = document.querySelector(".mobileBtnOpen");

let page1 = document.querySelector(".page1");
let page2 = document.querySelector(".page2");
let next = document.querySelector(".p-end");

// scripting

btnOpen.addEventListener("click", () => (mobileNav.style.display = "flex"));
btnClose.addEventListener("click", () => (mobileNav.style.display = "none"));

next.addEventListener("click", () => {
  page1.style.display = "none";
  page2.style.display = "flex";
});
