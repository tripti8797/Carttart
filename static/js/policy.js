window.addEventListener('scroll', function() {
          // Get the header and navLinks elements
          var header = document.querySelector('header');
          var navLinks = document.querySelector('.nav-links');
          
          // Check if the page is scrolled down
          if (window.scrollY > 0) {  // Adjust the threshold (50px) as needed
            header.classList.add('scrolled');
            navLinks.classList.add('scrolled');
          } else {
            header.classList.remove('scrolled');
            navLinks.classList.remove('scrolled');
          }
        });
    
        
        window.addEventListener('scroll', function() {
          var arrowElement = document.querySelector('.arrow');
          
          if (window.scrollY > 0) {  // You can adjust the threshold as needed
            arrowElement.classList.add('scrolled');
          } else {
            arrowElement.classList.remove('scrolled');
          }
        });
    
        const hamburger = document.getElementById('hamburger');
      const navLinks = document.getElementById('nav-links');
  
      hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('show');
      });