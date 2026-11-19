import html
import json
import os

with open('assets/data.json', encoding='utf-8') as f:
    SITE_DATA = json.load(f)

info = SITE_DATA['info']
hero = SITE_DATA['hero']
rows = SITE_DATA['home_rows']
videos_data = SITE_DATA['videos']
gallery_data = SITE_DATA['gallery']
mass_projects = SITE_DATA['mass_projects']

# Also export assets/data.js for instant offline and CORS-free admin access
with open('assets/data.js', 'w', encoding='utf-8') as f:
    f.write('window.PORTFOLIO_DATA = ' + json.dumps(SITE_DATA, ensure_ascii=False, indent=2) + ';\n')

HEAD = '''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{t} — Айару Абдолла | Aiaru Abdolla</title>
  <meta name="description" content="Айару Абдолла — юная актриса кино и рекламы, вокалистка (Гран-при), музыкант (домбыра, фортепиано, гитара, укулеле). Алматы, Казахстан.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Lora:ital,wght@0,500;0,600;1,400&family=Manrope:wght@400;500;600;700&family=Onest:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body data-page="{p}" data-light="{l}">
'''

TAIL = '''
  <script src="main.js"></script>
</body>
</html>
'''

def tr(ru, kz, en, tag='span', cls='', extra=''):
    c = f' class="{cls}"' if cls else ''
    ex = f' {extra}' if extra else ''
    return f'<{tag}{c}{ex} data-ru="{html.escape(ru)}" data-kz="{html.escape(kz)}" data-en="{html.escape(en)}">{ru}</{tag}>'

def write_page(name, title, page_id, body, light_header=0):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(HEAD.format(t=title, p=page_id, l=light_header) + body + TAIL)

# ==================== 1. INDEX.HTML ====================
index_body = f'''
<section class="hero" id="home-hero" style="background-image:url('{hero['image']}');background-position:{hero['focus']};">
  <div class="hero-txt">
    {tr(hero['title_ru'], hero['title_kz'], hero['title_en'], "h1", "", 'id="hero-title"')}
    {tr(hero['subtitle_ru'], hero['subtitle_kz'], hero['subtitle_en'], "p", "", 'id="hero-sub"')}
    <div class="hero-actions">
      <a class="btn btn-gold" href="assets/Aiaru_Abdolla_Portfolio.pdf" download="Aiaru_Abdolla_Portfolio.pdf"
         data-ru="Скачать PDF Портфолио" data-kz="PDF Портфолионы жүктеу" data-en="Download PDF Portfolio">Скачать PDF Портфолио</a>
      <button type="button" class="btn" onclick="copyCastingProfile()"
         data-ru="Скопировать кастинг-анкету" data-kz="Сауалнаманы көшіру" data-en="Copy Casting Profile">Скопировать кастинг-анкету</button>
    </div>
  </div>
</section>

<section class="dark center tagline reveal">
  {tr(info['tagline_ru'], info['tagline_kz'], info['tagline_en'], "h2")}
  <a class="btn" href="about.html" data-ru="познакомиться" data-kz="жақынырақ танысу" data-en="what's my deal">познакомиться</a>
</section>

<section class="dark">
  <div class="wrap block reveal">
    {tr("в кадре и на сцене", "кадрда және сахнада", "what's on", "h2")}
    <div class="row">
      <div class="row-img" id="home-row1-img">
        <img src="{rows['row1_image']}" alt="Айару Абдолла с домбырой">
      </div>
      <div class="row-content">
        {tr(rows['row1_title_ru'], rows['row1_title_kz'], rows['row1_title_en'], "h3", "", 'id="home-row1-title"')}
        {tr(rows['row1_desc_ru'], rows['row1_desc_kz'], rows['row1_desc_en'], "p", "", 'id="home-row1-desc"')}
        <a class="btn" href="media.html" data-ru="смотреть видео" data-kz="бейнелерді көру" data-en="watch videos">смотреть видео</a>
      </div>
    </div>
  </div>

  <div class="wrap block reveal">
    {tr("недавние работы", "соңғы жобалар", "recently", "h2")}
    <div class="row rev">
      <div class="row-img" id="home-row2-img">
        <img src="{rows['row2_image']}" alt="Айару Абдолла в сценическом образе">
      </div>
      <div class="row-content">
        {tr(rows['row2_title_ru'], rows['row2_title_kz'], rows['row2_title_en'], "h3", "", 'id="home-row2-title"')}
        {tr(rows['row2_desc_ru'], rows['row2_desc_kz'], rows['row2_desc_en'], "p", "", 'id="home-row2-desc"')}
        <a class="btn" href="resume.html" data-ru="полное резюме" data-kz="толық түйіндеме" data-en="full resume">полное резюме</a>
      </div>
    </div>
  </div>

  <div class="wrap">
    <div class="stats reveal">
      <div>
        <b data-age>12</b>
        {tr("лет · 30.07.2014", "жас · 30.07.2014", "years old · 2014", "small")}
      </div>
      <div>
        <b>{info['height']}</b>
        {tr("рост (см)", "бойы (см)", "height (cm)", "small")}
      </div>
      <div>
        <b>25+</b>
        {tr("кино и реклама", "кино және жарнама", "film & commercials", "small")}
      </div>
      <div>
        <b>4</b>
        {tr("инструмента + вокал", "музыкалық аспап + вокал", "instruments + vocals", "small")}
      </div>
    </div>
  </div>

  <div class="wrap block reveal">
    {tr("разделы портфолио", "портфолио бөлімдері", "extra extra", "h2")}
    <div class="three">
      <a class="tile" href="resume.html">
        <img src="assets/p1.jpg" alt="Резюме">
        {tr("резюме", "түйіндеме", "resume", "span")}
      </a>
      <a class="tile" href="media.html">
        <img src="assets/gallery/gal_boat_roses.jpg" alt="Проекты">
        {tr("видео и роли", "бейнелер", "production", "span")}
      </a>
      <a class="tile" href="gallery.html">
        <img src="assets/gallery/gal_p_18.jpg" alt="Галерея">
        {tr("фотогалерея", "галерея", "headshots", "span")}
      </a>
    </div>
  </div>

  <div class="center block reveal" style="padding-bottom:96px;">
    {tr("пригласить на пробы", "сынамаға шақыру", "reach out", "h2")}
    <div style="display:flex;justify-content:center;gap:14px;flex-wrap:wrap;">
      <a class="btn" href="contact.html" data-ru="контакты" data-kz="байланыс" data-en="contact">контакты</a>
      <a class="btn btn-gold" href="assets/Aiaru_Abdolla_Portfolio.pdf" download="Aiaru_Abdolla_Portfolio.pdf"
         data-ru="скачать PDF (2 стр.)" data-kz="PDF жүктеу (2 бет)" data-en="download PDF (2 pages)">скачать PDF (2 стр.)</a>
    </div>
  </div>
</section>
'''
write_page('index.html', 'Главная', 'home', index_body, 1)

# ==================== 2. ABOUT.HTML ====================
about_body = f'''
<main class="wrap">
  <div class="about">
    <div class="reveal">
      {tr("Привет! Я Айару.", "Сәлем! Мен Айарумын.", "Hey there! I'm Aiaru.", "h1")}
      {tr(info['bio_p1_ru'], info['bio_p1_kz'], info['bio_p1_en'], "p")}
      {tr(info['bio_p2_ru'], info['bio_p2_kz'], info['bio_p2_en'], "p")}
      {tr(info['bio_p3_ru'], info['bio_p3_kz'], info['bio_p3_en'], "p")}

      <div class="facts">
        <div>
          {tr("Имя", "Аты-жөні", "Full Name")}
          {tr(info['name_ru'], info['name_kz'], info['name_en'])}
        </div>
        <div>
          {tr("Дата рождения", "Туған күні", "Date of Birth")}
          {tr("30 июля 2014 (<span data-age>12</span> лет)", "30 шілде 2014 (<span data-age>12</span> жас)", "July 30, 2014 (Age <span data-age>12</span>)")}
        </div>
        <div>
          {tr("Рост", "Бойы", "Height")}
          {tr(f"{info['height']} см", f"{info['height']} см", f"{info['height']} cm (5'2\\\")")}
        </div>
        <div>
          {tr("Город", "Қала", "Location")}
          {tr(info['city_ru'], info['city_kz'], info['city_en'])}
        </div>
        <div>
          {tr("Языки", "Тілдер", "Languages")}
          {tr(info['languages_ru'], info['languages_kz'], info['languages_en'])}
        </div>
        <div>
          {tr("Инструменты", "Музыкалық аспаптар", "Instruments")}
          {tr(info['instruments_ru'], info['instruments_kz'], info['instruments_en'])}
        </div>
      </div>

      <div class="chips-group">
        {tr("Хобби и творчество", "Хобби және шығармашылық", "Hobbies & Interests", "h3")}
        {tr(info['hobbies_ru'], info['hobbies_kz'], info['hobbies_en'], "div", "dot-list")}
      </div>

      <div class="chips-group">
        {tr("Курсы и обучение", "Курстар мен дайындық", "Training & Courses", "h3")}
        {tr(info['courses_ru'], info['courses_kz'], info['courses_en'], "div", "dot-list")}
      </div>

      <div class="about-actions">
        <a class="btn" href="assets/Aiaru_Abdolla_Portfolio.pdf" download="Aiaru_Abdolla_Portfolio.pdf"
           data-ru="Скачать PDF Портфолио" data-kz="PDF Портфолионы жүктеу" data-en="Download PDF Portfolio">Скачать PDF Портфолио</a>
        <button type="button" class="btn" onclick="copyCastingProfile()"
           data-ru="Скопировать анкету" data-kz="Сауалнаманы көшіру" data-en="Copy Casting Info">Скопировать анкету</button>
      </div>
    </div>

    <div class="about-aside reveal">
      <img class="about-img" src="assets/p2.jpg" alt="Айару Абдолла">
      <img class="about-img" src="assets/gallery/gal_p_18.jpg" style="aspect-ratio:1/1;" alt="Айару с лошадью в степи">
    </div>
  </div>
</main>
'''
write_page('about.html', 'Обо мне', 'about', about_body)

# ==================== 3. RESUME.HTML ====================
def cred_row(title_ru, title_kz, title_en, role_ru, role_kz, role_en):
    return f'''
    <div class="credit">
      {tr(title_ru, title_kz, title_en, "span")}
      {tr(role_ru, role_kz, role_en, "em")}
    </div>'''

mass_rows = []
for title, ru_r, kz_r, en_r in mass_projects:
    mass_rows.append(cred_row(title, title, title, ru_r, kz_r, en_r))

resume_body = f'''
<main class="wrap res">
  <div class="res-top reveal">
    <div>
      {tr("Айару Абдолла", "Айару Абдолла", "Aiaru Abdolla", "h1")}
      {tr("Актриса · Вокалистка · Алматы, Казахстан", "Актриса · Вокалист · Алматы, Қазақстан", "Actor · Vocalist · Almaty, Kazakhstan", "p")}
    </div>
    <div class="res-actions">
      <a class="btn btn-gold" href="assets/Aiaru_Abdolla_Portfolio.pdf" download="Aiaru_Abdolla_Portfolio.pdf"
         data-ru="Скачать PDF Резюме" data-kz="PDF Түйіндемені жүктеу" data-en="Download PDF Resume">Скачать PDF Резюме</a>
      <button type="button" class="btn" onclick="copyCastingProfile()"
         data-ru="Скопировать анкету" data-kz="Сауалнаманы көшіру" data-en="Copy Casting Profile">Скопировать анкету</button>
      <a class="btn" href="contact.html" data-ru="Связаться" data-kz="Байланысу" data-en="Contact">Связаться</a>
    </div>
  </div>

  <section class="res-sec reveal">
    {tr("Характеристики и параметры", "Сипаттамасы мен өлшемдері", "Physical Characteristics & Stats", "h2")}
    <div class="stats-table">
      <div><span>{tr("Возраст", "Жасы", "Age")}</span><b>30.07.2014 (<span data-age>12</span> лет)</b></div>
      <div><span>{tr("Рост", "Бойы", "Height")}</span><b>{info['height']} см</b></div>
      <div><span>{tr("Город", "Қала", "Location")}</span><b>{info['city_ru']}</b></div>
      <div><span>{tr("Цвет глаз / волос", "Көз / шаш түсі", "Eyes / Hair")}</span><b>{tr("Карие / Тёмно-каштановые", "Қоңыр / Қарақоңыр", "Brown / Dark Brown")}</b></div>
      <div><span>{tr("Языки", "Тілдер", "Languages")}</span><b>{info['languages_ru']}</b></div>
      <div><span>{tr("Музыкальные инструменты", "Аспаптар", "Instruments")}</span><b>{info['instruments_ru']}</b></div>
    </div>
  </section>

  <section class="res-sec reveal">
    {tr("Кино и телевидение (Избранные роли)", "Кино және телевизия (Таңдаулы рөлдер)", "Television & Narrative Film (Selected)", "h2")}
    <div class="credits">
      {cred_row("«Было дело» (70-е годы) · серия «Холодное блюдо»",
                "«Было дело» (70-жылдар) · «Холодное блюдо» бөлімі",
                "“Bylo Delo” (1970s Period Detective) · “Cold Dish”",
                "Роль: Дочь убитой (сквозная драматическая роль)",
                "Рөлі: Қайтыс болған әйелдің қызы (драмалық рөл)",
                "Role: Victim's Daughter (Supporting Dramatic Role)")}
      {cred_row("«Сыныптас» (Молодёжный телесериал)",
                "«Сыныптас» (Жастар телехикаясы)",
                "“Synyptas” (Youth TV Series)",
                "Роль в сериале / школьный ансамбль",
                "Хикаядағы рөл / мектеп ансамблі",
                "Role in TV Series / School Ensemble")}
      {cred_row("«Было дело» (Второй эпизод)",
                "«Было дело» (Екінші үзінді)",
                "“Bylo Delo” (Episode 2)",
                "Драматическая игровая сцена",
                "Драмалық ойын сахнасы",
                "Dramatic Screen Appearance")}
    </div>
  </section>

  <section class="res-sec reveal">
    {tr("Кинопроекты и сериалы (Групповые сцены и съёмки — 17 проектов)",
        "Киножобалар мен хикаялар (Көпшілік сахналар — 17 жоба)",
        "Additional Television & Film Appearances (17 Productions)", "h2")}
    <div class="credits">
      {''.join(mass_rows)}
    </div>
  </section>

  <section class="res-sec reveal">
    {tr("Реклама и коммерческие видеопроекты", "Жарнама және коммерциялық жобалар", "Commercials & Brand Campaigns", "h2")}
    <div class="credits">
      {cred_row("Чипсы «Хрум» (HROOM)", "«Хрум» (HROOM) чипстері", "HROOM Potato Chips",
                "Главная детская роль в рекламном ролике", "Жарнамалық роликтегі басты рөл", "Lead Child Role in Commercial")}
      {cred_row("«CENTRAL DENT CLINIC»", "«CENTRAL DENT CLINIC»", "Central Dent Clinic",
                "Главная роль (имиджевая реклама клиники)", "Басты рөл (клиника имидждік жарнамасы)", "Principal Role (Clinic Campaign)")}
      {cred_row("«Білімді бол» (Языковой центр)", "«Білімді бол» (Тіл орталығы)", "“Bilimdi Bol” Language Center",
                "Главная роль ученицы языкового центра", "Тіл орталығы оқушысының рөлі", "Lead Student Role in Commercial")}
      {cred_row("Гимназия · «Соңғы қоңырау»", "Гимназия · «Соңғы қоңырау»", "Gymnasium · “Last Bell”",
                "Имиджевый короткометражный видеоролик", "Имидждік бейнеролик", "Brand & School Narrative Video")}
      {cred_row("Ресторан «Tito Arcanum»", "«Tito Arcanum» мейрамханасы", "“Tito Arcanum” Restaurant",
                "Рекламная кампания семейного ресторана", "Мейрамхананың жарнамалық науқаны", "Commercial Campaign")}
      {cred_row("Анонс-реклама фильма «Карина» (Якутия)", "«Карина» фильмінің жарнама анонсы", "“Karina” Feature Promo (Yakutia)",
                "Промо-ролик (режиссёр Марианна Сиэгэн)", "Промо-ролик (режиссер Марианна Сиэгэн)", "Promo Commercial (dir. Marianna Siegen)")}
      {cred_row("«SHAM SCHOOL»", "«SHAM SCHOOL»", "“SHAM SCHOOL” Campaign",
                "Рекламный проект образовательной школы", "Білім беру мектебінің жарнамасы", "Educational Academy Commercial")}
      {cred_row("«Бота Мия»", "«Бота Мия»", "“Bota Miya” Commercial",
                "Рекламный ролик (роль в детстве)", "Жарнамалық ролик (балалық шақтағы рөл)", "Commercial Role (Childhood Character)")}
    </div>
  </section>

  <section class="res-sec reveal">
    {tr("Вокал, музыка и награды", "Вокал, музыка және марапаттар", "Vocals, Music & Awards", "h2")}
    <div class="credits">
      {cred_row("Гран-при и дипломы по вокалу", "Вокал бойынша Гран-при және дипломдар", "Vocal Grand Prix & Golden Diplomas",
                "Обладательница многочисленных дипломов, медалей и Гран-при республиканских и международных вокальных конкурсов",
                "Республикалық және халықаралық вокал байқауларының көптеген дипломдары, медальдары мен Гран-при иегері",
                "Winner of multiple Grand Prix trophies, medals and diplomas at national and international vocal festivals")}
      {cred_row("Инструментальное мастерство (4 инструмента)", "Аспаптық шеберлік (4 аспап)", "Multi-Instrumentalist Skills (4 Instruments)",
                "Домбыра, Фортепиано, Гитара, Укулеле",
                "Домбыра, Фортепиано, Гитара, Укулеле",
                "Dombra (Kazakh traditional lute), Upright Piano, Acoustic Guitar, Ukulele")}
      {cred_row("Сценическое мастерство и вокал", "Сахналық шеберлік және вокал", "Stage Craft & Live Vocals",
                "Эстрадный и традиционный народный вокал (живой звук)",
                "Эстрадалық және дәстүрлі халықтық вокал (жанды дауыс)",
                "Pop & traditional Kazakh repertoire with live stage performance")}
    </div>
  </section>

  <section class="res-sec reveal">
    {tr("Курсы, тренинги и навыки", "Курстар, тренингтер және дағдылар", "Training, Education & Special Skills", "h2")}
    <div class="credits">
      {cred_row("Профессиональная подготовка", "Кәсіби дайындық", "Professional Training",
                "Актёрское мастерство, Эстрадный вокал, Домбыра, Фортепиано, Английский язык, Математика",
                "Актерлік шеберлік, Эстрадалық вокал, Домбыра, Фортепиано, Ағылшын тілі, Математика",
                "Screen Acting, Vocal Technique, Dombra, Piano, English, Mathematics")}
      {cred_row("Творческие навыки и хобби", "Шығармашылық дағдылар", "Special Skills & Hobbies",
                "Пение, игра на домбыре, фортепиано, гитаре и укулеле, академический рисунок, оригами и поделки из бумаги, изучение иностранных языков",
                "Ән айту, домбыра, фортепиано, гитара және укулеледе ойнау, сурет салу, оригами және қағаздан қолөнер жасау, шет тілдерін үйрену",
                "Singing, Dombra, Piano, Guitar, Ukulele, Drawing & Painting, Origami & Paper Crafts, Foreign Languages")}
    </div>
  </section>
</main>
'''
write_page('resume.html', 'Резюме', 'resume', resume_body)

# ==================== 4. MEDIA.HTML ====================
media_cards_html = []
for v in videos_data:
    media_cards_html.append(f'''
      <div class="card reveal" data-c="{v['cat']}" data-video="{v['video_src']}">
        <div class="media-frame">
          <img src="{v['poster_src']}" alt="{html.escape(v['title_ru'])}" loading="lazy">
          <video src="{v['video_src']}" muted loop playsinline preload="none"></video>
          <div class="play-badge" aria-label="Play">
            <svg viewBox="0 0 24 24"><polygon points="8 5 19 12 8 19 8 5"/></svg>
          </div>
        </div>
        <div class="card-meta">
          {tr(v['tag_ru'], v['tag_kz'], v['tag_en'], "div", "card-tag")}
          {tr(v['title_ru'], v['title_kz'], v['title_en'], "p", "card-title")}
        </div>
      </div>''')

media_body = f'''
<main class="media-layout">
  <aside class="media-sidebar" data-filter-group>
    <button type="button" class="on" data-f="all" data-ru="Все видео ({len(videos_data)})" data-kz="Барлық бейне ({len(videos_data)})" data-en="All ({len(videos_data)})">Все видео ({len(videos_data)})</button>
    <button type="button" data-f="roles" data-ru="Кино и сериалы" data-kz="Кино және хикая" data-en="Theatrical / TV">Кино и сериалы</button>
    <button type="button" data-f="ads" data-ru="Реклама" data-kz="Жарнама" data-en="Commercial">Реклама</button>
    <button type="button" data-f="music" data-ru="Вокал и музыка" data-kz="Вокал және музыка" data-en="Music & Vocals">Вокал и музыка</button>
    <button type="button" data-f="backstage" data-ru="Визитка и съёмки" data-kz="Визитка және түсірілім" data-en="Showreel & Backstage">Визитка и съёмки</button>
  </aside>

  <div>
    <div class="cards" id="media-cards-grid">
      {''.join(media_cards_html)}
    </div>

    <div class="mass-strip reveal">
      {tr(f"Также в фильмографии (массовка и групповые сцены — {len(mass_projects)} проектов)",
          f"Фильмографиядағы басқа да киножобалар (көпшілік сахна — {len(mass_projects)} жоба)",
          f"Additional Film & Television Appearances ({len(mass_projects)} Productions)", "h3")}
      <div class="mass-tags">
        {''.join(f"<span>{m[0]}</span>" for m in mass_projects)}
      </div>
    </div>
  </div>
</main>

<div class="v-modal">
  <button class="v-close" aria-label="Закрыть">✕</button>
  <div class="v-box">
    <video controls playsinline></video>
    <div class="v-meta">
      <h3 class="v-title"></h3>
      <p class="v-sub"></p>
    </div>
  </div>
</div>
'''
write_page('media.html', 'Проекты', 'media', media_body)

# ==================== 5. GALLERY.HTML (ALL 90 AUTHENTIC PHOTOS + CATEGORIES + LIGHTBOX) ====================
gal_items_html = []
cat_counts = {'all': len(gallery_data), 'cinema': 0, 'portraits': 0, 'music': 0, 'redcarpet': 0, 'awards': 0}

for item in gallery_data:
    cat = item.get('cat', 'cinema')
    cat_counts[cat] = cat_counts.get(cat, 0) + 1
    w_cls = ' wide' if item.get('is_wide') else ''
    gal_items_html.append(f'''
      <div class="gal-item{w_cls} reveal" data-c="{cat}" data-id="{item['id']}">
        <img src="{item['src']}" alt="{html.escape(item['title_ru'])}" loading="lazy">
        <div class="gal-item-info">
          <div>
            {tr(item['title_ru'], item['title_kz'], item['title_en'], "h4")}
            {tr(item['desc_ru'], item['desc_kz'], item['desc_en'], "span")}
          </div>
        </div>
      </div>''')

gallery_body = f'''
<main class="gal-page">
  <div class="gal-top">
    <div>
      {tr("Фотогалерея", "Фотогалерея", "Photo Gallery", "h1")}
      {tr(f"Всего {len(gallery_data)} кадров со съёмок, премьер, концертов и студийных фотосессий",
          f"Түсірілім, тұсаукесер, концерт және фотосессиялардан барлығы {len(gallery_data)} кадр",
          f"Collection of {len(gallery_data)} photos from film sets, red carpets, concerts and studio sessions", "p", "gal-desc")}
    </div>
    <div class="gal-subnav" data-filter-group>
      <button type="button" class="on" data-f="all" data-ru="ВСЕ ФОТО ({len(gallery_data)})" data-kz="БАРЛЫҚ ФОТО ({len(gallery_data)})" data-en="ALL PHOTOS ({len(gallery_data)})">ВСЕ ФОТО ({len(gallery_data)})</button>
      <button type="button" data-f="cinema" data-ru="КИНО И СЪЁМКИ ({cat_counts['cinema']})" data-kz="КИНО ЖӘНЕ ТҮСІРІЛІМ ({cat_counts['cinema']})" data-en="ON SET & CINEMA ({cat_counts['cinema']})">КИНО И СЪЁМКИ ({cat_counts['cinema']})</button>
      <button type="button" data-f="portraits" data-ru="ПОРТРЕТЫ И ХЭДШОТЫ ({cat_counts['portraits']})" data-kz="ПОРТРЕТТЕР МЕН ХЭДШОТТАР ({cat_counts['portraits']})" data-en="PORTRAITS & HEADSHOTS ({cat_counts['portraits']})">ПОРТРЕТЫ И ХЭДШОТЫ ({cat_counts['portraits']})</button>
      <button type="button" data-f="music" data-ru="СЦЕНА И МУЗЫКА ({cat_counts['music']})" data-kz="САХНА ЖӘНЕ МУЗЫКА ({cat_counts['music']})" data-en="STAGE & MUSIC ({cat_counts['music']})">СЦЕНА И МУЗЫКА ({cat_counts['music']})</button>
      <button type="button" data-f="redcarpet" data-ru="ПРЕМЬЕРЫ И ФЕСТИВАЛИ ({cat_counts['redcarpet']})" data-kz="ТҰСАУКЕСЕР МЕН ФЕСТИВАЛЬ ({cat_counts['redcarpet']})" data-en="RED CARPET & EVENTS ({cat_counts['redcarpet']})">ПРЕМЬЕРЫ И ФЕСТИВАЛИ ({cat_counts['redcarpet']})</button>
      <button type="button" data-f="awards" data-ru="НАГРАДЫ И ДИПЛОМЫ ({cat_counts['awards']})" data-kz="МАРАПАТТАР МЕН ДИПЛОМДАР ({cat_counts['awards']})" data-en="AWARDS & TROPHIES ({cat_counts['awards']})">НАГРАДЫ И ДИПЛОМЫ ({cat_counts['awards']})</button>
    </div>
  </div>

  <div class="gal-grid" id="gallery-grid">
    {''.join(gal_items_html)}
  </div>
</main>

<div class="lb">
  <button class="lb-close" aria-label="Закрыть">✕</button>
  <button class="lb-prev" aria-label="Предыдущее фото">‹</button>
  <button class="lb-next" aria-label="Следующее фото">›</button>
  <div class="lb-counter"></div>
  <div class="lb-content">
    <img class="lb-img" src="" alt="Увеличенное фото">
    <div class="lb-caption">
      <h3></h3>
      <p></p>
    </div>
  </div>
</div>
'''
write_page('gallery.html', 'Галерея', 'gallery', gallery_body)

# ==================== 6. CONTACT.HTML ====================
contact_body = f'''
<main class="contact">
  {tr("Связаться с нами", "Бізбен байланысу", "Get in Touch", "h1")}
  {tr(
    "По вопросам кастингов, съёмок в кино, сериалах и рекламе, а также концертных выступлений Айару Абдолла:",
    "Айару Абдолланың кино, хикая, жарнама кастингтеріне және концерттік өнер көрсетулеріне қатысты сұрақтар бойынша:",
    "For inquiries regarding film, television and commercial castings, as well as live musical performances of Aiaru Abdolla:",
    "p"
  )}

  <div class="cc">
    <div>
      {tr("Актриса · Айару Абдолла", "Актриса · Айару Абдолла", "Actor · Aiaru Abdolla", "small")}
      <a class="phone" href="tel:{info['phone_aiaru'].replace(' ', '')}">{info['phone_aiaru']}</a>
      <a class="btn" href="https://wa.me/{info['phone_aiaru'].replace(' ', '').replace('+', '')}" target="_blank" rel="noopener"
         data-ru="Написать в WhatsApp" data-kz="WhatsApp-қа жазу" data-en="Message on WhatsApp">Написать в WhatsApp</a>
    </div>

    <div>
      {tr(info['mama_name_ru'], info['mama_name_kz'], info['mama_name_en'], "small")}
      <a class="phone" href="tel:{info['phone_mama'].replace(' ', '')}">{info['phone_mama']}</a>
      <a class="btn" href="https://wa.me/{info['phone_mama'].replace(' ', '').replace('+', '')}" target="_blank" rel="noopener"
         data-ru="Написать в WhatsApp" data-kz="WhatsApp-қа жазу" data-en="Message on WhatsApp">Написать в WhatsApp</a>
    </div>
  </div>

  <div style="display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin-top:24px;">
    <a class="btn" href="{info['instagram_url']}" target="_blank" rel="noopener">
      Instagram · @{info['instagram']}
    </a>
    <a class="btn" href="assets/Aiaru_Abdolla_Portfolio.pdf" download="Aiaru_Abdolla_Portfolio.pdf"
       data-ru="Скачать PDF Портфолио" data-kz="PDF Портфолионы жүктеу" data-en="Download PDF Portfolio">Скачать PDF Портфолио</a>
    <button type="button" class="btn" onclick="copyCastingProfile()"
       data-ru="Скопировать кастинг-анкету" data-kz="Сауалнаманы көшіру" data-en="Copy Casting Profile">Скопировать кастинг-анкету</button>
  </div>
</main>
'''
write_page('contact.html', 'Контакты', 'contact', contact_body)

print(f'Successfully built all 6 pages with {len(gallery_data)} gallery photos and {len(videos_data)} videos!')
