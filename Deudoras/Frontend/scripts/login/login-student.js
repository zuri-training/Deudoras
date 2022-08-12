const form = document.getElementById('form')
const studentId = document.getElementById('student-id')
const password = document.querySelector('#password')
const togglePassword = document.querySelector('#togglePassword')

form.addEventListener('submit', (e) => {
  e.preventDefault()
  checkInputs()
})

function checkInputs() {
  const studentIdValue = studentId.value.trim()
  const passwordValue = password.value.trim()

  if (studentIdValue === '') {
    setError(studentId, 'Student ID required')
    // document.getElementById('form').preventDefault()
  } else if (studentIdValue !== '' && passwordValue === '') {
    setError(password, 'password required')
  } else {
    setSuccess(studentId, 'success')
    document.getElementById('form').submit()
  }

  if (passwordValue === '') {
    // document.getElementById('form').preventDefault()
    setError(password, 'Password required')
  } else if (passwordValue !== '' && studentIdValue === '') {
    setError(studentId, 'student ID required')
  } else {
    document.getElementById('form').submit()

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

//to view password
togglePassword.addEventListener('click', function () {
  // toggle the type attribute
  const type =
    password.getAttribute('type') === 'password' ? 'text' : 'password'
  password.setAttribute('type', type)

  // toggle the icon
  this.classList.toggle('bi-eye')
})
