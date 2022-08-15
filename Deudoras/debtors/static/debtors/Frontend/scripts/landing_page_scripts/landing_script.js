var swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  grabCursor: true,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

/* mobile menu bar JS */

let mobileNav = document.getElementById("mobile-nav");
let btnClose = document.getElementById("close");
let btnOpen = document.querySelector(".menu");

btnOpen.addEventListener("click", () => (mobileNav.style.display = "flex"));
btnClose.addEventListener("click", () => (mobileNav.style.display = "none"));

/*Button on clicks */

const seeMoreButton = (document.getElementsByClassName("see-more").onclick =
  function () {
    location.href = "{%url('About us')%}";
  });
const viewCommentButton = (document.getElementsByClassName(
  "view-comment"
).onclick = function () {
  location.href = "{% url('About us')%}";
});
const signup = (document.getElementsByClassName("sain").onclick = function () {
  location.href = "{%url('signup1')%}";
});
