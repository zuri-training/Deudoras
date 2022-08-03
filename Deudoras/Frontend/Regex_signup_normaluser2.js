var myInput = document.getElementById("password");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

myInput.onfocus = function(){
  document.getElementById("message").style.display = "block";
  }

myInput.onblur = function(){
  document.getElementById("message").style.display = "none";
  }

myInput.onkeyup = function(){
  var upperCaseLettters = /[A-Z]/g;
  if (myInput.value.match(upperCaseLetters)){
    capital.classList.remvove("invalid");
    capital.classList.add("valid");
    }else{
      capital.classList.remove("valid");
      capital.classList.add("invalid");
      }
  var numbers = /[0-9]/g;
  if (myInput.value.match(numbers)){
    number.classList.remvove("invalid");
    number.classList.add("valid");
    }else{
      number.classList.remove("valid");
      number.classList.add("invalid");
      }
  if (myInput.value.length >= 8){
    length.classList.remvove("invalid");
    length.classList.add("valid");
    }else{
      length.classList.remove("valid");
      length.classList.add("invalid");
      }
}




