// emuqi.com — MUQI Tech Interactions
document.addEventListener('DOMContentLoaded', () => {
  // Mobile nav toggle
  const toggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  if (toggle && navLinks) {
    toggle.addEventListener('click', () => navLinks.classList.toggle('active'));
    // Close nav on link click (mobile)
    navLinks.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => navLinks.classList.remove('active'));
    });
  }

  // Mobile dropdown support
  document.querySelectorAll('.dropdown > a').forEach(dropLink => {
    dropLink.addEventListener('click', (e) => {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        const menu = dropLink.nextElementSibling;
        if (menu) {
          menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
        }
      }
    });
  });

  // Application page thumbnail swap
  document.querySelectorAll('.application-thumbs').forEach(strip => {
    const heroImg = strip.closest('.application-product-bg')?.querySelector('img');
    if (!heroImg) return;
    strip.querySelectorAll('img').forEach(thumb => {
      thumb.addEventListener('click', () => {
        heroImg.src = thumb.src;
        heroImg.alt = thumb.alt;
        strip.querySelectorAll('img').forEach(t => t.classList.remove('active'));
        thumb.classList.add('active');
      });
    });
  });

  // Application page scroll-reveal for product panels
  if ('IntersectionObserver' in window) {
    const panels = document.querySelectorAll('.application-product-panel');
    panels.forEach(p => { p.style.opacity = '0'; p.style.transform = 'translateY(24px)'; p.style.transition = 'opacity .6s ease, transform .6s ease'; });
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.style.opacity = '1'; e.target.style.transform = 'translateY(0)'; } });
    }, { threshold: 0.15 });
    panels.forEach(p => io.observe(p));
  }
});
