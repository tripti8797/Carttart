// Hamburger menu functionality
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');

hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('show');
});

// Scroll event for header and nav-links
window.addEventListener('scroll', function () {
  const header = document.querySelector('header');
  const navLinks = document.querySelector('.nav-links');
  const arrowElement = document.querySelector('.arrow');

  if (window.scrollY > 0) {
    header.classList.add('scrolled');
    navLinks.classList.add('scrolled');
    arrowElement.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
    navLinks.classList.remove('scrolled');
    arrowElement.classList.remove('scrolled');
  }
}); 
 
 // Autoslider
document.addEventListener('DOMContentLoaded', function() {
  const slides = document.querySelectorAll('.slide');
  const sections = document.querySelectorAll('.section');
  let currentSlide = 0;

  // Initialize slider
  function initSlider() {
    slides[0].classList.add('active');
    sections[0].classList.add('active');
  }

  // Change slide
  function changeSlide(index) {
    slides.forEach(slide => slide.classList.remove('active'));
    sections.forEach(section => section.classList.remove('active'));
    
    slides[index].classList.add('active');
    sections[index].classList.add('active');
    currentSlide = index;
  }

  // Section click event
  sections.forEach((section, index) => {
    section.addEventListener('click', () => {
      changeSlide(index);
    });
  });

  // Auto slide change (optional)
  function autoSlide() {
    let nextSlide = (currentSlide + 1) % slides.length;
    changeSlide(nextSlide);
  }

  // Initialize
  initSlider();
  
  // Auto slide every 5 seconds (optional)
  setInterval(autoSlide, 5000);
});








