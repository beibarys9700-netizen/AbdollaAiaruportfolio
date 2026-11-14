import html
HEAD='''<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{t} — Айару Абдолла</title><meta name="description" content="Айару Абдолла — юная актриса и вокалистка из Алматы. Портфолио, резюме, проекты."><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="style.css"></head><body data-page="{p}" data-light="{l}">'''
TAIL='<script src="main.js"></script></body></html>'
def w(name,t,p,body,l=0):
    open(name,'w',encoding='utf-8').write(HEAD.format(t=t,p=p,l=l)+body+TAIL)

mass=["Қыздың жолы жіңішке","Қайрат","Бір ауылдың баласындай","Рестарт","Нурикамал","Көке","Сыныптас (молодёжный сериал)","Менің папам Тигр","111","Тик-так","Токсик","Гипноз","Қазақ әлемі 2","Алтын орда","Стадион","Қазақстан-Үнді-Корея (дорама)","105"]
roles=[("Было дело (70-е годы) · «Холодное блюдо»","Роль: дочь убитой","Роль")]
ads=[("Tito Arcanum","Реклама ресторана"),("Карина","Анонс фильма · Якутия · реж. Марианна Сиэгэн"),("Білімді бол","Реклама"),("Хрум","Реклама чипсов"),("CENTRAL DENT CLINIC","Реклама"),("SHAM SCHOOL","Реклама"),("Бота Мия","Реклама · в детстве (бала кезі)")]

# HOME
body='''<section class="hero" style="background-image:url(assets/hero-wide.jpg)"><div class="hero-txt"><h1>Айару<br>Абдолла</h1><p>Актриса · Вокалистка · Алматы</p></div></section>
<section class="dark center tagline reveal"><h2>юная актриса из Алматы</h2><a class="btn" href="about.html">познакомиться</a></section>
<section class="dark"><div class="wrap block reveal"><h2>что нового</h2><div class="row"><img src="assets/p3.jpg" style="object-position:center 30%" alt=""><div><p>Айару — обладательница многочисленных дипломов, медалей и гран-при по вокалу. Снимается в кино, сериалах и рекламе Казахстана.</p><a class="btn" href="resume.html">смотреть резюме</a></div></div></div>
<div class="wrap block reveal"><h2>недавно</h2><div class="row rev"><img src="assets/p0.jpg" style="object-position:center 35%" alt=""><div><p>Роль дочери в проекте «Было дело» («Холодное блюдо»), реклама Tito Arcanum, «Хрум», Central Dent Clinic, анонс фильма «Карина» (Якутия) и многое другое.</p><a class="btn" href="media.html">проекты</a></div></div></div>
<div class="wrap" style="max-width:1000px"><div class="stats reveal"><div><b data-age>11</b><small>лет</small></div><div><b>157</b><small>см рост</small></div><div><b>25+</b><small>проектов</small></div><div><b>6</b><small>направлений обучения</small></div></div></div>
<div class="wrap block reveal" style="max-width:1000px"><h2>ещё больше</h2><div class="three"><a class="tile" href="resume.html"><img src="assets/p1.jpg" alt=""><span>резюме</span></a><a class="tile" href="media.html"><img src="assets/p5.jpg" style="object-position:center 20%" alt=""><span>проекты</span></a><a class="tile" href="gallery.html"><img src="assets/p4.jpg" alt=""><span>галерея</span></a></div></div>
<div class="center block reveal"><h2 style="font-size:30px;margin-bottom:22px">связаться</h2><a class="btn" href="contact.html">контакты</a></div></section>'''
w('index.html','Главная','home',body,0)

# ABOUT
body='''<main class="wrap" style="max-width:1000px"><div class="about"><div class="reveal"><h1>Привет! Я Айару.</h1>
<p>Мне <b data-age>11</b> лет, я живу в Алматы. Я пою, играю на домбре и фортепиано, снимаюсь в кино, сериалах и рекламе.</p>
<p>Я обладательница многочисленных дипломов, медалей и гран-при по вокалу. Мне нравится выходить на сцену и перед камеру, а ещё — узнавать новое: учу языки, рисую и делаю оригами.</p>
<div class="facts"><div><span>Имя</span><span>Абдолла Айару</span></div><div><span>Дата рождения</span><span>30 июля 2014</span></div><div><span>Рост</span><span>157 см</span></div><div><span>Город</span><span>Алматы, Казахстан</span></div><div><span>Театр</span><span>не выступала</span></div></div>
<h3 style="margin-top:34px;font-size:22px">Хобби</h3><ul class="chips"><li>Пение</li><li>Домбыра</li><li>Фортепиано</li><li>Рисование</li><li>Поделки из бумаги</li><li>Оригами</li><li>Иностранные языки</li></ul>
<h3 style="margin-top:30px;font-size:22px">Курсы</h3><ul class="chips"><li>Вокал</li><li>Домбыра</li><li>Фортепиано</li><li>Английский язык</li><li>Математика</li><li>Актёрское мастерство</li></ul></div>
<img class="reveal" src="assets/p2.jpg" alt="Айару Абдолла"></div></main>'''
w('about.html','Обо мне','about',body)

# RESUME
def cr(n,d,k): return f'<div class="credit"><span><b>{html.escape(n)}</b> — {html.escape(d)}</span><em>{k}</em></div>' if d else f'<div class="credit"><span><b>{html.escape(n)}</b></span><em>{k}</em></div>'
r='<main class="wrap res" style="max-width:820px;padding-bottom:90px"><h1>Резюме</h1><p>Абдолла Айару · 30.07.2014 · рост 157 см · Алматы</p>'
r+='<h3>Роли</h3>'+''.join(cr(a,b,c) for a,b,c in [("Было дело (70-е годы)","«Холодное блюдо» — дочь убитой","Сериал")])
r+='<h3>Реклама</h3>'+''.join(cr(a,b,"Реклама") for a,b in ads)
r+='<h3>Массовка</h3>'+''.join(cr(a,"","Массовка") for a in mass)
r+='<h3>Достижения</h3>'+cr("Многочисленные дипломы, медали и гран-при","вокал","Музыка")
r+='<h3>Навыки</h3>'+cr("Вокал, домбыра, фортепиано","","Музыка")+cr("Английский язык","изучение иностранных языков","Языки")+cr("Актёрское мастерство","курс","Обучение")+cr("Рисование, оригами, поделки из бумаги","","Творчество")
r+='<p style="margin-top:36px"><a class="btn" href="contact.html">пригласить на пробы</a></p></main>'
w('resume.html','Резюме','resume',r)

# MEDIA
cards=[]
imgs=['p0','p1','p2','p3','p4','p5']
i=0
def card(n,sub,cat,label):
    global i
    im=imgs[i%6];i+=1
    cards.append(f'<a class="card reveal" data-c="{cat}" href="contact.html"><div class="th"><img src="assets/{im}.jpg" alt=""><b>{html.escape(n)}</b></div><small>{label}</small><p>{html.escape(sub)}</p></a>')
card("Было дело · Холодное блюдо","Дочь убитой · 70-е годы","roles","Роль")
for a,b in ads: card(a,b,"ads","Реклама")
for a in mass: card(a,"Массовка","mass","Массовка")
m='<main class="media"><div class="filters"><button class="on" data-f="all">Все</button><button data-f="roles">Роли</button><button data-f="ads">Реклама</button><button data-f="mass">Массовка</button></div><div class="cards">'+''.join(cards)+'</div></main>'
w('media.html','Проекты','media',m)

# GALLERY
g='<div class="gal">'+''.join(f'<img src="assets/{p}.jpg" alt="Айару Абдолла" loading="lazy">' for p in ['p2','p0','p5','p3','p1','p4'])+'</div><div class="lb"><img alt=""></div>'
w('gallery.html','Галерея','gallery',g)

# CONTACT
c='''<main class="contact"><h1>Связаться</h1><p>По вопросам съёмок, проб и сотрудничества — звоните или пишите.</p>
<div class="cc"><div><small>Айару</small><a href="tel:+77784767899">+7 778 476 78 99</a><a class="btn" href="https://wa.me/77784767899" target="_blank">WhatsApp</a></div><div><small>Мама · Жанар</small><a href="tel:+77057429700">+7 705 742 97 00</a><a class="btn" href="https://wa.me/77057429700" target="_blank">WhatsApp</a></div></div>
<a class="btn" href="https://www.instagram.com/superstar_aiaru/" target="_blank">Instagram · @superstar_aiaru</a></main>'''
w('contact.html','Контакты','contact',c)
