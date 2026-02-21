// Common functions used across all Sankar Motors website pages

/**
 * Toggle FAQ item visibility
 */
function toggleFAQ(element) {
  const answer = element.nextElementSibling;
  const toggle = element.querySelector('.faq-toggle');
  if (answer) {
    answer.classList.toggle('active');
    toggle.classList.toggle('active');
  }
}

/**
 * Show error message to user
 */
function showError(message) {
  const errorEl = document.getElementById("errorMessage");
  if (errorEl) {
    errorEl.textContent = message;
    errorEl.style.display = "block";
    errorEl.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }
}

/**
 * Clear all form fields
 */
function clearForm(formId) {
  const form = document.getElementById(formId);
  if (form) {
    form.reset();
  }
}

/**
 * Validate email format
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Validate phone number (10 digits)
 */
function isValidPhone(phone) {
  const phoneRegex = /^\d{10}$/;
  return phoneRegex.test(phone.replace(/\D/g, ''));
}

/**
 * Format phone number
 */
function formatPhoneNumber(phone) {
  const cleaned = phone.replace(/\D/g, '');
  if (cleaned.length === 10) {
    return cleaned.slice(0, 3) + '-' + cleaned.slice(3, 6) + '-' + cleaned.slice(6);
  }
  return phone;
}

/**
 * Search products by name
 */
function searchProducts(searchTerm) {
  // Search feature removed
}

/**
 * Smooth scroll to section
 */
function scrollToSection(sectionId) {
  const element = document.getElementById(sectionId);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
}

/**
 * Open WhatsApp chat
 */
function openWhatsApp(message = '') {
  const phoneNumber = '919246485044';
  const encodedMessage = encodeURIComponent(message);
  const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodedMessage}`;
  window.open(whatsappUrl, '_blank');
}

/**
 * Copy text to clipboard
 */
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert('Copied: ' + text);
  }).catch(() => {
    // Fallback for older browsers
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert('Copied: ' + text);
  });
}

/**
 * Add loading spinner to button
 */
function setButtonLoading(buttonId, isLoading) {
  const button = document.getElementById(buttonId);
  if (button) {
    if (isLoading) {
      button.disabled = true;
      button.textContent = '⏳ Processing...';
    } else {
      button.disabled = false;
      button.textContent = button.dataset.originalText || 'Submit';
    }
  }
}

/**
 * Validate required fields
 */
function validateRequiredFields(fieldIds) {
  let isValid = true;
  fieldIds.forEach(fieldId => {
    const field = document.getElementById(fieldId);
    if (field && !field.value.trim()) {
      field.style.borderColor = '#ef4444';
      field.style.backgroundColor = '#fef2f2';
      isValid = false;
    } else if (field) {
      field.style.borderColor = '#e0e0e0';
      field.style.backgroundColor = 'white';
    }
  });
  return isValid;
}

/**
 * Initialize tooltips
 */
function initializeTooltips() {
  const tooltips = document.querySelectorAll('[data-tooltip]');
  tooltips.forEach(element => {
    element.addEventListener('mouseenter', function() {
      const tooltipText = this.dataset.tooltip;
      const tooltip = document.createElement('div');
      tooltip.className = 'tooltip';
      tooltip.textContent = tooltipText;
      tooltip.style.position = 'absolute';
      tooltip.style.backgroundColor = '#333';
      tooltip.style.color = 'white';
      tooltip.style.padding = '8px 12px';
      tooltip.style.borderRadius = '4px';
      tooltip.style.fontSize = '0.85em';
      this.appendChild(tooltip);
    });
    
    element.addEventListener('mouseleave', function() {
      const tooltip = this.querySelector('.tooltip');
      if (tooltip) tooltip.remove();
    });
  });
}

/**
 * Mobile menu toggle
 */
function toggleMobileMenu() {
  const nav = document.querySelector('nav');
  if (nav) {
    nav.classList.toggle('mobile-active');
  }
}

/**
 * Lazy load images
 */
function initLazyLoading() {
  const images = document.querySelectorAll('img[data-src]');
  
  if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          observer.unobserve(img);
        }
      });
    });
    
    images.forEach(img => imageObserver.observe(img));
  } else {
    // Fallback for older browsers
    images.forEach(img => {
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
    });
  }
}

/**
 * Initialize all functionality on page load
 */
document.addEventListener('DOMContentLoaded', function() {
  initLazyLoading();
  initializeTooltips();
});

// Export functions for use in HTML
window.toggleFAQ = toggleFAQ;
window.showError = showError;
window.clearForm = clearForm;
window.isValidEmail = isValidEmail;
window.isValidPhone = isValidPhone;
window.searchProducts = searchProducts;
window.scrollToSection = scrollToSection;
window.openWhatsApp = openWhatsApp;
window.copyToClipboard = copyToClipboard;
window.toggleMobileMenu = toggleMobileMenu;
