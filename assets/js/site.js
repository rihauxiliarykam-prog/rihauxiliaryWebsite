// Site behaviour: mobile navigation + scroll-in animations.
// No dependencies. Animations use transform/opacity only (GPU-composited,
// no layout work) and are skipped entirely for prefers-reduced-motion.
(function () {
  'use strict';

  // Marks that JS is running; the CSS only hides animated elements under html.js,
  // so with JS disabled everything renders instantly and nothing is lost.
  document.documentElement.classList.add('js');

  /* ---------- Mobile navigation ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');

  function setOpen(open) {
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });

    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        setOpen(false);
        toggle.focus();
      }
    });

    window.matchMedia('(min-width: 1081px)').addEventListener('change', function (e) {
      if (e.matches) setOpen(false);
    });
  }

  /* ---------- Scroll-in animations ---------- */
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // [data-pullup]: split a plain-text heading into words that rise in one by one.
  document.querySelectorAll('[data-pullup]').forEach(function (el) {
    var words = el.textContent.trim().split(/\s+/);
    el.textContent = '';
    words.forEach(function (word, i) {
      var span = document.createElement('span');
      span.className = 'pu-w';
      span.textContent = word;
      span.style.transitionDelay = (i * 0.07) + 's';
      el.appendChild(span);
      if (i < words.length - 1) el.appendChild(document.createTextNode(' '));
    });
    el.classList.add('pu');
  });

  // [data-reveal-group]: each direct child fades up with a small stagger.
  document.querySelectorAll('[data-reveal-group]').forEach(function (group) {
    Array.prototype.forEach.call(group.children, function (child, i) {
      child.setAttribute('data-reveal', '');
      child.style.transitionDelay = (Math.min(i, 7) * 0.08) + 's';
    });
  });

  var seen = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        seen.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -6% 0px' });

  // Elements already in the first viewport animate right away (double rAF so the
  // hidden initial style paints first and the transition actually runs);
  // everything below the fold waits for the observer.
  var animated = document.querySelectorAll('.pu, [data-reveal]');
  requestAnimationFrame(function () {
    requestAnimationFrame(function () {
      animated.forEach(function (el) {
        if (el.getBoundingClientRect().top < window.innerHeight * 0.92) {
          el.classList.add('in');
        } else {
          seen.observe(el);
        }
      });
    });
  });
})();
