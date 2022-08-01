// pages selector
let firstPage = document.querySelector(".page1");
let firstPageSecond = document.querySelector(".page1-second");
let secondPage = document.querySelector(".page2");
let secondPageSecond = document.querySelector(".page2-second");
let thirdPage = document.querySelector(".page3");
let thirdPageHeader = document.querySelector(".page3-header");
let thirdPageSecond = document.querySelector(".page3-second");

console.log(thirdPageSecond);

// Input field for validation selector

//page1
let schoolName = document.getElementById("SchoolName");
let schoolEmail = document.getElementById("SchoolEmail");
// let emailError = document.getElementById("SchoolEmailError");
// let NameError = document.getElementById("SchoolNameError");

//page 2
let schoolCAC = document.getElementById("SchoolCAC");
let SchoolAddress = document.getElementById("SchoolAddress");
let SchoolLGA = document.getElementById("LGA");

//page 3
let Schoolpassword = document.getElementById("Password");
let ConfirmPassword = document.getElementById("ConfirmPassword");
let agree = document.getElementById("agree");

//button selector
let firstPageBtn = document.getElementById("next-1");
let secondPageBtn = document.getElementById("next-2");
let signUpbtn = document.getElementById("Signup_School_Form");
//input field declare variable

//input field declare variable for regex

let schoolNameRegex;
let schoolEmailRegex;
let schoolCACRegex;
let SchoolAddressRegex;
let SchoolLGARegex;
let SchoolpasswordRegex;
let ConfirmPasswordRegex;
let agreeRegex;

// page 1 validation
schoolName.addEventListener("change", (e) => {
  let Input = e.target.value;
  schoolNameRegex = /^[\D]+/gi.test(Input);
  console.log(schoolNameRegex);
  return schoolNameRegex;
});

schoolEmail.addEventListener("change", (e) => {
  let Input = e.target.value;
  schoolEmailRegex = /^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9+_.-]+$/gi.test(Input);
  console.log(schoolEmailRegex);
  return schoolEmailRegex;
});

firstPageBtn.addEventListener("click", (e) => {
  if (!schoolNameRegex && !schoolEmailRegex) {
    // emailError.style.display = "block";
    // NameError.style.display = "block";
  } else if (!schoolNameRegex) {
    // NameError.style.display = "block";
  } else if (!schoolEmailRegex) {
    // emailError.style.display = "block";
  } else {
    firstPage.style.display = "none";
    firstPageSecond.style.display = "none";
    secondPage.style.display = "flex";
    secondPageSecond.style.display = "flex";
  }
});

// page 2 validation
schoolCAC.addEventListener("change", (e) => {
  let Input = e.target.value;
  schoolCACRegex = /^[0-9]{14}$/gi.test(Input);
  console.log(schoolCACRegex);
  return schoolCACRegex;
});
SchoolAddress.addEventListener("change", (e) => {
  let Input = e.target.value;
  SchoolAddressRegex = /^[a-zA-Z0-9 -]+/gi.test(Input);
  console.log(SchoolAddressRegex);
  return SchoolAddressRegex;
});
SchoolLGA.addEventListener("change", (e) => {
  let Input = e.target.value;
  SchoolLGARegex = /^[a-zA-Z0-9 -]+/gi.test(Input);
  console.log(SchoolLGARegex);
  return SchoolLGARegex;
});

secondPageBtn.addEventListener("click", (e) => {
  if (!schoolCACRegex && !SchoolAddressRegex && !SchoolLGARegex) {
    // CACError.style.display = "block";
    // AddressError.style.display = "block";
    // LGAError.style.display = "block";
  } else if (!schoolCACRegex) {
    // CACError.style.display = "block";
  } else if (!SchoolAddressRegex) {
    // AddressError.style.display = "block";
  } else if (!SchoolLGARegex) {
    // LGAError.style.display = "block";
  } else {
    secondPage.style.display = "none";
    secondPageSecond.style.display = "none";
    thirdPageHeader.style.display = "block";
    thirdPage.style.display = "flex";
    thirdPageSecond.style.display = "flex";
  }
});

// page3 validation
let Password_Input;
Schoolpassword.addEventListener("change", (e) => {
  Password_Input = e.target.value;
  return Password_Input;
});

SchoolpasswordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/gi.test(
  Password_Input
);

ConfirmPassword.addEventListener("change", (e) => {
  console.log("Schoolpaswordregex state" + SchoolpasswordRegex);
  let Input = e.target.value;
  ConfirmPasswordRegex = Password_Input === Input;
  console.log(ConfirmPasswordRegex);
  return ConfirmPasswordRegex;
});
console.log(ConfirmPasswordRegex);

signUpbtn.addEventListener("click", (e) => {
  if (!ConfirmPasswordRegex && !SchoolpasswordRegex) {
    // ConfirmError.style.display = "block";
    // passwordError.style.display = "block";
    // agreeError.style.display = "block";
    e.preventDefault();
  } else if (!SchoolpasswordRegex) {
    e.preventDefault();
    // passwordError.style.display = "block";
  } else if (!ConfirmPassword) {
    // ConfirmError.style.display = "block";
    e.preventDefault();
  } else {
  }
});
