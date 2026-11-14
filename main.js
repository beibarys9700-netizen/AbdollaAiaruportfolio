const IG='https://www.instagram.com/superstar_aiaru/';
const ico={ig:'<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6"/></svg>',
wa:'<svg viewBox="0 0 24 24"><path d="M3 21l1.6-4.7A8.5 8.5 0 1 1 8 19.5z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.6-2-1-1 .8c-1-.4-2-1.4-2.4-2.4l.8-1-1-2z"/></svg>'};
const page=document.body.dataset.page;
const links=[['index.html','Главная','home'],['about.html','Обо мне','about'],['resume.html','Резюме','resume'],['media.html','Проекты','media'],['gallery.html','Галерея','gallery']];
const light=document.body.dataset.light==='1';
document.body.insertAdjacentHTML('afterbegin',`<header class="${light?'light':'solid'}"><a class="logo" href="index.html">Айару Абдолла</a><button class="burger" aria-label="menu">☰</button><nav>${links.map(l=>`<a href="${l[0]}" class="${l[2]===page?'on':''}">${l[1]}</a>`).join('')}<a href="${IG}" target="_blank" aria-label="Instagram">${ico.ig}</a><a href="https://wa.me/77784767899" target="_blank" aria-label="WhatsApp">${ico.wa}</a><a href="contact.html" class="btn-c">Контакты</a></nav></header>`);
document.body.insertAdjacentHTML('beforeend',`<footer><div class="soc"><a href="${IG}" target="_blank">${ico.ig}</a><a href="https://wa.me/77784767899" target="_blank">${ico.wa}</a></div>© ${new Date().getFullYear()} Айару Абдолла · Алматы, Казахстан</footer>`);
const b=document.querySelector('.burger'),n=document.querySelector('nav');
b.onclick=()=>{n.classList.toggle('open');b.textContent=n.classList.contains('open')?'✕':'☰'};
// age
const bd=new Date(2014,6,30),t=new Date();let age=t.getFullYear()-2014-((t.getMonth()<6||(t.getMonth()==6&&t.getDate()<30))?1:0);
document.querySelectorAll('[data-age]').forEach(e=>e.textContent=age);
// reveal
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(e=>io.observe(e));
// header solid on scroll for light header
// lightbox
const lb=document.querySelector('.lb');
if(lb){document.querySelectorAll('.gal img').forEach(i=>i.onclick=()=>{lb.querySelector('img').src=i.src;lb.classList.add('open')});lb.onclick=()=>lb.classList.remove('open');}
// filters
document.querySelectorAll('.filters button').forEach(btn=>btn.onclick=()=>{document.querySelectorAll('.filters button').forEach(x=>x.classList.remove('on'));btn.classList.add('on');const f=btn.dataset.f;document.querySelectorAll('.card').forEach(c=>c.classList.toggle('hide',f!=='all'&&c.dataset.c!==f))});

