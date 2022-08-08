/*const form = document.getElementById('form')*/
/*const email = document.getElementById('email')*/
/*const password = document.querySelector('#password')*/
/*const togglePassword = document.querySelector('#submit')*/


  /*function ValidateEmail(email) {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(form.email.value)) {
      return true
    }
  
    return false
  }*/

  const validateEmail = (email) =>{
      return email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/);
  };
  const validate = () =>{
      const $result = $("#result");
      const email = $("#email").val();
      $result.text("");

      if (validateEmail(email)){
          $result.text(email + "is valid :)");
          $result.css("color", "green");
      }else{
          $result.text(email + "is not valid :(");
          $result.css("color", "red");
      }
      return false;
    }
    $("#email").on("input".validate);
  