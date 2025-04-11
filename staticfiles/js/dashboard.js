document.addEventListener('DOMContentLoaded', function() {
  // Set up dropdown toggles in sidebar
  document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
    toggle.addEventListener('click', function(e) {
      e.stopPropagation();
      const menuId = this.getAttribute('data-menu');
      toggleDropdown(menuId, this);
    });
  });

  // Set up user dropdown in header
  const userDropdown = document.getElementById('userDropdown');
  if (userDropdown) {
    userDropdown.addEventListener('click', function(e) {
      e.stopPropagation();
      this.classList.toggle('active');
    });
  }

  // Close dropdowns when clicking outside
  document.addEventListener('click', function() {
    document.querySelectorAll('.dropdown-menu').forEach(menu => {
      menu.classList.remove('show');
    });
    document.querySelectorAll('.dropdown-toggle .icon-toggle').forEach(icon => {
      icon.classList.remove('rotated');
      icon.classList.remove('fa-chevron-down');
      icon.classList.add('fa-chevron-right');
    });
    if (userDropdown) userDropdown.classList.remove('active');
  });
});

/**
 * Toggle sidebar dropdowns
 */
function toggleDropdown(menuId, element) {
  const menu = document.getElementById(menuId);
  if (!menu) return;
  
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-menu').forEach(drop => {
    if (drop.id !== menuId) {
      drop.classList.remove('show');
      const otherIcon = drop.previousElementSibling?.querySelector('.icon-toggle');
      if (otherIcon) {
        otherIcon.classList.remove('rotated');
        otherIcon.classList.remove('fa-chevron-down');
        otherIcon.classList.add('fa-chevron-right');
      }
    }
  });

  // Toggle current dropdown
  menu.classList.toggle('show');
  
  const icon = element.querySelector('.icon-toggle');
  if (icon) {
    icon.classList.toggle('rotated');
    if (menu.classList.contains('show')) {
      icon.classList.remove('fa-chevron-right');
      icon.classList.add('fa-chevron-down');
    } else {
      icon.classList.remove('fa-chevron-down');
      icon.classList.add('fa-chevron-right');
    }
  }
}

/**
 * Show a notification to the user
 */
function showNotification(message, type = 'success') {
  // Create notification element
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.textContent = message;
  
  // Add to DOM
  document.body.appendChild(notification);
  
  // Remove after delay
  setTimeout(() => {
    notification.classList.add('fade-out');
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}

