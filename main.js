const IG = 'https://www.instagram.com/superstar_aiaru/';
const ico = {
  ig: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6"/></svg>',
  wa: '<svg viewBox="0 0 24 24"><path d="M3 21l1.6-4.7A8.5 8.5 0 1 1 8 19.5z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.6-2-1-1 .8c-1-.4-2-1.4-2.4-2.4l.8-1-1-2z"/></svg>'
};
const page = document.body.dataset.page;
const links = [
  ['index.html', 'Главная', 'home'],
  ['about.html', 'Обо мне', 'about'],
  ['resume.html', 'Резюме', 'resume'],
  ['media.html', 'Проекты & Видео', 'media'],
  ['gallery.html', 'Галерея', 'gallery']
];
const light = document.body.dataset.light === '1';

// Header inject
document.body.insertAdjacentHTML('afterbegin', `
  <header class="${light ? 'light' : 'solid'}">
    <a class="logo" href="index.html">Айару Абдолла</a>
    <button class="burger" aria-label="menu">☰</button>
    <nav>
      ${links.map(l => `<a href="${l[0]}" class="${l[2] === page ? 'on' : ''}">${l[1]}</a>`).join('')}
      <a href="${IG}" target="_blank" aria-label="Instagram" rel="noopener">${ico.ig}</a>
      <a href="https://wa.me/77784767899" target="_blank" aria-label="WhatsApp" rel="noopener">${ico.wa}</a>
      <a href="contact.html" class="btn-c">Контакты</a>
    </nav>
  </header>
`);

// Footer inject
document.body.insertAdjacentHTML('beforeend', `
  <footer>
    <div class="soc">
      <a href="${IG}" target="_blank" aria-label="Instagram" rel="noopener">${ico.ig}</a>
      <a href="https://wa.me/77784767899" target="_blank" aria-label="WhatsApp" rel="noopener">${ico.wa}</a>
    </div>
    <p>© ${new Date().getFullYear()} Айару Абдолла · Актриса и вокалистка · Алматы, Казахстан</p>
  </footer>
`);

// Burger menu
const burger = document.querySelector('.burger');
const nav = document.querySelector('nav');
if (burger && nav) {
  burger.onclick = () => {
    nav.classList.toggle('open');
    burger.textContent = nav.classList.contains('open') ? '✕' : '☰';
  };
}

// Age calculator (born 2014-07-30)
const bd = new Date(2014, 6, 30);
const now = new Date();
let age = now.getFullYear() - 2014;
if (now.getMonth() < 6 || (now.getMonth() === 6 && now.getDate() < 30)) {
  age--;
}
document.querySelectorAll('[data-age]').forEach(e => e.textContent = age);

// IntersectionObserver for reveal animations
const io = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in');
      io.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Video cards hover-preview & modal playback
document.querySelectorAll('.media-frame').forEach(frame => {
  const vid = frame.querySelector('video');
  if (vid) {
    frame.addEventListener('mouseenter', () => {
      vid.play().catch(() => {});
      frame.classList.add('playing');
    });
    frame.addEventListener('mouseleave', () => {
      vid.pause();
      vid.currentTime = 0;
      frame.classList.remove('playing');
    });
  }
});

// Video Modal Player
const vModal = document.querySelector('.v-modal');
if (vModal) {
  const vVideo = vModal.querySelector('video');
  const vTitle = vModal.querySelector('.v-title');
  const vSub = vModal.querySelector('.v-sub');
  const vClose = vModal.querySelector('.v-close');

  window.openVideoModal = (src, title, sub) => {
    vVideo.src = src;
    vTitle.textContent = title || '';
    vSub.textContent = sub || '';
    vModal.classList.add('open');
    vVideo.play().catch(() => {});
  };

  const closeVideo = () => {
    vModal.classList.remove('open');
    vVideo.pause();
    vVideo.currentTime = 0;
    vVideo.src = '';
  };

  if (vClose) vClose.onclick = closeVideo;
  vModal.onclick = (e) => {
    if (e.target === vModal) closeVideo();
  };
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && vModal.classList.contains('open')) closeVideo();
  });
}

// Media filtering
document.querySelectorAll('.filters button').forEach(btn => {
  btn.onclick = () => {
    const parent = btn.parentElement;
    parent.querySelectorAll('button').forEach(b => b.classList.remove('on'));
    btn.classList.add('on');
    const f = btn.dataset.f;
    const cards = document.querySelectorAll('.card, .gal-item');
    cards.forEach(c => {
      const match = (f === 'all' || c.dataset.c === f);
      c.classList.toggle('hide', !match);
    });
  };
});

// Interactive Gallery Lightbox Viewer
const lb = document.querySelector('.lb');
if (lb) {
  let currentIndex = 0;
  let visibleItems = [];

  const updateVisibleItems = () => {
    visibleItems = Array.from(document.querySelectorAll('.gal-item:not(.hide)'));
  };

  const showImage = (index) => {
    updateVisibleItems();
    if (!visibleItems.length) return;
    if (index < 0) index = visibleItems.length - 1;
    if (index >= visibleItems.length) index = 0;
    currentIndex = index;

    const item = visibleItems[currentIndex];
    const img = item.querySelector('img');
    const title = item.dataset.title || '';
    const desc = item.dataset.desc || '';

    lb.querySelector('.lb-img').src = img.src;
    lb.querySelector('.lb-caption h3').textContent = title;
    lb.querySelector('.lb-caption p').textContent = desc;
    lb.querySelector('.lb-counter').textContent = `${currentIndex + 1} / ${visibleItems.length}`;
    lb.classList.add('open');
  };

  document.querySelectorAll('.gal-item').forEach(item => {
    item.addEventListener('click', () => {
      updateVisibleItems();
      const idx = visibleItems.indexOf(item);
      if (idx !== -1) showImage(idx);
    });
  });

  const prevBtn = lb.querySelector('.lb-prev');
  const nextBtn = lb.querySelector('.lb-next');
  const closeBtn = lb.querySelector('.lb-close');

  if (prevBtn) prevBtn.onclick = (e) => { e.stopPropagation(); showImage(currentIndex - 1); };
  if (nextBtn) nextBtn.onclick = (e) => { e.stopPropagation(); showImage(currentIndex + 1); };
  if (closeBtn) closeBtn.onclick = () => lb.classList.remove('open');

  lb.onclick = (e) => {
    if (e.target === lb || e.target.classList.contains('lb-content')) {
      lb.classList.remove('open');
    }
  };

  document.addEventListener('keydown', (e) => {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'ArrowLeft') showImage(currentIndex - 1);
    if (e.key === 'ArrowRight') showImage(currentIndex + 1);
    if (e.key === 'Escape') lb.classList.remove('open');
  });
}
