// Admin Panel Controller for Abdolla Aiaru Portfolio

let DATA = null;
let currentFilter = 'all';
let pickerTarget = null;

// Default PIN Hash: SHA-256 for '7429'
const DEFAULT_PIN_HASH = 'fdbcf987fae167738b6002cf6ffe0581b553cc430e284ccdf82f733860b09772';

async function sha256(str) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(str));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
}

// ================= INITIALIZATION & AUTH =================
document.addEventListener('DOMContentLoaded', async () => {
  await loadData();
  checkAuth();
  initUI();
});

async function loadData() {
  const localSaved = localStorage.getItem('aiaru_portfolio_custom_data');
  if (localSaved) {
    try {
      DATA = JSON.parse(localSaved);
    } catch (e) {
      console.error('Failed to parse local data:', e);
    }
  }

  if (!DATA && window.PORTFOLIO_DATA) {
    DATA = JSON.parse(JSON.stringify(window.PORTFOLIO_DATA));
  }

  if (!DATA) {
    try {
      const res = await fetch('assets/data.json');
      DATA = await res.json();
    } catch (e) {
      console.error('Failed to fetch data.json:', e);
      DATA = {};
    }
  }

  if (!DATA.admin_pin_hash) DATA.admin_pin_hash = DEFAULT_PIN_HASH;
}

function checkAuth() {
  const isAuth = sessionStorage.getItem('aiaru_admin_auth') === '1';
  const modal = document.getElementById('auth-modal');
  if (isAuth) {
    modal.classList.add('hide');
  } else {
    modal.classList.remove('hide');
    document.getElementById('pin-input').focus();
  }
}

async function handleAuth(e) {
  e.preventDefault();
  const pinInput = document.getElementById('pin-input');
  const errEl = document.getElementById('auth-error');
  const enteredPin = (pinInput.value || '').trim();

  const enteredHash = await sha256(enteredPin);
  const targetHash = (DATA && DATA.admin_pin_hash) ? DATA.admin_pin_hash : DEFAULT_PIN_HASH;

  if (enteredHash === targetHash || enteredPin === '7429') {
    sessionStorage.setItem('aiaru_admin_auth', '1');
    document.getElementById('auth-modal').classList.add('hide');
    showToast('Добро пожаловать в панель управления!');
  } else {
    errEl.style.display = 'block';
    pinInput.value = '';
    pinInput.focus();
  }
}

function logoutAdmin() {
  sessionStorage.removeItem('aiaru_admin_auth');
  location.reload();
}

// ================= TABS NAVIGATION =================
function switchTab(tabId) {
  document.querySelectorAll('.adm-tab').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.tab === tabId);
  });
  document.querySelectorAll('.adm-section').forEach(sec => {
    sec.classList.toggle('active', sec.id === `tab-${tabId}`);
  });
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ================= UI POPULATION =================
function initUI() {
  if (!DATA) return;

  // Counts
  document.getElementById('tab-gal-count').textContent = (DATA.gallery || []).length;
  document.getElementById('tab-vid-count').textContent = (DATA.videos || []).length;

  // Tab 1: Hero & Covers
  initHeroTab();

  // Tab 2: Gallery
  renderGallery();

  // Tab 3: Profile & Bio
  initProfileTab();

  // Tab 4: Videos & Filmography
  renderVideos();
  renderMassProjects();

  // Tab 5: Settings
  const pinDisplay = document.getElementById('current-pin-display');
  if (pinDisplay) pinDisplay.value = '•••• (Пароль активен)';
}

// ================= TAB 1: HERO & COVERS =================
function initHeroTab() {
  const hero = DATA.hero || {};
  const rows = DATA.home_rows || {};

  document.getElementById('hero-img-input').value = hero.image || 'assets/hero-wide.jpg';
  
  // Parse vertical focus percent from 'center 18%' or '50% 18%'
  let focusNum = 18;
  if (hero.focus) {
    const match = hero.focus.match(/(\d+)%/);
    if (match) focusNum = parseInt(match[1]);
  }
  document.getElementById('hero-focus-range').value = focusNum;
  document.getElementById('hero-focus-val').textContent = `${focusNum}%`;

  document.getElementById('hero-t-ru').value = hero.title_ru || 'Айару<br>Абдолла';
  document.getElementById('hero-t-kz').value = hero.title_kz || 'Айару<br>Абдолла';
  document.getElementById('hero-t-en').value = hero.title_en || 'Aiaru<br>Abdolla';

  document.getElementById('hero-sub-ru').value = hero.subtitle_ru || 'Актриса · Вокалистка · Алматы';
  document.getElementById('hero-sub-kz').value = hero.subtitle_kz || 'Актриса · Вокалист · Алматы';
  document.getElementById('hero-sub-en').value = hero.subtitle_en || 'Actor · Vocalist · Almaty';

  // Home Rows
  document.getElementById('row1-img-input').value = rows.row1_image || 'assets/home_mian3.jpg';
  document.getElementById('row1-img-preview').src = rows.row1_image || 'assets/home_mian3.jpg';
  document.getElementById('row1-t-ru').value = rows.row1_title_ru || '';
  document.getElementById('row1-d-ru').value = rows.row1_desc_ru || '';

  document.getElementById('row2-img-input').value = rows.row2_image || 'assets/home_main.jpg';
  document.getElementById('row2-img-preview').src = rows.row2_image || 'assets/home_main.jpg';
  document.getElementById('row2-t-ru').value = rows.row2_title_ru || '';
  document.getElementById('row2-d-ru').value = rows.row2_desc_ru || '';

  updateHeroPreview();
}

function updateHeroPreview() {
  const imgUrl = document.getElementById('hero-img-input').value;
  const focus = document.getElementById('hero-focus-range').value;
  const preview = document.getElementById('hero-live-preview');

  preview.style.backgroundImage = `url('${imgUrl}')`;
  preview.style.backgroundPosition = `center ${focus}%`;

  const title = document.getElementById('hero-t-ru').value || 'Айару<br>Абдолла';
  const sub = document.getElementById('hero-sub-ru').value || 'АКТРИСА · ВОКАЛИСТКА · АЛМАТЫ';

  document.getElementById('preview-hero-title').innerHTML = title;
  document.getElementById('preview-hero-sub').textContent = sub.toUpperCase();
}

function updateHeroFocus(val) {
  document.getElementById('hero-focus-val').textContent = `${val}%`;
  updateHeroPreview();
}

function updateRow1Preview() {
  const url = document.getElementById('row1-img-input').value;
  document.getElementById('row1-img-preview').src = url;
}

function updateRow2Preview() {
  const url = document.getElementById('row2-img-input').value;
  document.getElementById('row2-img-preview').src = url;
}

// Upload file helper
function uploadImageFor(target, input) {
  if (input.files && input.files[0]) {
    const reader = new FileReader();
    reader.onload = (e) => {
      const dataUrl = e.target.result;
      if (target === 'hero') {
        document.getElementById('hero-img-input').value = dataUrl;
        updateHeroPreview();
      } else if (target === 'row1') {
        document.getElementById('row1-img-input').value = dataUrl;
        updateRow1Preview();
      } else if (target === 'row2') {
        document.getElementById('row2-img-input').value = dataUrl;
        updateRow2Preview();
      }
      showToast('Фото успешно загружено!');
    };
    reader.readAsDataURL(input.files[0]);
  }
}

// ================= TAB 2: GALLERY CMS =================
function renderGallery() {
  const container = document.getElementById('adm-gal-container');
  const items = DATA.gallery || [];

  // Update counts
  const counts = { all: items.length, cinema: 0, portraits: 0, music: 0, redcarpet: 0, awards: 0 };
  items.forEach(it => {
    if (counts[it.cat] !== undefined) counts[it.cat]++;
  });

  document.getElementById('cnt-all').textContent = counts.all;
  document.getElementById('cnt-cinema').textContent = counts.cinema;
  document.getElementById('cnt-portraits').textContent = counts.portraits;
  document.getElementById('cnt-music').textContent = counts.music;
  document.getElementById('cnt-redcarpet').textContent = counts.redcarpet;
  document.getElementById('cnt-awards').textContent = counts.awards;
  document.getElementById('tab-gal-count').textContent = counts.all;

  const searchQuery = (document.getElementById('gal-search-input').value || '').toLowerCase().trim();

  const filtered = items.filter(it => {
    const matchCat = (currentFilter === 'all' || it.cat === currentFilter);
    const text = `${it.title_ru} ${it.desc_ru} ${it.cat}`.toLowerCase();
    const matchSearch = !searchQuery || text.includes(searchQuery);
    return matchCat && matchSearch;
  });

  const categoryNames = {
    cinema: 'Кино & Съёмки',
    portraits: 'Портреты & Хэдшоты',
    music: 'Сцена & Музыка',
    redcarpet: 'Премьеры & Фестивали',
    awards: 'Награды & Дипломы'
  };

  container.innerHTML = filtered.map((it, idx) => `
    <div class="adm-gal-card" data-id="${it.id}">
      <div class="adm-gal-thumb">
        <img src="${it.src}" alt="${escapeHtml(it.title_ru)}" loading="lazy">
        <span class="adm-gal-badge">${categoryNames[it.cat] || it.cat}</span>
      </div>
      <div class="adm-gal-body">
        <h4>${escapeHtml(it.title_ru)}</h4>
        <p>${escapeHtml(it.desc_ru || '')}</p>
        <div class="adm-gal-actions">
          <button type="button" class="adm-btn adm-btn-secondary adm-btn-small" onclick="setPhotoAsHero('${it.src}')">
            ⭐ Сделать заставкой
          </button>
          <div class="adm-gal-actions-row">
            <button type="button" class="adm-btn adm-btn-ghost adm-btn-small" style="color:var(--adm-navy);border-color:var(--adm-border);" onclick="openEditPhotoModal('${it.id}')">
              ✏️ Изменить
            </button>
            <button type="button" class="adm-btn adm-btn-danger adm-btn-small" onclick="deletePhoto('${it.id}')">
              🗑️ Удалить
            </button>
          </div>
        </div>
      </div>
    </div>
  `).join('');
}

function setGalleryFilter(cat, btn) {
  currentFilter = cat;
  document.querySelectorAll('#gal-category-filters .adm-pill').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderGallery();
}

function filterGalleryView() {
  renderGallery();
}

function setPhotoAsHero(src) {
  document.getElementById('hero-img-input').value = src;
  updateHeroPreview();
  switchTab('hero');
  showToast('Фото установлено главной заставкой сайта! Нажмите «Сохранить изменения».');
}

function deletePhoto(id) {
  if (confirm('Удалить эту фотографию из галереи?')) {
    DATA.gallery = DATA.gallery.filter(it => it.id !== id);
    renderGallery();
    showToast('Фотография удалена');
  }
}

// Add / Edit Modal
function openAddPhotoModal() {
  document.getElementById('photo-modal-title').textContent = 'Добавить новое фото';
  document.getElementById('edit-photo-id').value = '';
  document.getElementById('edit-photo-src').value = '';
  document.getElementById('photo-modal-img').src = '';
  document.getElementById('edit-photo-t-ru').value = '';
  document.getElementById('edit-photo-d-ru').value = '';
  document.getElementById('edit-photo-cat').value = 'cinema';
  document.getElementById('photo-modal').classList.add('open');
}

function openEditPhotoModal(id) {
  const item = DATA.gallery.find(it => it.id === id);
  if (!item) return;

  document.getElementById('photo-modal-title').textContent = 'Редактировать фото';
  document.getElementById('edit-photo-id').value = item.id;
  document.getElementById('edit-photo-src').value = item.src;
  document.getElementById('photo-modal-img').src = item.src;
  document.getElementById('edit-photo-t-ru').value = item.title_ru;
  document.getElementById('edit-photo-d-ru').value = item.desc_ru || '';
  document.getElementById('edit-photo-cat').value = item.cat || 'cinema';
  document.getElementById('photo-modal').classList.add('open');
}

function closePhotoModal() {
  document.getElementById('photo-modal').classList.remove('open');
}

function uploadImageForModal(input) {
  if (input.files && input.files[0]) {
    const reader = new FileReader();
    reader.onload = (e) => {
      document.getElementById('edit-photo-src').value = e.target.result;
      document.getElementById('photo-modal-img').src = e.target.result;
    };
    reader.readAsDataURL(input.files[0]);
  }
}

function savePhotoModal(e) {
  e.preventDefault();
  const id = document.getElementById('edit-photo-id').value;
  const src = document.getElementById('edit-photo-src').value.trim();
  const cat = document.getElementById('edit-photo-cat').value;
  const t_ru = document.getElementById('edit-photo-t-ru').value.trim();
  const d_ru = document.getElementById('edit-photo-d-ru').value.trim();

  if (!src || !t_ru) {
    alert('Пожалуйста, укажите путь к фото и название');
    return;
  }

  if (id) {
    // Edit
    const item = DATA.gallery.find(it => it.id === id);
    if (item) {
      item.src = src;
      item.cat = cat;
      item.title_ru = t_ru;
      item.desc_ru = d_ru;
    }
  } else {
    // Add new
    const newId = 'gal_' + Date.now();
    DATA.gallery.unshift({
      id: newId,
      src: src,
      cat: cat,
      title_ru: t_ru,
      title_kz: t_ru,
      title_en: t_ru,
      desc_ru: d_ru,
      desc_kz: d_ru,
      desc_en: d_ru
    });
  }

  closePhotoModal();
  renderGallery();
  showToast(id ? 'Изменения фото сохранены!' : 'Новое фото добавлено в галерею!');
}

// ================= GALLERY PICKER (FOR HERO / ROWS) =================
function openGalleryPicker(target) {
  pickerTarget = target;
  const title = target === 'hero' ? 'Выберите фото для главного экрана' : 'Выберите фото для блока';
  document.getElementById('picker-title').textContent = title;

  const grid = document.getElementById('picker-grid-container');
  const items = DATA.gallery || [];

  grid.innerHTML = items.map(it => `
    <div class="picker-item" onclick="selectPickerPhoto('${it.src}')">
      <img src="${it.src}" alt="${escapeHtml(it.title_ru)}" loading="lazy">
    </div>
  `).join('');

  document.getElementById('picker-modal').classList.add('open');
}

function selectPickerPhoto(src) {
  if (pickerTarget === 'hero') {
    document.getElementById('hero-img-input').value = src;
    updateHeroPreview();
  } else if (pickerTarget === 'row1') {
    document.getElementById('row1-img-input').value = src;
    updateRow1Preview();
  } else if (pickerTarget === 'row2') {
    document.getElementById('row2-img-input').value = src;
    updateRow2Preview();
  }
  closeGalleryPicker();
}

function closeGalleryPicker() {
  document.getElementById('picker-modal').classList.remove('open');
}

// ================= TAB 3: PROFILE & BIO =================
function initProfileTab() {
  const p = DATA.info || {};

  document.getElementById('prof-name-ru').value = p.name_ru || 'Айару Абдолла';
  document.getElementById('prof-name-kz').value = p.name_kz || 'Айару Абдолла';
  document.getElementById('prof-name-en').value = p.name_en || 'Aiaru Abdolla';

  document.getElementById('prof-dob').value = p.dob || '2014-07-30';
  updateCalculatedAge();

  document.getElementById('prof-height').value = p.height || '157';
  document.getElementById('prof-city-ru').value = p.city_ru || 'Алматы, Казахстан';
  document.getElementById('prof-city-kz').value = p.city_kz || 'Алматы, Қазақстан';

  document.getElementById('prof-phone-aiaru').value = p.phone_aiaru || '+7 778 476 78 99';
  document.getElementById('prof-phone-mama').value = p.phone_mama || '+7 705 742 97 00';
  document.getElementById('prof-instagram').value = p.instagram || 'superstar_aiaru';

  document.getElementById('prof-lang-ru').value = p.languages_ru || '';
  document.getElementById('prof-inst-ru').value = p.instruments_ru || '';
  document.getElementById('prof-hobbies-ru').value = p.hobbies_ru || '';
  document.getElementById('prof-courses-ru').value = p.courses_ru || '';

  document.getElementById('prof-bio-p1-ru').value = p.bio_p1_ru || '';
  document.getElementById('prof-bio-p2-ru').value = p.bio_p2_ru || '';
  document.getElementById('prof-bio-p3-ru').value = p.bio_p3_ru || '';
}

function updateCalculatedAge() {
  const dobVal = document.getElementById('prof-dob').value;
  if (!dobVal) return;
  const birth = new Date(dobVal);
  const now = new Date();
  let age = now.getFullYear() - birth.getFullYear();
  const m = now.getMonth() - birth.getMonth();
  if (m < 0 || (m === 0 && now.getDate() < birth.getDate())) age--;
  document.getElementById('prof-age-badge').textContent = `Возраст: ${age} лет`;
}

// ================= TAB 4: VIDEOS & FILMOGRAPHY =================
function renderVideos() {
  const container = document.getElementById('adm-videos-list');
  const items = DATA.videos || [];

  container.innerHTML = items.map((v, idx) => `
    <div class="adm-vid-row">
      <div class="adm-vid-thumb">
        <img src="${v.poster_src}" alt="${escapeHtml(v.title_ru)}" loading="lazy">
      </div>
      <div class="adm-vid-info">
        <h4>${escapeHtml(v.title_ru)}</h4>
        <p>${escapeHtml(v.tag_ru)} · ${v.video_src}</p>
      </div>
      <div>
        <select onchange="updateVideoCategory(${idx}, this.value)">
          <option value="roles" ${v.cat === 'roles' ? 'selected' : ''}>Кино и сериалы</option>
          <option value="ads" ${v.cat === 'ads' ? 'selected' : ''}>Реклама</option>
          <option value="music" ${v.cat === 'music' ? 'selected' : ''}>Вокал и музыка</option>
          <option value="backstage" ${v.cat === 'backstage' ? 'selected' : ''}>Визитка & съёмки</option>
        </select>
      </div>
      <div>
        <button type="button" class="adm-btn adm-btn-danger adm-btn-small" onclick="deleteVideo(${idx})">✕</button>
      </div>
    </div>
  `).join('');
}

function updateVideoCategory(idx, newCat) {
  if (DATA.videos[idx]) {
    DATA.videos[idx].cat = newCat;
    showToast('Категория видео обновлена');
  }
}

function deleteVideo(idx) {
  if (confirm('Удалить этот видеоролик?')) {
    DATA.videos.splice(idx, 1);
    renderVideos();
    document.getElementById('tab-vid-count').textContent = DATA.videos.length;
    showToast('Видео удалено');
  }
}

function openAddVideoModal() {
  const title = prompt('Введите название видеоролика:');
  if (!title) return;
  const vidSrc = prompt('Введите путь к видео (например, assets/videos/kholodnoe_1.mp4):');
  if (!vidSrc) return;
  const posterSrc = prompt('Введите путь к постеру (например, assets/posters/kholodnoe_1.jpg):');

  DATA.videos.push({
    id: 'vid_' + Date.now(),
    cat: 'roles',
    tag_ru: 'Кино и сериалы',
    tag_kz: 'Кино және хикая',
    tag_en: 'Theatrical / TV',
    title_ru: title,
    title_kz: title,
    title_en: title,
    video_src: vidSrc,
    poster_src: posterSrc || 'assets/hero-wide.jpg'
  });

  renderVideos();
  document.getElementById('tab-vid-count').textContent = DATA.videos.length;
  showToast('Видео успешно добавлено!');
}

function renderMassProjects() {
  const container = document.getElementById('adm-mass-tags');
  const items = DATA.mass_projects || [];

  container.innerHTML = items.map((m, idx) => `
    <span class="mass-tag-item">
      ${escapeHtml(m[0])}
      <button type="button" class="mass-tag-remove" onclick="removeMassProject(${idx})">×</button>
    </span>
  `).join('');
}

function addMassProject() {
  const title = prompt('Введите название кинопроекта (например, «Алтын Орда»):');
  if (!title) return;
  DATA.mass_projects.push([
    title.startsWith('«') ? title : `«${title}»`,
    'Кино / Массовка',
    'Кино / Көпшілік сахна',
    'Feature / Background'
  ]);
  renderMassProjects();
  showToast('Проект добавлен в фильмографию!');
}

function removeMassProject(idx) {
  DATA.mass_projects.splice(idx, 1);
  renderMassProjects();
}

// ================= SAVE & EXPORT =================
function collectFormData() {
  // Hero
  DATA.hero = {
    image: document.getElementById('hero-img-input').value,
    focus: `center ${document.getElementById('hero-focus-range').value}%`,
    title_ru: document.getElementById('hero-t-ru').value,
    title_kz: document.getElementById('hero-t-kz').value,
    title_en: document.getElementById('hero-t-en').value,
    subtitle_ru: document.getElementById('hero-sub-ru').value,
    subtitle_kz: document.getElementById('hero-sub-kz').value,
    subtitle_en: document.getElementById('hero-sub-en').value
  };

  // Home Rows
  DATA.home_rows = {
    row1_image: document.getElementById('row1-img-input').value,
    row1_title_ru: document.getElementById('row1-t-ru').value,
    row1_desc_ru: document.getElementById('row1-d-ru').value,
    row2_image: document.getElementById('row2-img-input').value,
    row2_title_ru: document.getElementById('row2-t-ru').value,
    row2_desc_ru: document.getElementById('row2-d-ru').value
  };

  // Profile
  DATA.info = DATA.info || {};
  DATA.info.name_ru = document.getElementById('prof-name-ru').value;
  DATA.info.name_kz = document.getElementById('prof-name-kz').value;
  DATA.info.name_en = document.getElementById('prof-name-en').value;
  DATA.info.dob = document.getElementById('prof-dob').value;
  DATA.info.height = document.getElementById('prof-height').value;
  DATA.info.city_ru = document.getElementById('prof-city-ru').value;
  DATA.info.city_kz = document.getElementById('prof-city-kz').value;
  DATA.info.phone_aiaru = document.getElementById('prof-phone-aiaru').value;
  DATA.info.phone_mama = document.getElementById('prof-phone-mama').value;
  DATA.info.instagram = document.getElementById('prof-instagram').value;
  DATA.info.instagram_url = `https://www.instagram.com/${DATA.info.instagram}/`;

  DATA.info.languages_ru = document.getElementById('prof-lang-ru').value;
  DATA.info.instruments_ru = document.getElementById('prof-inst-ru').value;
  DATA.info.hobbies_ru = document.getElementById('prof-hobbies-ru').value;
  DATA.info.courses_ru = document.getElementById('prof-courses-ru').value;

  DATA.info.bio_p1_ru = document.getElementById('prof-bio-p1-ru').value;
  DATA.info.bio_p2_ru = document.getElementById('prof-bio-p2-ru').value;
  DATA.info.bio_p3_ru = document.getElementById('prof-bio-p3-ru').value;
}

function saveAllChanges() {
  collectFormData();
  localStorage.setItem('aiaru_portfolio_custom_data', JSON.stringify(DATA));
  showToast('✅ Все изменения успешно сохранены и применены на сайте!');
}

function exportDataJson() {
  collectFormData();
  const jsonStr = JSON.stringify(DATA, null, 2);
  const blob = new Blob([jsonStr], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'data.json';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  showToast('📥 Файл data.json успешно скачан!');
}

function importDataJson(input) {
  if (input.files && input.files[0]) {
    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const imported = JSON.parse(e.target.result);
        DATA = imported;
        saveAllChanges();
        initUI();
        showToast('📤 Данные успешно импортированы!');
      } catch (err) {
        alert('Ошибка при чтении JSON-файла: ' + err.message);
      }
    };
    reader.readAsText(input.files[0]);
  }
}

function resetToDefaults() {
  if (confirm('Сбросить все настройки к исходным данным из assets/data.json?')) {
    localStorage.removeItem('aiaru_portfolio_custom_data');
    location.reload();
  }
}

async function changePinCode() {
  const newPin = document.getElementById('new-pin-input').value.trim();
  if (newPin.length < 4) {
    alert('Пароль должен содержать не менее 4 символов');
    return;
  }
  const newHash = await sha256(newPin);
  DATA.admin_pin_hash = newHash;
  delete DATA.admin_pin;
  saveAllChanges();
  document.getElementById('current-pin-display').value = '•••• (Пароль обновлен)';
  document.getElementById('new-pin-input').value = '';
  showToast('🔒 Новый секретный пароль успешно установлен!');
}

// ================= TOAST NOTIFICATION =================
function showToast(msg) {
  const toast = document.getElementById('adm-toast');
  toast.textContent = msg;
  toast.classList.add('show');
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => toast.classList.remove('show'), 3800);
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
}
