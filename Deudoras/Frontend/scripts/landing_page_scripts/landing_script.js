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

/*Button on clicks */

const loginButton = (document.getElementsByName("nav-button-1").onclick =
  function () {
    location.href = "";
  });
const signupButton = (document.getElementsByClassName("nav-button-2").onclick =
  function () {
    location.href = "";
  });
const seeMoreButton = (document.getElementsByClassName("see-more").onclick =
  function () {
    location.href = "";
  });
const viewCommentButton = (document.getElementsByClassName(
  "view-comment"
).onclick = function () {
  location.href = "";
});
const signup = (document.getElementsByClassName("sign-up").onclick =
  function () {
    location.href = "";
  });
const registerAccountButton = (document.getElementsByClassName(
  "center register-account"
).onclick = function () {
  location.href = "";
});
const privacyProtectedButton = (document.getElementsByClassName(
  "center how-privacy-protected"
).onclick = function () {
  location.href = "";
});
const cheeckIfDebtorButton = (document.getElementsByClassName(
  "center check-if-debtor"
).onclick = function () {
  location.href = "";
});
const readMoreButton = (document.getElementsByClassName(
  "read-more center"
).onclick = function () {
  location.href = "";
});
