// Navbar Scroll Effect
window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Hamburger menu functionality
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');

hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('show');
});



// // Card
document.addEventListener("DOMContentLoaded", function () {
  const cardGrid = document.querySelector(".card-grid");
  let scrollAmount = 0;
  let scrollSpeed = 0.7; // Adjust for faster/slower movement
  let clone = cardGrid.innerHTML; // Clone the card content for seamless looping
  cardGrid.innerHTML += clone;
  let isPaused = false;

  function autoScroll() {
    if (!isPaused) {
      if (scrollAmount >= cardGrid.scrollWidth / 2) {
        scrollAmount = 0;
        cardGrid.scrollTo({ left: 0, behavior: "instant" });
      } else {
        cardGrid.scrollTo({ left: scrollAmount, behavior: "smooth" });
        scrollAmount += scrollSpeed;
      }
    }
    requestAnimationFrame(autoScroll);
  }

  // Pause scrolling when hovering over any card
  document.querySelectorAll(".card").forEach((card) => {
    card.addEventListener("mouseenter", () => (isPaused = true));
    card.addEventListener("mouseleave", () => (isPaused = false));
  });

  autoScroll();
});
