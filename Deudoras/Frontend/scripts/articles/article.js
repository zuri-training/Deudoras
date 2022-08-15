let mobileNav = document.getElementById('mobile-nav')
let btnClose = document.getElementById('close')
let btnOpen = document.querySelector('.menu')

// scripting

btnOpen.addEventListener('click', () => (mobileNav.style.display = 'flex'))
btnClose.addEventListener('click', () => (mobileNav.style.display = 'none'))
Footer
