import html

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

# Massovka & Feature/Series Appearances (17 projects)
mass_projects = [
    ("«Қыздың жолы жіңішке»", "Кино / Массовка", "Кино / Көпшілік сахна", "Feature / Background"),
    ("«Қайрат»", "Кино / Массовка", "Кино / Көпшілік сахна", "Feature / Background"),
    ("«Бір ауылдың баласындай»", "Кино / Массовка", "Кино / Көпшілік сахна", "Feature / Background"),
    ("«Рестарт»", "Сериал / Массовка", "Хикая / Көпшілік сахна", "Series / Background"),
    ("«Нурикамал»", "Полнометражный фильм", "Толықметражды фильм", "Feature Film"),
    ("«Көке»", "Сериал / Массовка", "Хикая / Көпшілік сахна", "TV Series"),
    ("«Сыныптас»", "Молодёжный сериал", "Жастар телехикаясы", "Youth TV Series"),
    ("«Менің папам Тигр»", "Полнометражная комедия", "Толықметражды комедия", "Feature Comedy"),
    ("«111»", "Сериал / Массовка", "Хикая / Көпшілік сахна", "TV Series"),
    ("«Тик-так»", "Кинопроект / Массовка", "Киножоба / Көпшілік сахна", "Film Project"),
    ("«Токсик»", "Сериал / Массовка", "Хикая / Көпшілік сахна", "TV Series"),
    ("«Гипноз»", "Кинопроект / Массовка", "Киножоба / Көпшілік сахна", "Film Project"),
    ("«Қазақ әлемі 2»", "Кино / Массовка", "Кино / Көпшілік сахна", "Feature Film"),
    ("«Алтын орда»", "Исторический проект", "Тарихи жоба", "Historical Drama"),
    ("«Стадион»", "Кинопроект / Массовка", "Киножоба / Көпшілік сахна", "Film Project"),
    ("«Қазақстан-Үнді-Корея»", "Международная дорама", "Халықаралық дорама", "Co-Production Drama"),
    ("«105»", "Сериал / Массовка", "Хикая / Көпшілік сахна", "TV Series"),
]

# ==================== 1. INDEX.HTML ====================
index_body = f'''
<section class="hero" style="background-image:url('assets/hero-wide.jpg');">
  <div class="hero-txt">
    {tr("Айару<br>Абдолла", "Айару<br>Абдолла", "Aiaru<br>Abdolla", "h1")}
    {tr("Актриса · Вокалистка · Алматы", "Актриса · Вокалист · Алматы", "Actor · Vocalist · Almaty", "p")}
    <div class="hero-actions">
      <a class="btn btn-gold" href="assets/Aiaru_Abdolla_Portfolio.pdf" download="Aiaru_Abdolla_Portfolio.pdf"
         data-ru="Скачать PDF Портфолио" data-kz="PDF Портфолионы жүктеу" data-en="Download PDF Portfolio">Скачать PDF Портфолио</a>
      <button type="button" class="btn" onclick="copyCastingProfile()"
         data-ru="Скопировать кастинг-анкету" data-kz="Сауалнаманы көшіру" data-en="Copy Casting Profile">Скопировать кастинг-анкету</button>
    </div>
  </div>
</section>

<section class="dark center tagline reveal">
  {tr("юная актриса и вокалистка из Алматы.", "Алматылық жас актриса және вокалист.", "almaty-based young actor & vocalist.", "h2")}
  <a class="btn" href="about.html" data-ru="познакомиться" data-kz="жақынырақ танысу" data-en="what's my deal">познакомиться</a>
</section>

<section class="dark">
  <div class="wrap block reveal">
    {tr("в кадре и на сцене", "кадрда және сахнада", "what's on", "h2")}
    <div class="row">
      <div class="row-img">
        <img src="assets/home_mian3.jpg" alt="Айару Абдолла с домбырой">
      </div>
      <div class="row-content">
        {tr("Талант, пластика и живые эмоции", "Дарын, пластика және шынайы эмоция", "Versatility, Music & Authentic Emotion", "h3")}
        {tr(
          "Айару — обладательница многочисленных дипломов, медалей и Гран-при по вокалу. Поёт, играет на домбыре, фортепиано, гитаре и укулеле. Свободно работает в кадре на казахском и русском языках, изучает английский язык.",
          "Айару — вокал бойынша көптеген дипломдар, медальдар мен Гран-при иегері. Ән айтады, домбыра, фортепиано, гитара және укулеледе ойнайды. Кадрда қазақ және орыс тілдерінде еркін жұмыс істейді, ағылшын тілін меңгеруде.",
          "Aiaru is a Grand Prix-winning vocalist and young screen actor based in Almaty. She sings and plays four instruments — dombra, piano, guitar, and ukulele — performing fluently in Kazakh and Russian while studying English.",
          "p"
        )}
        <a class="btn" href="media.html" data-ru="смотреть видео" data-kz="бейнелерді көру" data-en="watch videos">смотреть видео</a>
      </div>
    </div>
  </div>

  <div class="wrap block reveal">
    {tr("недавние работы", "соңғы жобалар", "recently", "h2")}
    <div class="row rev">
      <div class="row-img">
        <img src="assets/home_main.jpg" alt="Айару Абдолла в сценическом образе">
      </div>
      <div class="row-content">
        {tr("От драматического кино до рекламы", "Драмалық кинодан жарнамаға дейін", "From Dramatic Television to Commercials", "h3")}
        {tr(
          "Драматическая роль дочери убитой в ретро-сериале «Было дело» (70-е годы, серия «Холодное блюдо»), главные детские роли в рекламе «Хрум», «Central Dent Clinic», «Білімді бол», «Tito Arcanum», анонсе фильма «Карина» и 25+ проектах.",
          "«Было дело» (70-ші жылдар, «Холодное блюдо» бөлімі) ретро-хикаясындағы драмалық рөл, «Хрум», «Central Dent Clinic», «Білімді бол», «Tito Arcanum» жарнамаларындағы басты балалар рөлдері және 25-тен астам киножоба.",
          "Featured in the 1970s detective period series “Bylo Delo” (“Cold Dish” — role of the victim's daughter), alongside lead commercial campaigns for HROOM Chips, Central Dent Clinic, Bilimdi Bol, Tito Arcanum, and 25+ film & TV productions.",
          "p"
        )}
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
        <b>157</b>
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
        <img src="assets/p2.jpg" alt="Галерея">
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
      {tr(
        "Я юная актриса и певица из Алматы. Профессионально занимаюсь актёрским мастерством и вокалом, снимаюсь в художественном кино, телесериалах и рекламных роликах.",
        "Мен Алматы қаласының жас актрисасы және әншісімін. Актерлік шеберлік пен вокалмен кәсіби түрде айналысамын, көркем фильмдерге, телехикаяларға және жарнамалық роликтерге түсемін.",
        "I'm an Almaty-based young actor and vocalist. I train in acting and vocal performance, working across narrative film, television series, and national commercials.",
        "p"
      )}
      {tr(
        "Недавно я сыграла драматическую роль дочери убитой в историческом сериале «Было дело» (70-е годы, серия «Холодное блюдо»), а также главные детские роли в рекламе «Хрум», «Central Dent Clinic» и «Білімді бол».",
        "Жақында «Было дело» (70-ші жылдар, «Холодное блюдо» бөлімі) тарихи хикаясында драмалық рөлді, сондай-ақ «Хрум», «Central Dent Clinic» және «Білімді бол» жарнамаларында басты рөлдерді сомдадым.",
        "I recently played the dramatic supporting role of the victim's daughter in the 1970s period series “Bylo Delo” (“Cold Dish”), and starred in commercials for HROOM Chips, Central Dent Clinic, and Bilimdi Bol.",
        "p"
      )}
      {tr(
        "В свободное время я пою, играю на домбыре, фортепиано, гитаре и укулеле, рисую, создаю оригами из бумаги и изучаю иностранные языки. Буду рада новым интересным ролям и кинопроектам!",
        "Бос уақытымда ән айтамын, домбыра, фортепиано, гитара және укулеледе ойнаймын, сурет саламын, оригами жасаймын және шет тілдерін үйренемін. Жаңа қызықты рөлдер мен киножобаларға әрдайым ашықпын!",
        "In my spare time I sing, play dombra, piano, guitar, and ukulele, draw, fold origami, and study foreign languages. I'm always excited for challenging new roles on screen.",
        "p"
      )}

      <div class="facts">
        <div>
          {tr("Имя", "Аты-жөні", "Full Name")}
          {tr("Абдолла Айару", "Абдолла Айару", "Aiaru Abdolla")}
        </div>
        <div>
          {tr("Дата рождения", "Туған күні", "Date of Birth")}
          {tr("30 июля 2014 (<span data-age>12</span> лет)", "30 шілде 2014 (<span data-age>12</span> жас)", "July 30, 2014 (Age <span data-age>12</span>)")}
        </div>
        <div>
          {tr("Рост", "Бойы", "Height")}
          {tr("157 см", "157 см", "157 cm (5'2\")")}
        </div>
        <div>
          {tr("Город", "Қала", "Location")}
          {tr("Алматы, Казахстан", "Алматы, Қазақстан", "Almaty, Kazakhstan")}
        </div>
        <div>
          {tr("Языки", "Тілдер", "Languages")}
          {tr("Казахский (родной) · Русский (свободно) · Английский", "Қазақ тілі (ана тілі) · Орыс тілі (еркін) · Ағылшын тілі", "Kazakh (Native) · Russian (Fluent) · English")}
        </div>
        <div>
          {tr("Инструменты", "Музыкалық аспаптар", "Instruments")}
          {tr("Домбыра · Фортепиано · Гитара · Укулеле", "Домбыра · Фортепиано · Гитара · Укулеле", "Dombra · Piano · Guitar · Ukulele")}
        </div>
      </div>

      <div class="chips-group">
        {tr("Хобби и творчество", "Хобби және шығармашылық", "Hobbies & Interests", "h3")}
        {tr(
          "Пение (эстрадный и народный вокал) · Домбыра · Фортепиано · Гитара · Укулеле · Рисование · Рукоделие (поделки из бумаги, оригами) · Изучение иностранных языков",
          "Ән айту (эстрадалық және халықтық вокал) · Домбыра · Фортепиано · Гитара · Укулеле · Сурет салу · Қолөнер (қағаздан бұйымдар, оригами) · Шет тілдерін үйрену",
          "Singing (Pop & Traditional Vocals) · Dombra · Piano · Guitar · Ukulele · Drawing · Paper Crafts & Origami · Foreign Languages",
          "div", "dot-list"
        )}
      </div>

      <div class="chips-group">
        {tr("Курсы и обучение", "Курстар мен дайындық", "Training & Courses", "h3")}
        {tr(
          "Актёрское мастерство · Вокал · Домбыра · Фортепиано · Английский язык · Математика",
          "Актерлік шеберлік · Вокал · Домбыра · Фортепиано · Ағылшын тілі · Математика",
          "Acting Technique · Vocal Performance · Dombra · Piano · English Language · Mathematics",
          "div", "dot-list"
        )}
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
      <img class="about-img" src="assets/gallery/gal_emotions.jpg" style="aspect-ratio:1/1;" alt="Карта эмоций Айару">
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

ads_credits = [
    ("Реклама чипсов «Хрум» (HROOM) — видеоролик", "«Хрум» (HROOM) чипстерінің бейнежарнамасы", "“HROOM” Chips — TV & Digital Commercial", "Главная роль", "Басты рөл", "Principal"),
    ("Реклама клиники «CENTRAL DENT CLINIC»", "«CENTRAL DENT CLINIC» стоматология жарнамасы", "“CENTRAL DENT CLINIC” Dental Commercial", "Главная роль", "Басты рөл", "Lead Spokesperson"),
    ("Реклама центра «Білімді бол» (языки)", "«Білімді бол» оқу орталығының жарнамасы", "“Bilimdi Bol” Education Center Commercial", "Роль ученицы", "Оқушы рөлі", "Lead Student"),
    ("Реклама ресторана «Tito Arcanum»", "«Tito Arcanum» мейрамханасының жарнамасы", "“Tito Arcanum” Restaurant Commercial", "Реклама", "Жарнама", "Commercial"),
    ("Анонс-реклама фильма «Карина» (Якутия, реж. Марианна Сиэгэн)", "«Карина» фильмінің анонс-жарнамасы (Якутия, реж. М. Сиэгэн)", "“Karina” Feature Film Teaser (Yakutia, dir. Marianna Siegen)", "Анонс фильма", "Фильм анонсы", "Promo Teaser"),
    ("Реклама школы «SHAM SCHOOL»", "«SHAM SCHOOL» мектебінің жарнамасы", "“SHAM SCHOOL” Commercial", "Реклама", "Жарнама", "Commercial"),
    ("Реклама «Бота Мия» — в детстве (бала кезі)", "«Бота Мия» жарнамасы — бала кезі", "“Bota Miya” Commercial — Young Lead", "Роль в детстве", "Бала кезі", "Young Lead"),
]

resume_body = f'''
<main class="wrap res" style="max-width:880px;">
  <div class="res-top">
    <div>
      {tr("Резюме и фильмография", "Түйіндеме және фильмография", "Acting Resume & Credits", "h1")}
      {tr(
        "Абдолла Айару · 30.07.2014 (<span data-age>12</span> лет) · Рост 157 см · Алматы, Казахстан",
        "Абдолла Айару · 30.07.2014 (<span data-age>12</span> жас) · Бойы 157 см · Алматы, Қазақстан",
        "Aiaru Abdolla · DOB 30.07.2014 (Age <span data-age>12</span>) · Height 157 cm · Almaty, Kazakhstan",
        "p", "res-sub"
      )}
    </div>
    <div style="display:flex;gap:10px;flex-wrap:wrap;">
      <a class="btn" href="assets/Aiaru_Abdolla_Portfolio.pdf" download="Aiaru_Abdolla_Portfolio.pdf"
         data-ru="Скачать PDF Резюме" data-kz="PDF Түйіндемені жүктеу" data-en="Download PDF Resume">Скачать PDF Резюме</a>
      <button type="button" class="btn" onclick="copyCastingProfile()"
         data-ru="Скопировать анкету" data-kz="Сауалнаманы көшіру" data-en="Copy Profile">Скопировать анкету</button>
    </div>
  </div>

  <h3>
    {tr("Роли в кино и сериалах", "Кино және телехикаялардағы рөлдер", "Film & Television Roles")}
    {tr("Кино", "Кино", "Narrative", "small")}
  </h3>
  {cred_row(
    "<b>«Было дело» (70-е годы)</b> — Серия «Холодное блюдо» (телеканал КТК)",
    "<b>«Было дело» (70-ші жылдар)</b> — «Холодное блюдо» бөлімі (КТК арнасы)",
    "<b>“Bylo Delo” (1970s Period Series)</b> — Episode “Cold Dish” (KTK TV)",
    "Роль: дочь убитой", "Рөлі: қайтыс болған әйелдің қызы", "Supporting: Victim's Daughter"
  )}

  <h3>
    {tr("Реклама и коммерческие проекты", "Жарнама және коммерциялық жобалар", "Commercials & Promo")}
    {tr("Реклама", "Жарнама", "Commercial", "small")}
  </h3>
  {''.join(cred_row(f"<b>{a[0]}</b>", f"<b>{a[1]}</b>", f"<b>{a[2]}</b>", a[3], a[4], a[5]) for a in ads_credits)}

  <h3>
    {tr("Участие в кино и сериалах (массовка и эпизоды)", "Кино және телехикаялар (көпшілік сахна)", "Film & Series Appearances (Background / Ensemble)")}
    {tr("17 проектов", "17 жоба", "17 Credits", "small")}
  </h3>
  {''.join(cred_row(f"<b>{m[0]}</b>", f"<b>{m[0]}</b>", f"<b>{m[0]}</b>", m[1], m[2], m[3]) for m in mass_projects)}

  <h3>
    {tr("Вокальные достижения и награды", "Вокалдық жетістіктер мен марапаттар", "Vocal Awards & Honors")}
    {tr("Гран-при", "Гран-при", "Honors", "small")}
  </h3>
  {cred_row(
    "<b>Обладательница многочисленных кубков Гран-при, медалей и дипломов</b> по вокалу",
    "<b>Вокал бойынша көптеген Гран-при кубоктары, медальдар мен дипломдар иегері</b>",
    "<b>Multiple Grand Prix Trophy, Gold Medal & First-Degree Diploma Winner</b> in Vocal Competitions",
    "Вокал", "Вокал", "Grand Prix"
  )}

  <h3>
    {tr("Образование, инструменты и языки", "Білімі, аспаптар және тілдер", "Training, Instruments & Languages")}
    {tr("Навыки", "Дағдылар", "Skills", "small")}
  </h3>
  {cred_row(
    "<b>Музыкальные инструменты:</b> домбыра, фортепиано, гитара, укулеле",
    "<b>Музыкалық аспаптар:</b> домбыра, фортепиано, гитара, укулеле",
    "<b>Musical Instruments:</b> Dombra, Piano, Guitar, Ukulele",
    "Музыка", "Музыка", "Music"
  )}
  {cred_row(
    "<b>Языки:</b> казахский (родной), русский (свободно), английский (изучает)",
    "<b>Тілдер:</b> қазақ тілі (ана тілі), орыс тілі (еркін), ағылшын тілі",
    "<b>Languages:</b> Kazakh (Native), Russian (Fluent), English",
    "Языки", "Тілдер", "Languages"
  )}
  {cred_row(
    "<b>Курсы:</b> актёрское мастерство, вокал, домбыра, фортепиано, английский язык, математика",
    "<b>Курстар:</b> актерлік шеберлік, вокал, домбыра, фортепиано, ағылшын тілі, математика",
    "<b>Courses:</b> Acting Technique, Vocals, Dombra, Piano, English, Mathematics",
    "Обучение", "Оқу", "Training"
  )}
</main>
'''
write_page('resume.html', 'Резюме', 'resume', resume_body)

# ==================== 4. MEDIA.HTML (KATELYN SPARKS LEFT SIDEBAR + 3-COL GRID) ====================
# 20 unique, verified videos with exact RU / KZ / EN titles
videos_data = [
    # (vid_id, cat, tag_ru, tag_kz, tag_en, title_ru, title_kz, title_en)
    ('kholodnoe_1', 'roles',
     'Кино и сериалы', 'Кино және хикая', 'Theatrical / TV',
     '«Было дело» (70-е) · «Холодное блюдо» | Роль дочери убитой (эпизод 1)',
     '«Было дело» (70-ж.) · «Холодное блюдо» | Қайтыс болған әйелдің қызы (1-үзінді)',
     '“Bylo Delo” (1970s) · “Cold Dish” | Victim\'s Daughter (Scene 1)'),

    ('kholodnoe_2', 'roles',
     'Кино и сериалы', 'Кино және хикая', 'Theatrical / TV',
     '«Было дело» · «Холодное блюдо» | Драматическая сцена (эпизод 2)',
     '«Было дело» · «Холодное блюдо» | Драмалық сахна (2-үзінді)',
     '“Bylo Delo” · “Cold Dish” | Emotional Dramatic Scene (Scene 2)'),

    ('backstage_direct', 'roles',
     'Кино и сериалы', 'Кино және хикая', 'Theatrical / TV',
     'Молодёжный сериал | Игровая сцена на натуре',
     'Жастар хикаясы | Ашық алаңдағы ойын сахнасы',
     'Youth Series | Outdoor Ensemble Scene'),

    ('ad_hroom', 'ads',
     'Реклама', 'Жарнама', 'Commercial',
     'Чипсы «Хрум» (HROOM) | Главная роль в рекламном ролике',
     '«Хрум» (HROOM) чипстері | Жарнамадағы басты рөл',
     'HROOM Chips | Principal Commercial Role'),

    ('ad_centraldent', 'ads',
     'Реклама', 'Жарнама', 'Commercial',
     'Central Dent Clinic | Реклама стоматологической клиники',
     'Central Dent Clinic | Стоматологиялық клиника жарнамасы',
     'Central Dent Clinic | Dental Clinic Commercial'),

    ('ad_languages', 'ads',
     'Реклама', 'Жарнама', 'Commercial',
     '«Білімді бол» | Реклама языкового центра (роль ученицы)',
     '«Білімді бол» | Тіл орталығының жарнамасы (оқушы рөлі)',
     '“Bilimdi Bol” | Language Center Commercial'),

    ('ad_gimnaziya', 'ads',
     'Реклама', 'Жарнама', 'Commercial',
     'Гимназия · «Соңғы қоңырау» | Имиджевый видеоролик',
     'Гимназия · «Соңғы қоңырау» | Имидждік бейнеролик',
     'Gymnasium · “Last Bell” | Narrative Promo Short'),

    ('music_piano', 'music',
     'Вокал и музыка', 'Вокал және музыка', 'Music & Vocals',
     'Сольное выступление на сцене | Эстрадный вокал (живой звук)',
     'Сахнадағы жеке өнер көрсету | Эстрадалық вокал (жанды дауыс)',
     'Solo Stage Vocal Performance | Live Vocals'),

    ('music_vocal', 'music',
     'Вокал и музыка', 'Вокал және музыка', 'Music & Vocals',
     'Игра на фортепиано | Инструментальное исполнение',
     'Фортепианода ойнау | Аспаптық жеке орындау',
     'Piano Performance | Solo Upright Piano'),

    ('music_nature', 'music',
     'Вокал и музыка', 'Вокал және музыка', 'Music & Vocals',
     'Домбыра в юрте | Казахский национальный образ и инструмент',
     'Киіз үйдегі домбыра | Ұлттық образ және дәстүрлі өнер',
     'Dombra in Kazakh Yurt | Traditional Instrument & Costume'),

    ('music_dombra', 'music',
     'Вокал и музыка', 'Вокал және музыка', 'Music & Vocals',
     'Праздничный концерт «Наурыз мейрамы» | Вокал на большой сцене',
     '«Наурыз мейрамы» концерті | Үлкен сахнадағы ән',
     '“Nauryz Meiramy” Gala Concert | Stage Vocal Performance'),

    ('music_stage', 'music',
     'Вокал и музыка', 'Вокал және музыка', 'Music & Vocals',
     'Выступление вокального ансамбля | Открытая сцена',
     'Вокалдық ансамбльдің өнер көрсетуі | Ашық сахна',
     'Vocal Ensemble Performance | Open-Air Stage'),

    ('backstage_boat', 'music',
     'Вокал и музыка', 'Вокал және музыка', 'Music & Vocals',
     'Песня в парке у фонтана | Музыкальное видео',
     'Саябақтағы субұрқақ жанындағы ән | Музыкалық бейне',
     'Song by the Park Fountain | Outdoor Vocal Reel'),

    ('intro_card', 'backstage',
     'Визитка и бэкстейдж', 'Визитка және бэкстейдж', 'Showreel & Backstage',
     'Видеопрезентация | Художественный образ в лодке с цветами',
     'Бейнепрезентация | Гүлге толы қайықтағы көркем образ',
     'Video Presentation | Boat with Flowers on the Lake'),

    ('showreel_gown', 'backstage',
     'Визитка и бэкстейдж', 'Визитка және бэкстейдж', 'Showreel & Backstage',
     'Сценический образ в белом бальном платье | Предгорья Алматы',
     'Ақ бал көйлегіндегі сахналық образ | Алматы таулары',
     'White Ball Gown Portrait Reel | Almaty Foothills'),

    ('music_dombra_dress', 'backstage',
     'Визитка и бэкстейдж', 'Визитка және бэкстейдж', 'Showreel & Backstage',
     'Студийная съёмка с доберманом | Бэкстейдж фотосессии',
     'Доберманмен студиялық түсірілім | Фотосессия бэкстейджі',
     'Studio Shoot with Doberman | Behind the Scenes'),

    ('fashion_podium', 'backstage',
     'Визитка и бэкстейдж', 'Визитка және бэкстейдж', 'Showreel & Backstage',
     'Модный показ | Дефиле на красной ковровой дорожке',
     'Сән көрсетілімі | Қызыл кілемдегі подиум дефилесі',
     'Fashion Show | Red Carpet Runway Walk'),

    ('choreo_duet', 'backstage',
     'Визитка и бэкстейдж', 'Визитка және бэкстейдж', 'Showreel & Backstage',
     'Современная хореография | Танцевальный дуэт',
     'Заманауи хореография | Би дуэті',
     'Contemporary Street Choreography | Dance Duet'),

    ('award_medal', 'backstage',
     'Визитка и бэкстейдж', 'Визитка және бэкстейдж', 'Showreel & Backstage',
     'Торжественное награждение медалью | Конкурс вокала',
     'Медальмен салтанатты марапаттау | Вокал байқауы',
     'Award Ceremony | Vocal Competition Medal Presentation'),

    ('award_school', 'backstage',
     'Визитка и бэкстейдж', 'Визитка және бэкстейдж', 'Showreel & Backstage',
     'Вручение почётной грамоты и знака | Школьное награждение',
     'Құрмет грамотасы мен төсбелгі табыстау | Мектептегі марапат',
     'School Honor & Badge Presentation Ceremony'),
]

media_cards_html = []
for vid, cat, tag_ru, tag_kz, tag_en, t_ru, t_kz, t_en in videos_data:
    media_cards_html.append(f'''
      <div class="card reveal" data-c="{cat}" data-video="assets/videos/{vid}.mp4">
        <div class="media-frame">
          <img src="assets/posters/{vid}.jpg" alt="{html.escape(t_ru)}" loading="lazy">
          <video src="assets/videos/{vid}.mp4" muted loop playsinline preload="none"></video>
          <div class="play-badge" aria-label="Play">
            <svg viewBox="0 0 24 24"><polygon points="8 5 19 12 8 19 8 5"/></svg>
          </div>
        </div>
        <div class="card-meta">
          {tr(tag_ru, tag_kz, tag_en, "div", "card-tag")}
          {tr(t_ru, t_kz, t_en, "p", "card-title")}
        </div>
      </div>''')

media_body = f'''
<main class="media-layout">
  <aside class="media-sidebar" data-filter-group>
    <button type="button" class="on" data-f="all" data-ru="Все видео (20)" data-kz="Барлық бейне (20)" data-en="All (20)">Все видео (20)</button>
    <button type="button" data-f="roles" data-ru="Кино и сериалы" data-kz="Кино және хикая" data-en="Theatrical / TV">Кино и сериалы</button>
    <button type="button" data-f="ads" data-ru="Реклама" data-kz="Жарнама" data-en="Commercial">Реклама</button>
    <button type="button" data-f="music" data-ru="Вокал и музыка" data-kz="Вокал және музыка" data-en="Music & Vocals">Вокал и музыка</button>
    <button type="button" data-f="backstage" data-ru="Визитка и съёмки" data-kz="Визитка және түсірілім" data-en="Showreel & Backstage">Визитка и съёмки</button>
  </aside>

  <div>
    <div class="cards">
      {''.join(media_cards_html)}
    </div>

    <div class="mass-strip reveal">
      {tr("Также в фильмографии (массовка и групповые сцены — 17 проектов)", "Фильмографиядағы басқа да киножобалар (көпшілік сахна — 17 жоба)", "Additional Film & Television Appearances (17 Productions)", "h3")}
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

# ==================== 5. GALLERY.HTML (CURATED NON-REPEATING PHOTOS + WORKING FILTERS + LIGHTBOX) ====================
# 18 distinct, curated photos (no duplicates!)
gallery_data = [
    # (img_file, cat, is_wide, title_ru, title_kz, title_en, desc_ru, desc_kz, desc_en)
    ('assets/gallery/gal_port_white.jpg', 'portraits', False,
     'Студийный актёрский портрет', 'Студиялық актерлік портрет', 'Studio Acting Headshot',
     'Естественный образ · Хэдшот', 'Табиғи образ · Хэдшот', 'Natural Look · Headshot'),

    ('assets/gallery/gal_emotions.jpg', 'portraits', False,
     'Актёрская карта эмоций (9 состояний)', 'Актерлік эмоциялар картасы (9 күй)', 'Actor Emotion Grid (9 States)',
     'Мимика и эмоциональный диапазон', 'Мимика және эмоциялық диапазон', 'Facial Expression Range Test'),

    ('assets/gallery/gal_port_black.jpg', 'portraits', False,
     'Крупный план в чёрном', 'Қара киімдегі ірі план', 'Close-Up Studio Portrait',
     'Классический кастинг-портрет', 'Классикалық кастинг-портрет', 'Classic Casting Portrait'),

    ('assets/gallery/gal_boat_roses.jpg', 'portraits', False,
     'Художественная съёмка в лодке с цветами', 'Гүлге толы қайықтағы көркем түсірілім', 'Editorial Shoot in a Flower Boat',
     'Кинематографичный кадр на озере', 'Көл бетіндегі кинематографиялық кадр', 'Cinematic Lake Portrait'),

    ('assets/gallery/gal_leather.jpg', 'portraits', False,
     'Образ в кожаной куртке-косухе', 'Былғары күртешедегі заманауи образ', 'Modern Look in Leather Jacket',
     'Характерный подростковый типаж', 'Мінезді жасөспірім бейнесі', 'Contemporary Teen Character Look'),

    ('assets/gallery/gal_chanel_black.jpg', 'portraits', False,
     'Вечерний образ в чёрном платье', 'Қара көйлектегі кешкі образ', 'Evening Gown Studio Look',
     'Элегантная фотосессия в студии', 'Студиядағы сәнді фотосессия', 'Editorial Studio Fashion'),

    ('assets/gallery/gal_park_autumn.jpg', 'portraits', False,
     'Осенний портрет в парке', 'Саябақтағы күзгі портрет', 'Autumn Park Portrait',
     'Естественный дневной свет', 'Табиғи күндізгі жарық', 'Natural Daylight Portrait'),

    ('assets/gallery/gal_roses_bouquet.jpg', 'portraits', False,
     'Портрет с букетом роз', 'Раушан гүл шоғымен портрет', 'Portrait with Rose Bouquet',
     'Студийный портрет с улыбкой', 'Күлімсіреген студиялық портрет', 'Warm Smiling Studio Shot'),

    ('assets/gallery/gal_kazakh_red.jpg', 'kazakh', False,
     'Красный казахский камзол с орнаментом', 'Оюлы қызыл қазақ камзолы', 'Red Kazakh National Jacket',
     'Традиционный национальный образ', 'Дәстүрлі ұлттық образ', 'Traditional Kazakh Costume'),

    ('assets/gallery/gal_dombra_red.jpg', 'kazakh', False,
     'С домбырой в красном костюме', 'Қызыл ұлттық костюмде домбырамен', 'With Dombra in Red Costume',
     'Музыкальное исполнительское искусство', 'Музыкалық орындаушылық өнер', 'Traditional Dombra Performer'),

    ('assets/gallery/gal_kazakh_black.jpg', 'kazakh', False,
     'Чёрный стилизованный казахский наряд', 'Қара стилизациаланған ұлттық киім', 'Black Stylized Kazakh Costume',
     'Серебряный орнамент · Крупный план', 'Күміс ою-өрнек · Ірі план', 'Silver Ornament Close-Up'),

    ('assets/gallery/gal_dombra_black.jpg', 'kazakh', False,
     'С домбырой в чёрном наряде', 'Қара костюмде домбырамен', 'With Dombra in Black Costume',
     'Традиционный кюй и вокал', 'Дәстүрлі күй және вокал', 'Traditional Music & Vocals'),

    ('assets/gallery/gal_dance_arms.jpg', 'kazakh', False,
     'Пластика казахского танца', 'Қазақ биінің пластикасы', 'Kazakh Traditional Dance Pose',
     'Сценическое движение', 'Сахналық қозғалыс', 'Stage Movement & Grace'),

    ('assets/gallery/gal_pink_dress.jpg', 'kazakh', False,
     'Нежный национальный образ', 'Нәзік ұлттық көйлек', 'Pink Traditional Silk Dress',
     'Белое платье с малиновым камзолом', 'Ақ көйлек пен алқызыл камзол', 'Traditional Kazakh Attire'),

    ('assets/gallery/gal_clinic_doctor.jpg', 'backstage', False,
     'На съёмках в клинике с актёрами', 'Клиникадағы түсірілім алаңында', 'On Set with Cast & Doctor',
     'Бэкстейдж съёмочного процесса', 'Түсірілім барысынан кадр', 'Behind the Scenes on Location'),

    ('assets/gallery/gal_lead_actor.jpg', 'backstage', False,
     'На съёмочной площадке сериала', 'Телехикаяның түсірілім алаңында', 'On Set of TV Series',
     'Рабочий момент между дублями', 'Дубль арасындағы сәт', 'Between Takes on Set'),

    ('assets/gallery/gal_director.jpg', 'backstage', False,
     'За кулисами съёмок и концерта', 'Түсірілім мен концерт сахнасының артында', 'Backstage at Event & Shoot',
     'В сценическом костюме', 'Сахналық костюмде', 'Backstage Portrait'),

    ('assets/gallery/gal_trophies_2.jpg', 'awards', False,
     'Кубки Гран-при и медали Айару', 'Айарудың Гран-при кубоктары мен медальдары', 'Aiaru\'s Grand Prix Trophies & Medals',
     'Награды республиканских и международных вокальных конкурсов', 'Республикалық және халықаралық вокал байқауларының марапаттары', 'National & International Vocal Competition Awards'),
]

gal_items_html = []
for img_p, cat, is_wide, t_ru, t_kz, t_en, d_ru, d_kz, d_en in gallery_data:
    w_cls = ' wide' if is_wide else ''
    gal_items_html.append(f'''
      <div class="gal-item{w_cls} reveal" data-c="{cat}">
        <img src="{img_p}" alt="{html.escape(t_ru)}" loading="lazy">
        <div class="gal-item-info">
          <div>
            {tr(t_ru, t_kz, t_en, "h4")}
            {tr(d_ru, d_kz, d_en, "span")}
          </div>
        </div>
      </div>''')

gallery_body = f'''
<main class="gal-page">
  <div class="gal-top">
    {tr("Фотогалерея", "Фотогалерея", "Photo Gallery", "h1")}
    <div class="gal-subnav" data-filter-group>
      <button type="button" class="on" data-f="all" data-ru="ВСЕ ФОТО (18)" data-kz="БАРЛЫҚ ФОТО (18)" data-en="ALL PHOTOS (18)">ВСЕ ФОТО (18)</button>
      <button type="button" data-f="portraits" data-ru="ПОРТРЕТЫ И ХЭДШОТЫ" data-kz="ПОРТРЕТТЕР МЕН ХЭДШОТТАР" data-en="HEADSHOTS & PORTRAITS">ПОРТРЕТЫ И ХЭДШОТЫ</button>
      <button type="button" data-f="kazakh" data-ru="НАЦИОНАЛЬНЫЕ ОБРАЗЫ" data-kz="ҰЛТТЫҚ ОБРАЗДАР" data-en="NATIONAL COSTUME">НАЦИОНАЛЬНЫЕ ОБРАЗЫ</button>
      <button type="button" data-f="backstage" data-ru="СЪЁМКИ И БЭКСТЕЙДЖ" data-kz="ТҮСІРІЛІМ ЖӘНЕ БЭКСТЕЙДЖ" data-en="PRODUCTION SHOTS">СЪЁМКИ И БЭКСТЕЙДЖ</button>
      <button type="button" data-f="awards" data-ru="КУБКИ И НАГРАДЫ" data-kz="КУБОКТАР МЕН МАРАПАТТАР" data-en="TROPHIES & AWARDS">КУБКИ И НАГРАДЫ</button>
    </div>
  </div>

  <div class="gal-grid">
    {''.join(gal_items_html)}
  </div>
</main>

<div class="lb">
  <button class="lb-close" aria-label="Закрыть">✕</button>
  <button class="lb-nav lb-prev" aria-label="Предыдущее">❮</button>
  <button class="lb-nav lb-next" aria-label="Следующее">❯</button>
  <div class="lb-content">
    <div class="lb-counter"></div>
    <img class="lb-img" alt="Фото Айару Абдолла">
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
    "По вопросам кастингов, кинопроб, съёмок в рекламе и выступлений — звоните или пишите в WhatsApp.",
    "Кастинг, киносынама, жарнамаға түсу және өнер көрсету мәселелері бойынша қоңырау шалыңыз немесе WhatsApp-қа жазыңыз.",
    "For casting inquiries, auditions, commercial bookings, and performances — reach out via phone or WhatsApp.",
    "p"
  )}

  <div class="cc">
    <div>
      {tr("Айару Абдолла", "Айару Абдолла", "Aiaru Abdolla", "small")}
      <a class="phone" href="tel:+77784767899">+7 778 476 78 99</a>
      <a class="btn" href="https://wa.me/77784767899" target="_blank" rel="noopener"
         data-ru="Написать в WhatsApp" data-kz="WhatsApp-қа жазу" data-en="Message on WhatsApp">Написать в WhatsApp</a>
    </div>

    <div>
      {tr("Мама · Жанар (Представитель)", "Анасы · Жанар (Өкілі)", "Mother & Manager · Zhanar", "small")}
      <a class="phone" href="tel:+77057429700">+7 705 742 97 00</a>
      <a class="btn" href="https://wa.me/77057429700" target="_blank" rel="noopener"
         data-ru="Написать в WhatsApp" data-kz="WhatsApp-қа жазу" data-en="Message on WhatsApp">Написать в WhatsApp</a>
    </div>
  </div>

  <div style="display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin-top:24px;">
    <a class="btn" href="https://www.instagram.com/superstar_aiaru/" target="_blank" rel="noopener">
      Instagram · @superstar_aiaru
    </a>
    <a class="btn" href="assets/Aiaru_Abdolla_Portfolio.pdf" download="Aiaru_Abdolla_Portfolio.pdf"
       data-ru="Скачать PDF Портфолио" data-kz="PDF Портфолионы жүктеу" data-en="Download PDF Portfolio">Скачать PDF Портфолио</a>
    <button type="button" class="btn" onclick="copyCastingProfile()"
       data-ru="Скопировать кастинг-анкету" data-kz="Сауалнаманы көшіру" data-en="Copy Casting Profile">Скопировать кастинг-анкету</button>
  </div>
</main>
'''
write_page('contact.html', 'Контакты', 'contact', contact_body)

print('Built all 6 pages with RU/KZ/EN and PDF support!')
