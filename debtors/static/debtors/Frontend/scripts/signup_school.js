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

//page 2
let schoolCAC = document.getElementById("SchoolCAC");
let schoolCACDanger = document.querySelector(".school-danger");
let SchoolAddress = document.getElementById("SchoolAddress");
let SchoolLGA = document.getElementById("LGA");

//page 3
let Schoolpassword = document.getElementById("Password");
let ConfirmPassword = document.getElementById("ConfirmPassword");
let agree = document.getElementById("agree");
let ConfirmError = document.querySelector(".page-3_confirmError");

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
    ConfirmError.innerHTML = "<div> Fill in the field properly </div>";
    ConfirmError.style.display = "block";
    schoolName.style.borderColor = "#d31616";
    schoolEmail.style.borderColor = "#d31616";
  } else if (!schoolNameRegex) {
    ConfirmError.innerHTML = "<div> Input the school name  </div>";
    ConfirmError.style.display = "block";
    schoolName.style.borderColor = "#d31616";
  } else if (!schoolEmailRegex) {
    ConfirmError.innerHTML = "<div> Invalid school email  </div>";
    ConfirmError.style.display = "block";
    schoolEmail.style.borderColor = "#d31616";
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
    ConfirmError.innerHTML = "<div> Fill in the field properly </div>";
    ConfirmError.style.display = "block";
    SchoolAddress.style.borderColor = "#d31616";
    SchoolLGA.style.borderColor = "#d31616";
    schoolCAC.style.borderColor = "#d31616";
  } else if (!schoolCACRegex) {
    schoolCACDanger.style.display = "block";

    schoolCAC.style.borderColor = "#d31616";
  } else if (!SchoolAddressRegex) {
    ConfirmError.innerHTML = "<div> Input the address field  </div>";
    ConfirmError.style.display = "block";
    SchoolAddress.style.borderColor = "#d31616";
  } else if (!SchoolLGARegex) {
    ConfirmError.innerHTML = "<div> Input the LGA field  </div>";
    ConfirmError.style.display = "block";
    SchoolLGA.style.borderColor = "#d31616";
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
  const regex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/gim;
  console.log(Password_Input);
  SchoolpasswordRegex = regex.test(Password_Input);
  console.log(SchoolpasswordRegex);
  return SchoolpasswordRegex, Password_Input;
});

ConfirmPassword.addEventListener("change", (e) => {
  let Input = e.target.value;
  console.log(Input);
  ConfirmPasswordRegex = Password_Input === Input;
  console.log(ConfirmPasswordRegex);
  return ConfirmPasswordRegex;
});
conso6le.log(ConfirmPasswordRegex);

signUpbtn.addEventListener("click", (e) => {
  if (!ConfirmPasswordRegex && !SchoolpasswordRegex) {
    ConfirmError.innerHTML = "<div> Fill in the field properly  </div>";
    ConfirmError.style.display = "block";
    thirdPageHeader.style.display = "none";
    ConfirmPassword.style.borderColor = "#d31616";
    Schoolpassword.style.borderColor = "#d31616";
    e.preventDefault();
  } else if (!SchoolpasswordRegex) {
    ConfirmError.innerHTML = "<div> Use the hint for password </div>";
    ConfirmError.style.display = "block";
    thirdPageHeader.style.display = "none";
    if (Password_Input < 8) {
      ConfirmError.innerHTML = "<div> password is too short </div>";
      ConfirmError.style.display = "block";
      Schoolpassword.style.borderColor = "#d31616";
      e.preventDefault();
    }
    e.preventDefault();
  } else if (!ConfirmPassword) {
    ConfirmError.innerHTML = "<div> Password does not match! </div>";
    ConfirmError.style.display = "block";
    thirdPageHeader.style.display = "none";
    ConfirmPassword.style.borderColor = "#d31616";
    e.preventDefault();
  } else {
  }
});
