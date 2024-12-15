let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const carousel = document.querySelector('.carousel');

function showSlide(index) {
    if (index >= slides.length) currentSlide = 0;
    else if (index < 0) currentSlide = slides.length - 1;
    else currentSlide = index;
    const offset = -currentSlide * 100;
    carousel.style.transform = `translateX($ {
        offset
    }
    %)`;
}

document.querySelector('.prev').addEventListener('click', () => showSlide(currentSlide - 1));
document.querySelector('.next').addEventListener('click', () => showSlide(currentSlide + 1));
// Hamburger Menu
const menuToggle = document.querySelector('.menu-toggle');
const navMenu = document.querySelector('nav ul');
menuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    }

);