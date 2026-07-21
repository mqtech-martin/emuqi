// emuqi.com — Interactions
document.addEventListener('DOMContentLoaded', () => {
  // Mobile nav toggle
  const toggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  if (toggle && navLinks) {
    toggle.addEventListener('click', () => navLinks.classList.toggle('active'));
    // Close on link click
    navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinks.classList.remove('active')));
  }
});
