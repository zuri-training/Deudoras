const form = document.getElementById('form')
const email = document.getElementById('email')
const password = document.querySelector('#password')
const togglePassword = document.querySelector('#togglePassword')

form.addEventListener('submit', (e) => {
  e.preventDefault()

  checkInputs()
})

function checkInputs() {
  const emailValue = email.value.trim()
  const passwordValue = password.value.trim()

  if (emailValue === '') {
    setError(email, 'Email required')
  } else if (ValidateEmail(email)) {
    email.setCustomValidity('')
    setSuccess(email, 'Success')
  } else {
    email.setCustomValidity('email.@example/com')
    setError(email, 'looks like this is not a valid email')
  }

  if (passwordValue === '') {
    setError(password, 'Password required')
  }
  //  else if (passwordCheck(password)) {
  //   setSuccess(password, 'success')
  // }
  else {
    setSuccess(password, 'success')
  }
}

function setError(input, message) {
  const formControl = input.parentElement
  const small = formControl.querySelector('small')
  // add error message inside small
  small.innerText = message

  formControl.className = 'form-controller error'
}
function setSuccess(input, message) {
  const formControl = input.parentElement
  const small = formControl.querySelector('small')
  small.innerText = message
  formControl.className = 'form-controller success'
}

function ValidateEmail(mail) {
  if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(form.email.value)) {
    return true
  }

  return false
}

function passwordCheck(password) {
  var letters = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/gim
  if (password.value.match(letters)) {
    return true
  } else {
    return false
  }
}

togglePassword.addEventListener('click', function () {
  // toggle the type attribute
  const type =
    password.getAttribute('type') === 'password' ? 'text' : 'password'
  password.setAttribute('type', type)

  // toggle the icon
  this.classList.toggle('bi-eye')
})
