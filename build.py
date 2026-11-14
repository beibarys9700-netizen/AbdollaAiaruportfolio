import html

HEAD = '''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{t} — Айару Абдолла | Портфолио актрисы и вокалистки</title>
  <meta name="description" content="Официальное портфолио Айару Абдолла (Алматы, Казахстан). Актриса, певица, исполнительница на домбыре и фортепиано. Кино, реклама, видеовизитка, фото и награды.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body data-page="{p}" data-light="{l}">
'''

TAIL = '''
  <script src="main.js"></script>
</body>
</html>
'''

def write_page(name, title, page_id, body, light_header=0):
    content = HEAD.format(t=title, p=page_id, l=light_header) + body + TAIL
    with open(name, 'w', encoding='utf-8') as f:
        f.write(content)

# Massovka list
mass = [
    "«Қыздың жолы жіңішке»",
    "«Қайрат»",
    "«Бір ауылдың баласындай»",
    "«Рестарт»",
    "«Нурикамал»",
    "«Көке»",
    "«Сыныптас» (молодёжный сериал)",
    "«Менің папам Тигр»",
    "«111»",
    "«Тик-так»",
    "«Токсик»",
    "«Гипноз»",
    "«Қазақ әлемі 2»",
    "«Алтын орда»",
    "«Стадион»",
    "«Қазақстан-Үнді-Корея» (международная дорама)",
    "«105»"
]

# Ads list
ads = [
    ("Реклама чипсов «Хрум»", "Главная детская роль в рекламе", "Реклама"),
    ("Реклама «Білімді бол»", "Образовательный центр · Роль ученицы", "Реклама"),
    ("Реклама «CENTRAL DENT CLINIC»", "Стоматологическая клиника · Имиджевый ролик", "Реклама"),
    ("Реклама ресторана «Tito Arcanum»", "Имиджевая реклама ресторана", "Реклама"),
    ("Анонс-реклама фильма «Карина»", "Якутия · Режиссёр Марианна Сиэгэн", "Кино / Анонс"),
    ("Реклама «SHAM SCHOOL»", "Школьная реклама", "Реклама"),
    ("Реклама «Бота Мия»", "Роль главной героини в детстве (бала кезі)", "Реклама")
]

# ----------------- 1. INDEX.HTML -----------------
index_body = '''
<!-- Hero Section -->
<section class="hero" style="background-image:url('assets/hero-wide.jpg');">
  <div class="hero-txt">
    <h1>Айару<br>Абдолла</h1>
    <p>Актриса · Вокалистка · Алматы</p>
  </div>
</section>

<!-- Tagline CTA -->
<section class="dark center tagline reveal">
  <h2>Юная актриса и вокалистка из Казахстана</h2>
  <a class="btn" href="about.html">Познакомиться</a>
</section>

<!-- Content Rows (Balanced 50/50 Grid) -->
<section class="dark">
  <div class="wrap block reveal">
    <div class="row">
      <div class="row-img">
        <img src="assets/gallery/gal_port_white.jpg" alt="Айару Абдолла портрет">
      </div>
      <div class="row-content">
        <h3>Талант, сцена и камера</h3>
        <p>Айару — разносторонняя, эмоциональная и харизматичная юная артистка. Обладательница Гран-при и золотых медалей по вокалу. Поёт, играет на домбыре, фортепиано, гитаре и укулеле. Свободно чувствует себя на съёмочной площадке и быстро находит контакт с режиссёром.</p>
        <a class="btn" href="about.html">Подробнее обо мне</a>
      </div>
    </div>
  </div>

  <div class="wrap block reveal">
    <div class="row rev">
      <div class="row-img">
        <img src="assets/gallery/gal_emotions.jpg" alt="Тест эмоций Айару Абдолла">
      </div>
      <div class="row-content">
        <h3>Опыт в кино и рекламе</h3>
        <p>В фильмографии Айару — драматическая роль дочери убитой в историческом сериале «Было дело» (70-е годы, КТК), роли в рекламе брендов «Хрум», «Central Dent Clinic», «Білімді бол», а также участие в более чем 25 кинопроектах и телесериалах.</p>
        <a class="btn" href="media.html">Смотреть видео и роли</a>
      </div>
    </div>
  </div>

  <!-- Key Casting Stats -->
  <div class="wrap">
    <div class="stats reveal">
      <div>
        <b data-age>12</b>
        <small>Возраст (лет)</small>
      </div>
      <div>
        <b>157</b>
        <small>Рост (см)</small>
      </div>
      <div>
        <b>25+</b>
        <small>Кино и реклама</small>
      </div>
      <div>
        <b>Гран-при</b>
        <small>Вокал и музыка</small>
      </div>
    </div>
  </div>

  <!-- Three Discover Tiles -->
  <div class="wrap block reveal">
    <h2 style="text-align:center;margin-bottom:36px;">Познакомиться ближе</h2>
    <div class="three">
      <a class="tile" href="resume.html">
        <img src="assets/gallery/gal_kazakh_red.jpg" alt="Резюме Айару">
        <span>Резюме</span>
      </a>
      <a class="tile" href="media.html">
        <img src="assets/gallery/gal_boat_roses.jpg" alt="Проекты и видео Айару">
        <span>Проекты</span>
      </a>
      <a class="tile" href="gallery.html">
        <img src="assets/gallery/gal_trophies_1.jpg" alt="Галерея и награды Айару">
        <span>Галерея</span>
      </a>
    </div>
  </div>

  <!-- Call to Action -->
  <div class="center block reveal" style="padding-bottom:100px;">
    <h2 style="font-size:36px;margin-bottom:24px;">Пригласить на пробы и кастинг</h2>
    <a class="btn" href="contact.html">Связаться с нами</a>
  </div>
</section>
'''
write_page('index.html', 'Главная', 'home', index_body, 1)

# ----------------- 2. ABOUT.HTML -----------------
about_body = '''
<main class="wrap">
  <div class="about">
    <div class="reveal">
      <h1>Привет! Я Айару.</h1>
      <p>Мне <b data-age>12</b> лет, я живу в Алматы. С самого детства моё сердце принадлежит сцене, музыке и кино. Я легко перевоплощаюсь в самые разные образы — от драматических глубоких персонажей до ярких, жизнерадостных комедийных героинь.</p>
      <p>Я пою сольно и на большой сцене, играю на четырёх музыкальных инструментах: домбыре, фортепиано, гитаре и укулеле. Профессионально занимаюсь вокалом и актёрским мастерством, побеждала в республиканских и международных конкурсах, завоевав множество кубков Гран-при.</p>
      <p>Свободно говорю на казахском и русском языках, углубленно изучаю английский язык. Всегда открыта к интересным съёмкам в фильмах, сериалах, клипах и рекламных кампаниях!</p>

      <div class="facts">
        <div><span>Имя</span><span>Абдолла Айару</span></div>
        <div><span>Дата рождения</span><span>30 июля 2014</span></div>
        <div><span>Возраст</span><span><span data-age>12</span> лет</span></div>
        <div><span>Рост</span><span>157 см</span></div>
        <div><span>Город</span><span>Алматы, Казахстан</span></div>
        <div><span>Языки</span><span>Казахский (родной) · Русский (свободно) · Английский</span></div>
        <div><span>Инструменты</span><span>Домбыра · Фортепиано · Гитара · Укулеле</span></div>
      </div>

      <div class="chips-group">
        <h3>Хобби и увлечения</h3>
        <ul class="chips">
          <li>Вокал</li>
          <li>Домбыра</li>
          <li>Фортепиано</li>
          <li>Гитара</li>
          <li>Укулеле</li>
          <li>Рисование</li>
          <li>Оригами</li>
          <li>Поделки из бумаги</li>
          <li>Иностранные языки</li>
        </ul>
      </div>

      <div class="chips-group">
        <h3>Курсы и подготовка</h3>
        <ul class="chips">
          <li>Актёрское мастерство</li>
          <li>Вокал</li>
          <li>Домбыра</li>
          <li>Фортепиано</li>
          <li>Английский язык</li>
          <li>Математика</li>
        </ul>
      </div>
    </div>

    <div class="about-aside reveal">
      <img class="about-img" src="assets/gallery/gal_port_white.jpg" alt="Айару Абдолла">
    </div>
  </div>
</main>
'''
write_page('about.html', 'Обо мне', 'about', about_body)

# ----------------- 3. RESUME.HTML -----------------
def render_credit(title, desc, cat):
    if desc:
        return f'<div class="credit"><span><b>{html.escape(title)}</b> — {html.escape(desc)}</span><em>{html.escape(cat)}</em></div>'
    return f'<div class="credit"><span><b>{html.escape(title)}</b></span><em>{html.escape(cat)}</em></div>'

resume_body = f'''
<main class="wrap res" style="max-width:860px;padding-bottom:100px;">
  <h1>Резюме актрисы</h1>
  <p class="res-sub">Абдолла Айару · 30.07.2014 (<span data-age>12</span> лет) · рост 157 см · Алматы, Казахстан</p>

  <h3>Роли в кино и сериалах <span>Кино</span></h3>
  {render_credit("«Было дело» (70-е годы)", "Исторический детективный сериал (КТК) · Фильм «Холодное блюдо» — роль дочери убитой", "Роль")}

  <h3>Реклама и коммерческие съёмки <span>Реклама</span></h3>
  {''.join(render_credit(t, d, c) for t, d, c in ads)}

  <h3>Массовка и групповые сцены <span>Проекты</span></h3>
  {''.join(render_credit(m, "", "Массовка") for m in mass)}

  <h3>Музыкальные достижения и награды <span>Вокал</span></h3>
  {render_credit("Многочисленные кубки Гран-при и дипломы", "Республиканские и международные вокальные конкурсы", "Гран-при")}
  {render_credit("Золотые медали и лауреатство I степени", "Эстрадный и академический вокал", "Награда")}

  <h3>Инструменты и навыки <span>Навыки</span></h3>
  {render_credit("Домбыра, фортепиано, гитара, укулеле", "Музыкальное исполнительское мастерство", "Музыка")}
  {render_credit("Казахский (родной), Русский (свободно), Английский", "Языковая подготовка для кастингов", "Языки")}
  {render_credit("Актёрское мастерство и сценическая речь", "Профессиональные курсы", "Обучение")}
  {render_credit("Рисование, поделки из бумаги, оригами", "Творческие хобби", "Творчество")}

  <div style="margin-top:48px;">
    <a class="btn" href="contact.html">Пригласить на пробы</a>
  </div>
</main>
'''
write_page('resume.html', 'Резюме', 'resume', resume_body)

# ----------------- 4. MEDIA.HTML -----------------
video_items = [
    ('intro_card', 'Видеопрезентация Айару', 'Актёрская самопрезентация для кастинг-директоров', 'roles', 'Визитка'),
    ('kholodnoe_1', '«Было дело» · 70-е годы', '«Холодное блюдо» — драматическая роль дочери убитой', 'roles', 'Кино'),
    ('kholodnoe_2', '«Было дело» · Сцена в отделе', 'Драматический эпизод из сериала', 'roles', 'Сериал'),
    ('ad_hroom', 'Реклама чипсов «Хрум»', 'Главная детская роль в рекламном ролике', 'ads', 'Реклама'),
    ('ad_centraldent', 'Реклама «Central Dent Clinic»', 'Стоматологическая клиника · Имиджевый ролик', 'ads', 'Реклама'),
    ('ad_languages', 'Реклама «Білімді бол»', 'Образовательный центр · Роль прилежной ученицы', 'ads', 'Реклама'),
    ('music_piano', 'Фортепиано и вокал', 'Живой звук и виртуозное исполнение', 'music', 'Музыка'),
    ('music_dombra', 'Игра на домбыре', 'Традиционный казахский кюй на домбыре', 'music', 'Домбыра'),
    ('music_vocal', 'Вокал · Живое исполнение', 'Сольный вокальный номер', 'music', 'Вокал'),
    ('music_stage', 'Выступление на большой сцене', 'Концертное сольное выступление перед зрителями', 'music', 'Сцена'),
    ('music_white_dress', 'Вокал на фоне гор', 'Выступление в белом бальном платье', 'music', 'Вокал'),
    ('music_dombra_dress', 'Домбыра в национальном наряде', 'Исполнение народных мотивов', 'music', 'Домбыра'),
    ('music_nature', 'Песня на природе', 'Музыкальный номер на открытом воздухе', 'music', 'Вокал'),
    ('backstage_boat', 'Съёмки клипа в лодке с розами', 'Красивый атмосферный бэкстейдж', 'backstage', 'Съёмки'),
    ('backstage_direct', 'Репетиция с режиссёром', 'Отработка сцены перед съёмочным дублем', 'backstage', 'Бэкстейдж'),
    ('fashion_podium', 'Подиум и дефиле', 'Модный показ на красной ковровой дорожке', 'backstage', 'Подиум'),
    ('choreo_duet', 'Хореография и танец', 'Современный дуэтный номер на площадке', 'backstage', 'Танец'),
    ('award_ceremony', 'Церемония награждения', 'Вручение диплома победителя конкурса', 'backstage', 'Награды'),
    ('award_medal', 'Награждение медалью', 'Победа на республиканском конкурсе', 'backstage', 'Награды'),
]

cards_html = []
for vid, title, sub, cat, badge in video_items:
    cards_html.append(f'''
    <div class="card reveal" data-c="{cat}">
      <div class="media-frame" onclick="openVideoModal('assets/videos/{vid}.mp4', '{html.escape(title)}', '{html.escape(sub)}')">
        <img src="assets/posters/{vid}.jpg" alt="{html.escape(title)}" loading="lazy">
        <video src="assets/videos/{vid}.mp4" muted loop playsinline preload="none"></video>
        <div class="play-badge" title="Смотреть видео">
          <svg viewBox="0 0 24 24"><polygon points="8 5 19 12 8 19 8 5"/></svg>
        </div>
      </div>
      <div class="card-meta">
        <div class="card-tag">{html.escape(badge)}</div>
        <h4 class="card-title">{html.escape(title)}</h4>
        <p class="card-desc">{html.escape(sub)}</p>
      </div>
    </div>
    ''')

# Massovka extra cards
for idx, m in enumerate(mass):
    cards_html.append(f'''
    <div class="card reveal" data-c="mass">
      <div class="media-frame" onclick="location.href='resume.html'">
        <img src="assets/gallery/gal_emotions.jpg" style="object-position:center {20 + (idx*4)%60}%;" alt="{html.escape(m)}" loading="lazy">
        <div class="play-badge" style="background:rgba(27,49,71,0.85);" title="Подробнее в резюме">
          <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" stroke="#fff" stroke-width="2" fill="none"/></svg>
        </div>
      </div>
      <div class="card-meta">
        <div class="card-tag">Массовка</div>
        <h4 class="card-title">{html.escape(m)}</h4>
        <p class="card-desc">Художественный фильм / Сериал</p>
      </div>
    </div>
    ''')

media_body = f'''
<main class="media-page">
  <div class="media-header">
    <h1>Проекты и видеоматериалы</h1>
    <p>Видеовизитка, кинофрагменты, реклама, сольные выступления и бэкстейдж</p>
  </div>

  <div class="filters">
    <button class="on" data-f="all">Все проекты ({len(video_items) + len(mass)})</button>
    <button data-f="roles">Кино и роли</button>
    <button data-f="ads">Реклама</button>
    <button data-f="music">Музыка и инструменты</button>
    <button data-f="backstage">Съёмки и бэкстейдж</button>
    <button data-f="mass">Массовка ({len(mass)})</button>
  </div>

  <div class="cards">
    {''.join(cards_html)}
  </div>
</main>

<!-- Video Modal Player -->
<div class="v-modal">
  <div class="v-box">
    <button class="v-close" aria-label="Закрыть">✕</button>
    <video controls playsinline></video>
    <div class="v-meta">
      <div>
        <h3 class="v-title"></h3>
        <p class="v-sub"></p>
      </div>
    </div>
  </div>
</div>
'''
write_page('media.html', 'Проекты & Видео', 'media', media_body)

# ----------------- 5. GALLERY.HTML -----------------
gallery_items = [
    ('gal_emotions', 'Тест эмоций (9 состояний)', 'Актёрский тест широты эмоционального диапазона', 'portraits'),
    ('gal_trophies_1', 'Кубки Гран-при и награды', 'Коллекция наград республиканских и международных конкурсов', 'awards'),
    ('gal_trophies_2', 'Медали и кубки победителя', 'Многочисленные победы на вокальных фестивалях', 'awards'),
    ('gal_boat_roses', 'В лодке с розами', 'Художественная фотосессия на озере', 'portraits'),
    ('gal_port_white', 'Студийный хэдшот в белом топе', 'Классический модельный и актёрский портрет', 'portraits'),
    ('gal_leather', 'Образ в кожаной куртке', 'Дерзкий подростковый образ для кинопроб', 'portraits'),
    ('gal_chanel_black', 'Вечерний образ в чёрном платье', 'Элегантный сценический образ', 'portraits'),
    ('gal_park_autumn', 'Осенний портрет в парке', 'Естественный портрет при натуральном освещении', 'portraits'),
    ('gal_port_black', 'Крупный план в студии', 'Глубокий выразительный взгляд', 'portraits'),
    ('gal_roses_bouquet', 'С букетом роз', 'Праздничный студийный портрет', 'portraits'),
    ('gal_kazakh_red', 'Красный национальный камзол', 'Традиционный казахский орнамент и сценический наряд', 'kazakh'),
    ('gal_kazakh_black', 'Чёрный стилизованный наряд', 'Сценический костюм с серебряной вышивкой', 'kazakh'),
    ('gal_dombra_red', 'С домбырой в красном костюме', 'Инструментальное исполнительское искусство', 'kazakh'),
    ('gal_dombra_black', 'С домбырой в чёрном костюме', 'Традиционная домбыра и сцена', 'kazakh'),
    ('gal_dance_arms', 'Элемент казахского танца', 'Пластика и выразительность в движении', 'kazakh'),
    ('gal_full_height', 'Полный рост в национальном образе', 'Сценический образ в полный рост', 'kazakh'),
    ('gal_clinic_doctor', 'На съёмках в клинике', 'Рабочий момент съёмочного процесса с актёром-врачом', 'backstage'),
    ('gal_clinic_gown', 'В больничной палате', 'Съёмки эпизода в клинике', 'backstage'),
    ('gal_lead_actor', 'С коллегой по площадке', 'На съёмках полнометражного фильма', 'backstage'),
    ('gal_director', 'С режиссёром проекта', 'После удачного дубля на съёмочной площадке', 'backstage'),
    ('gal_pink_dress', 'Розовое национальное платье', 'Традиционный шёлковый наряд', 'kazakh'),
    ('gal_white_sport', 'Белый спортивный образ', 'Динамичный современный образ', 'portraits'),
]

gal_cards_html = []
for gid, title, desc, cat in gallery_items:
    gal_cards_html.append(f'''
    <div class="gal-item reveal" data-c="{cat}" data-title="{html.escape(title)}" data-desc="{html.escape(desc)}">
      <img src="assets/gallery/{gid}.jpg" alt="{html.escape(title)}" loading="lazy">
      <div class="gal-item-info">
        <div>
          <h4>{html.escape(title)}</h4>
          <span>{html.escape(desc)}</span>
        </div>
      </div>
    </div>
    ''')

gallery_body = f'''
<main class="gal-page">
  <div class="gal-header">
    <h1>Фотогалерея</h1>
    <p>Актёрские портреты, национальные образы, съёмки и трофеи побед</p>
  </div>

  <div class="filters">
    <button class="on" data-f="all">Все фото ({len(gallery_items)})</button>
    <button data-f="portraits">Портреты & Хэдшоты</button>
    <button data-f="awards">Награды & Кубки</button>
    <button data-f="kazakh">Казахские образы</button>
    <button data-f="backstage">Съёмки & Бэкстейдж</button>
  </div>

  <div class="gal-grid">
    {''.join(gal_cards_html)}
  </div>
</main>

<!-- Interactive Lightbox Viewer -->
<div class="lb">
  <button class="lb-close" aria-label="Закрыть">✕</button>
  <button class="lb-nav lb-prev" aria-label="Предыдущее">❮</button>
  <button class="lb-nav lb-next" aria-label="Следующее">❯</button>
  <div class="lb-content">
    <div class="lb-counter"></div>
    <img class="lb-img" alt="Фото">
    <div class="lb-caption">
      <h3></h3>
      <p></p>
    </div>
  </div>
</div>
'''
write_page('gallery.html', 'Галерея', 'gallery', gallery_body)

# ----------------- 6. CONTACT.HTML -----------------
contact_body = '''
<main class="contact">
  <h1>Связаться с нами</h1>
  <p>По вопросам кастингов, съёмок в кино и рекламе, участия в фестивалях и концертах — звоните или пишите в любое удобное время.</p>

  <div class="cc">
    <div>
      <small>Айару Абдолла</small>
      <a class="phone" href="tel:+77784767899">+7 778 476 78 99</a>
      <a class="btn" href="https://wa.me/77784767899" target="_blank" rel="noopener">Написать в WhatsApp</a>
    </div>

    <div>
      <small>Мама · Жанар</small>
      <a class="phone" href="tel:+77057429700">+7 705 742 97 00</a>
      <a class="btn" href="https://wa.me/77057429700" target="_blank" rel="noopener">Написать в WhatsApp</a>
    </div>
  </div>

  <div style="margin-top:20px;">
    <a class="btn" href="https://www.instagram.com/superstar_aiaru/" target="_blank" rel="noopener" style="padding:16px 36px;">
      Instagram: @superstar_aiaru
    </a>
  </div>
</main>
'''
write_page('contact.html', 'Контакты', 'contact', contact_body)

print("All site pages generated successfully!")
