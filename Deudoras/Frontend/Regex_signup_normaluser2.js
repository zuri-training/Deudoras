function validateForm(){
var myInput = document.getElementById("password").value;
var myInput2 = document.getElementById("cpassword").value;


if(myInput == ""){
    document.getElementById("message1").innerHTML = "**Fill the password please!";
    return false;
}

if(myInput2 == ""){
    document.getElementById("message2").innerHTML = "**Enter the password please!";
    return false;
}

if(myInput.length < 8){
    document.getElementById("message1").innerHTML = "**Password length must be atleast 8 characters";
    return false;
}


var numbers = /[0-9]/g;
if (!myInput.match(numbers)){
    document.getElementById("message1").innerHTML = "**Password length must contain a number";
    return false;
}    
  

var upperCaseLetters = /[A-Z]/g;
if (!myInput.match(upperCaseLetters)){
    document.getElementById("message1").innerHTML = "**Password length must contain an uppercase";
    return false;
}
  
    
if(myInput != myInput2){
    document.getElementById("message2").innerHTML = "**Passwords are not same";
    return false;
}else{
    alert("Your password created successfully");
    document.write("JavaScript form has been submitted successfully");
}
}


/* check box for password */
function myFunction(){
  if (myInput.type === "password"){
    myInput.type = "text";
  }else{
    myInput.type = "password";
  }
}

/* check box for confirm password */
function myFunc(){
  if (myInput2.type === "password"){
    myInput2.type = "text";
  }else{
    myInput2.type = "password";
  }
}
