import os, subprocess, time
import imageio_ffmpeg
from PIL import Image

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
base_dir = r'd:\portfolios for kids\Aiaru portfolio'
assets_dir = os.path.join(base_dir, 'assets')
videos_dir = os.path.join(assets_dir, 'videos')
posters_dir = os.path.join(assets_dir, 'posters')
gallery_dir = os.path.join(assets_dir, 'gallery')

os.makedirs(videos_dir, exist_ok=True)
os.makedirs(posters_dir, exist_ok=True)
os.makedirs(gallery_dir, exist_ok=True)

# List of videos with metadata:
# (id, source_path, title, subtitle, category, poster_ss)
videos = [
    ('intro_card', r'D:\загрузки\aiaru photos\видео презентация.mp4', 'Видеовизитка', 'Актёрская самопрезентация Айару', 'roles', '00:00:02'),
    ('kholodnoe_1', r'D:\загрузки\aiaru photos\роль Было дело (70-е годы) — «Холодное блюдо» — дочь убитой.mp4', '«Было дело» · 70-е годы', '«Холодное блюдо» — роль дочери убитой', 'roles', '00:00:03'),
    ('kholodnoe_2', r'D:\загрузки\aiaru photos\роль Было дело (70-е годы) — «Холодное блюдо» 2 видео — дочь убитой.mp4', '«Было дело» · Сцена в отделе', 'Драматический эпизод · Роль', 'roles', '00:00:02'),
    ('ad_hroom', r'D:\загрузки\aiaru photos\реклама HROOM .mp4', 'Реклама чипсов «Хрум»', 'Главная детская роль в рекламе', 'ads', '00:00:01'),
    ('ad_languages', r'D:\загрузки\aiaru photos\реклама языки.mp4', 'Реклама «Білімді бол»', 'Образовательный центр · Роль ученицы', 'ads', '00:00:02'),
    ('ad_centraldent', r'D:\загрузки\aiaru photos\реклама central dent.mp4', 'Реклама «Central Dent Clinic»', 'Стоматологическая клиника · Имиджевый ролик', 'ads', '00:00:02'),
    ('music_piano', r'D:\загрузки\i3ysgikdtdf66xw6t800.mp4', 'Фортепиано и вокал', 'Живое исполнение на фортепиано', 'music', '00:00:05'),
    ('music_dombra', r'D:\загрузки\odbssyr4342y41a6ty6u.mp4', 'Игра на домбыре', 'Традиционный казахский кюй · Домбыра', 'music', '00:00:03'),
    ('music_vocal', r'D:\загрузки\AQOAmJTa6WyKB_DTeMB2YisQ0alyy3SsFOJ4RREy_tVNrOHJdU16Lg_45llg2yI.mp4', 'Вокал · Живой звук', 'Сольное вокальное выступление', 'music', '00:00:04'),
    ('music_stage', r'D:\загрузки\iyoDkZEdJlT2npBOA96W.mp4', 'Выступление на большой сцене', 'Концертное сольное выступление', 'music', '00:00:10'),
    ('music_white_dress', r'D:\загрузки\aiaru photos\WhatsApp Video 2026-11-14 at 23.00.59.mp4', 'Вокал в горах', 'Выступление в бальном платье', 'music', '00:00:03'),
    ('music_dombra_dress', r'D:\загрузки\aiaru photos\WhatsApp Video 2026-11-14 at 23.44.09.mp4', 'Домбыра в национальном костюме', 'Народная музыка · Домбыра', 'music', '00:00:02'),
    ('music_nature', r'D:\загрузки\aiaru photos\WhatsApp Video 2026-11-14 at 23.32.37.mp4', 'Песня на природе', 'Музыкальный номер на открытом воздухе', 'music', '00:00:02'),
    ('backstage_boat', r'D:\загрузки\aiaru photos\WhatsApp Video 2026-11-14 at 23.22.39.mp4', 'Съёмки в лодке с розами', 'Кинематографичный бэкстейдж съёмок', 'backstage', '00:00:02'),
    ('backstage_direct', r'D:\загрузки\AQOta_E4oiXlKbZQ2_H3ztET271nc1V3aK5GeKk8_uUyQ0hJPYM7_eK8cW_Kb7l.mp4', 'Работа с режиссёром', 'Репетиция сцены перед дублем', 'backstage', '00:00:02'),
    ('choreo_duet', r'D:\загрузки\AQOWUY_QESoGNqZEl4BRBRDBqd_D6kSDuP9NEGZymCW7r4oZ1iZVZmZyERLdCaq.mp4', 'Хореография (дуэт)', 'Современный танец · Пластика', 'backstage', '00:00:02'),
    ('fashion_podium', r'D:\загрузки\AQPbRBDKSmCR9y0P9wksLKFcg4hZXEJfzZrSSDUMtJ6KiP_0aI1VSC4a95I53o4.mp4', 'Модный показ · Красная дорожка', 'Дефиле и подиумное выступление', 'backstage', '00:00:02'),
    ('award_ceremony', r'D:\загрузки\AQMc_v_S8XREB4WWCSX2zCktQRGJOkBmKJebxMl7rPfDntQHyeQ_5yEPLaZH6QkmbthO6fmq.mp4', 'Церемония награждения', 'Вручение диплома победителя', 'backstage', '00:00:02'),
    ('award_medal', r'D:\загрузки\AQOU1PprPi_HXfPNhYkWN4y1pwsE_sPJga2O7ScKh54OZo3kGoyHMNUA4r6J5w1.mp4', 'Награждение медалью', 'Победа на конкурсе вокала', 'backstage', '00:00:02'),
]

print(f'Starting processing {len(videos)} videos...')
for vid, src, title, sub, cat, ss in videos:
    v_out = os.path.join(videos_dir, f'{vid}.mp4')
    p_out = os.path.join(posters_dir, f'{vid}.jpg')
    
    # 1. Poster
    if not os.path.exists(p_out):
        cmd_p = [ffmpeg_exe, '-y', '-ss', ss, '-i', src, '-frames:v', '1', '-q:v', '2', p_out]
        subprocess.run(cmd_p, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # 2. Web-optimized MP4 (scale to 720p or 540p, faststart, crf 27)
    if not os.path.exists(v_out) or os.path.getsize(v_out) == 0:
        # scale so max dimension is 720 or 540
        vf = "scale='if(gt(iw,ih),min(iw,720),-2)':'if(gt(iw,ih),-2,min(ih,720))'"
        cmd_v = [
            ffmpeg_exe, '-y', '-i', src,
            '-vf', vf,
            '-c:v', 'libx264', '-crf', '27', '-preset', 'faster',
            '-c:a', 'aac', '-b:a', '96k',
            '-movflags', '+faststart',
            v_out
        ]
        t0 = time.time()
        subprocess.run(cmd_v, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sz = os.path.getsize(v_out)/(1024*1024) if os.path.exists(v_out) else 0
        print(f'Encoded {vid}: {sz:.2f} MB ({time.time()-t0:.1f}s)')

print('Videos processed!')

# Now gallery photos
# (id, src, title, category)
gallery_photos = [
    ('gal_emotions', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 22.05.10.jpeg', 'Актёрский тест эмоций (9 состояний)', 'portraits'),
    ('gal_trophies_1', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 22.16.46.jpeg', 'Кубки Гран-при и награды по вокалу', 'awards'),
    ('gal_trophies_2', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 22.55.07 (1).jpeg', 'Награды и медали республиканских и международных конкурсов', 'awards'),
    ('gal_boat_roses', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 21.05.50.jpeg', 'Художественная съёмка на озере в лодке с розами', 'portraits'),
    ('gal_port_white', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 21.05.50 (2).jpeg', 'Актёрский портрет в студии', 'portraits'),
    ('gal_leather', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 21.05.50 (3).jpeg', 'Образ в кожаной куртке-косухе', 'portraits'),
    ('gal_chanel_black', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 21.05.50 (4).jpeg', 'Вечерний образ в чёрном платье', 'portraits'),
    ('gal_park_autumn', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 21.05.50 (5).jpeg', 'Осенняя съёмка в парке', 'portraits'),
    ('gal_port_black', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 21.05.51 (1).jpeg', 'Крупный план · Студия', 'portraits'),
    ('gal_roses_bouquet', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 21.05.51.jpeg', 'Портрет с букетом роз', 'portraits'),
    ('gal_kazakh_red', r'D:\загрузки\aiaru photos\main 2 .jpeg', 'Национальный казахский костюм · Красный камзол', 'kazakh'),
    ('gal_kazakh_black', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 22.03.36.jpeg', 'Казахский стилизованный наряд с орнаментом', 'kazakh'),
    ('gal_dombra_red', r'D:\загрузки\aiaru photos\mian  3.jpeg', 'С домбырой в традиционном образе', 'kazakh'),
    ('gal_dombra_black', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 22.03.36 (1).jpeg', 'Домбыра и сценический наряд', 'kazakh'),
    ('gal_dance_arms', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 22.03.36 (11).jpeg', 'Элемент казахского танца', 'kazakh'),
    ('gal_full_height', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 22.03.36 (10).jpeg', 'Полный рост · Сценический образ', 'kazakh'),
    ('gal_clinic_doctor', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 22.04.59.jpeg', 'На съёмках сериала с врачом-актёром', 'backstage'),
    ('gal_clinic_gown', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 22.03.37.jpeg', 'На съёмочной площадке в клинике', 'backstage'),
    ('gal_lead_actor', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 22.05.33.jpeg', 'С коллегой по съёмочной площадке', 'backstage'),
    ('gal_director', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 22.13.47.jpeg', 'На съёмках с режиссёром проекта', 'backstage'),
    ('gal_pink_dress', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 21.05.50 (1).jpeg', 'В национальном шёлковом платье', 'kazakh'),
    ('gal_white_sport', r'D:\загрузки\aiaru photos\WhatsApp Image 2026-11-14 at 17.32.35.jpeg', 'Спортивный образ', 'portraits'),
]

print(f'Processing {len(gallery_photos)} gallery photos...')
for gid, src, title, cat in gallery_photos:
    g_out = os.path.join(gallery_dir, f'{gid}.jpg')
    if not os.path.exists(g_out):
        im = Image.open(src).convert('RGB')
        # resize nicely to max dimension 1600 if larger
        max_dim = 1600
        if max(im.width, im.height) > max_dim:
            im.thumbnail((max_dim, max_dim), Image.LANCZOS)
        im.save(g_out, quality=88)

print('Gallery photos processed!')
