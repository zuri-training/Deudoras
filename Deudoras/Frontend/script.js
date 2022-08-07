const menu = document.querySelector('.menu-icon')
const close = document.querySelector('.close')
const nav = document.querySelector('.nav-bar')

menu.addEventListener('click', () => {
    nav.classList.add('open-nav')
})

close.addEventListener('click', () => {
    nav.classList.remove('open-nav')
})