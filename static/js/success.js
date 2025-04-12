
    // Add interactive animations
    document.querySelectorAll('.stat-box').forEach(box => {
        box.addEventListener('mouseenter', () => {
            box.style.animation = 'pulse 0.5s ease, float 2s ease-in-out infinite alternate';
        });
        
        box.addEventListener('mouseleave', () => {
            box.style.animation = 'pulse 2s ease-in-out infinite';
        });
    });
    
    // Add scroll animation
    document.addEventListener('DOMContentLoaded', () => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = 1;
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, { threshold: 0.1 });
        
        document.querySelectorAll('.proven-box, .ratings-box, .stat-box').forEach(el => {
            observer.observe(el);
        });
    });
    
