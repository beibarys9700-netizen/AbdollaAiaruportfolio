const IG = 'https://www.instagram.com/superstar_aiaru/';
const PDF_URL = 'assets/Aiaru_Abdolla_Portfolio.pdf';

const ico = {
  ig: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6"/></svg>',
  wa: '<svg viewBox="0 0 24 24"><path d="M3 21l1.6-4.7A8.5 8.5 0 1 1 8 19.5z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.6-2-1-1 .8c-1-.4-2-1.4-2.4-2.4l.8-1-1-2z"/></svg>',
  dl: '<svg viewBox="0 0 24 24" style="width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:1.8;"><path d="M12 3v12m0 0l-4-4m4 4l4-4M4 17v2a2 2 0 002 2h12a2 2 0 002-2v-2"/></svg>'
};

const UI_TEXT = {
  ru: {
    logo: 'Айару Абдолла',
    nav_home: 'Главная',
    nav_about: 'Обо мне',
    nav_resume: 'Резюме',
    nav_media: 'Проекты',
    nav_gallery: 'Галерея',
    nav_pdf: 'PDF Портфолио',
    nav_contact: 'Контакты',
    footer_copy: 'Айару Абдолла · Актриса и вокалистка · Алматы, Казахстан',
    copied_toast: 'Кастинг-анкета скопирована в буфер обмена!'
  },
  kz: {
    logo: 'Айару Абдолла',
    nav_home: 'Басты бет',
    nav_about: 'Мен туралы',
    nav_resume: 'Түйіндеме',
    nav_media: 'Жобалар',
    nav_gallery: 'Галерея',
    nav_pdf: 'PDF Портфолио',
    nav_contact: 'Байланыс',
    footer_copy: 'Айару Абдолла · Актриса және вокалист · Алматы, Қазақстан',
    copied_toast: 'Кастинг-сауалнама алмасу буферіне көшірілді!'
  },
  en: {
    logo: 'Aiaru Abdolla',
    nav_home: 'Home',
    nav_about: 'About',
    nav_resume: 'Resume',
    nav_media: 'Media',
    nav_gallery: 'Gallery',
    nav_pdf: 'PDF Portfolio',
    nav_contact: 'Contact',
    footer_copy: 'Aiaru Abdolla · Actor & Vocalist · Almaty, Kazakhstan',
    copied_toast: 'Casting profile copied to clipboard!'
  }
};

const page = document.body.dataset.page;
const light = document.body.dataset.light === '1';

// Inject Header
document.body.insertAdjacentHTML('afterbegin', `
  <header class="${light ? 'light' : 'solid'}">
    <a class="logo" href="index.html" data-ui="logo">Айару Абдолла</a>
    <div class="nav-right">
      <nav>
        <a href="index.html" class="${page === 'home' ? 'on' : ''}" data-ui="nav_home">Главная</a>
        <a href="about.html" class="${page === 'about' ? 'on' : ''}" data-ui="nav_about">Обо мне</a>
        <a href="resume.html" class="${page === 'resume' ? 'on' : ''}" data-ui="nav_resume">Резюме</a>
        <a href="media.html" class="${page === 'media' ? 'on' : ''}" data-ui="nav_media">Проекты</a>
        <a href="gallery.html" class="${page === 'gallery' ? 'on' : ''}" data-ui="nav_gallery">Галерея</a>
        <a href="${PDF_URL}" download="Aiaru_Abdolla_Portfolio.pdf" data-ui="nav_pdf">PDF Портфолио</a>
        <a href="${IG}" target="_blank" rel="noopener" class="icon-link" aria-label="Instagram">${ico.ig}</a>
        <a href="https://wa.me/77784767899" target="_blank" rel="noopener" class="icon-link" aria-label="WhatsApp">${ico.wa}</a>
        <a href="contact.html" class="btn-c" data-ui="nav_contact">Контакты</a>
      </nav>
      <div class="lang-switch" aria-label="Language">
        <button type="button" data-lang="ru" class="active">RU</button>
        <button type="button" data-lang="kz">KZ</button>
        <button type="button" data-lang="en">EN</button>
      </div>
      <button class="burger" aria-label="Меню">☰</button>
    </div>
  </header>
`);

// Inject Footer & Toast
document.body.insertAdjacentHTML('beforeend', `
  <footer>
    <div class="soc">
      <a href="${IG}" target="_blank" rel="noopener" aria-label="Instagram">${ico.ig}</a>
      <a href="https://wa.me/77784767899" target="_blank" rel="noopener" aria-label="WhatsApp">${ico.wa}</a>
    </div>
    <p>© ${new Date().getFullYear()} <span data-ui="footer_copy">Айару Абдолла · Актриса и вокалистка · Алматы, Казахстан</span></p>
    <div style="margin-top:14px;">
      <a href="admin.html" style="font-size:11.5px;opacity:0.35;text-decoration:none;letter-spacing:0.04em;transition:opacity 0.2s;" onmouseover="this.style.opacity=1" onmouseout="this.style.opacity=0.35">⚙️ Управление сайтом</a>
    </div>
  </footer>
  <div class="toast" id="toast"></div>
`);

// Burger menu
const burger = document.querySelector('.burger');
const nav = document.querySelector('nav');
if (burger && nav) {
  burger.onclick = () => {
    nav.classList.toggle('open');
    burger.textContent = nav.classList.contains('open') ? '✕' : '☰';
  };
  nav.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      nav.classList.remove('open');
      burger.textContent = '☰';
    });
  });
}

// Age calculator (born 2014-07-30)
function calcAge() {
  const now = new Date();
  let age = now.getFullYear() - 2014;
  if (now.getMonth() < 6 || (now.getMonth() === 6 && now.getDate() < 30)) {
    age--;
  }
  document.querySelectorAll('[data-age]').forEach(e => e.textContent = age);
  return age;
}
calcAge();

// Language Switcher Logic (RU / KZ / EN)
let currentLang = localStorage.getItem('aiaru_lang') || 'ru';
if (!['ru', 'kz', 'en'].includes(currentLang)) currentLang = 'ru';

function applyLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('aiaru_lang', lang);
  document.documentElement.lang = lang === 'kz' ? 'kk' : lang;

  // Toggle buttons
  document.querySelectorAll('.lang-switch button').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });

  // Update header/footer UI strings
  const dict = UI_TEXT[lang] || UI_TEXT.ru;
  document.querySelectorAll('[data-ui]').forEach(el => {
    const key = el.dataset.ui;
    if (dict[key]) el.textContent = dict[key];
  });

  // Update all elements with data-ru / data-kz / data-en
  document.querySelectorAll('[data-ru]').forEach(el => {
    const val = el.getAttribute(`data-${lang}`) || el.getAttribute('data-ru');
    if (val !== null) {
      el.innerHTML = val;
    }
  });

  calcAge();
}

document.querySelectorAll('.lang-switch button').forEach(btn => {
  btn.addEventListener('click', () => applyLanguage(btn.dataset.lang));
});
applyLanguage(currentLang);

// Copy Casting Profile to Clipboard
window.copyCastingProfile = () => {
  const age = calcAge();
  const profiles = {
    ru: `АЙАРУ АБДОЛЛА — Кастинг-анкета\nДата рождения: 30.07.2014 (${age} лет)\nРост: 157 см\nГород: Алматы, Казахстан\nЯзыки: Казахский (родной), Русский (свободно), Английский\nНавыки: Вокал (Гран-при), Домбыра, Фортепиано, Гитара, Укулеле, Актёрское мастерство\nОпыт: 25+ проектов (сериал «Было дело» — роль дочери убитой; главные роли в рекламе «Хрум», Central Dent Clinic, «Білімді бол»)\nТел. Айару: +7 778 476 78 99\nМама (Жанар): +7 705 742 97 00\nInstagram: @superstar_aiaru\nПортфолио: https://abdollaaiaruportfolio.vercel.app`,
    kz: `АЙАРУ АБДОЛЛА — Кастинг-сауалнама\nТуған күні: 30.07.2014 (${age} жас)\nБойы: 157 см\nҚала: Алматы, Қазақстан\nТілдер: Қазақ тілі (ана тілі), Орыс тілі (еркін), Ағылшын тілі\nДағдылар: Вокал (Гран-при), Домбыра, Фортепиано, Гитара, Укулеле, Актерлік шеберлік\nТәжірибе: 25+ жоба («Было дело» хикаясы — рөл; «Хрум», Central Dent Clinic, «Білімді бол» жарнамаларында басты рөл)\nАйару тел.: +7 778 476 78 99\nАнасы (Жанар): +7 705 742 97 00\nInstagram: @superstar_aiaru\nПортфолио: https://abdollaaiaruportfolio.vercel.app`,
    en: `AIARU ABDOLLA — Casting Profile\nDOB: July 30, 2014 (Age ${age})\nHeight: 157 cm (5'2")\nLocation: Almaty, Kazakhstan\nLanguages: Kazakh (Native), Russian (Fluent), English\nSkills: Grand Prix Vocalist, Dombra, Piano, Guitar, Ukulele, Acting Training\nCredits: 25+ Film/TV & Commercial credits ("Bylo Delo" TV Series — Supporting Role; Lead in HROOM, Central Dent Clinic, Bilimdi Bol commercials)\nAiaru Phone/WhatsApp: +7 778 476 78 99\nMother (Zhanar): +7 705 742 97 00\nInstagram: @superstar_aiaru\nPortfolio: https://abdollaaiaruportfolio.vercel.app`
  };
  const text = profiles[currentLang] || profiles.ru;
  navigator.clipboard.writeText(text).then(() => {
    const t = document.getElementById('toast');
    if (t) {
      t.textContent = (UI_TEXT[currentLang] || UI_TEXT.ru).copied_toast;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2800);
    }
  });
};

// Reveal animation on scroll
const io = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in');
      io.unobserve(entry.target);
    }
  });
}, { threshold: 0.08 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Video Hover Preview
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

  document.querySelectorAll('.card[data-video]').forEach(card => {
    card.addEventListener('click', () => {
      const src = card.dataset.video;
      const tEl = card.querySelector('.card-title');
      const sEl = card.querySelector('.card-tag');
      vVideo.src = src;
      vTitle.textContent = tEl ? tEl.textContent : '';
      vSub.textContent = sEl ? sEl.textContent : '';
      vModal.classList.add('open');
      vVideo.play().catch(() => {});
    });
  });

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

// Universal Filter Buttons (Media & Gallery)
document.querySelectorAll('[data-filter-group]').forEach(group => {
  const buttons = group.querySelectorAll('button[data-f]');
  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.remove('on'));
      btn.classList.add('on');
      const f = btn.dataset.f;
      document.querySelectorAll('.card[data-c], .gal-item[data-c]').forEach(item => {
        const match = (f === 'all' || item.dataset.c === f);
        item.classList.toggle('hide', !match);
      });
    });
  });
});

// Interactive Gallery Lightbox Viewer (with keyboard & touch swipe)
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
    const titleEl = item.querySelector('.gal-item-info h4');
    const descEl = item.querySelector('.gal-item-info span');

    lb.querySelector('.lb-img').src = img.src;
    lb.querySelector('.lb-caption h3').textContent = titleEl ? titleEl.textContent : '';
    lb.querySelector('.lb-caption p').textContent = descEl ? descEl.textContent : '';
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

  // Touch swipe support on mobile
  let startX = 0;
  lb.addEventListener('touchstart', (e) => {
    startX = e.changedTouches[0].screenX;
  }, { passive: true });
  lb.addEventListener('touchend', (e) => {
    const diff = e.changedTouches[0].screenX - startX;
    if (Math.abs(diff) > 45) {
      if (diff > 0) showImage(currentIndex - 1);
      else showImage(currentIndex + 1);
    }
  }, { passive: true });

  window.showGalleryImage = showImage;
}

// ================= LIVE CMS OVERRIDE (FROM LOCALSTORAGE) =================
(function initLiveCMS() {
  const customDataStr = localStorage.getItem('aiaru_portfolio_custom_data');
  if (!customDataStr) return;
  try {
    const data = JSON.parse(customDataStr);
    
    // Hero Cover & Focus
    if (data.hero) {
      const heroEl = document.getElementById('home-hero');
      if (heroEl) {
        if (data.hero.image) heroEl.style.backgroundImage = `url("${data.hero.image}")`;
        if (data.hero.focus) heroEl.style.backgroundPosition = data.hero.focus;
      }
    }

    // Home Rows
    if (data.home_rows) {
      const r1 = document.querySelector('#home-row1-img img');
      if (r1 && data.home_rows.row1_image) r1.src = data.home_rows.row1_image;
      const r2 = document.querySelector('#home-row2-img img');
      if (r2 && data.home_rows.row2_image) r2.src = data.home_rows.row2_image;
    }

    // Dynamic Gallery update (if items were modified in Admin)
    if (data.gallery && page === 'gallery') {
      const grid = document.getElementById('gallery-grid');
      if (grid && data.gallery.length) {
        grid.innerHTML = data.gallery.map(it => `
          <div class="gal-item${it.is_wide ? ' wide' : ''} reveal in" data-c="${it.cat}" data-id="${it.id}">
            <img src="${it.src}" alt="${it.title_ru || ''}" loading="lazy">
            <div class="gal-item-info">
              <div>
                <h4>${it.title_ru || ''}</h4>
                <span>${it.desc_ru || ''}</span>
              </div>
            </div>
          </div>
        `).join('');

        grid.querySelectorAll('.gal-item').forEach(item => {
          item.addEventListener('click', () => {
            const visible = Array.from(document.querySelectorAll('.gal-item:not(.hide)'));
            const idx = visible.indexOf(item);
            if (idx !== -1 && window.showGalleryImage) window.showGalleryImage(idx);
          });
        });
      }
    }
  } catch (err) {
    console.error('Error applying live CMS data:', err);
  }
})();
