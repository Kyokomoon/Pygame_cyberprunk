import pygame
import math
from random import random, randrange, randint
from gui_Inventory import run
from gui_skils import run_skill
pygame.init() 
def load(ANSWER, ANSWER_2, hero_type, root):
    global save_inf
    root.destroy()                              #Уничтожение окна запуска
    WHITE = (255, 255, 255)                     #Базовые цвета
    RED = (225, 0, 50)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 225)
    W = 960                                     #Ширина окна
    H = 624                                     #Высота окна
    sc = pygame.display.set_mode((W, H))
    road = pygame.image.load('road1.png')       #Загрузка карты
    road_rect = road.get_rect(bottomright=(960,624))
    sc.fill(WHITE)                              #Заполнение белым
    pygame.display.update()
    skil_activ = 0                              #Необхоим для работы скилла
    shoot_chek = 0                              #Необхоим для работы скилла
    skil_2_activ = 0                            #Необхоим для работы скилла
    skil_3_activ = 0                            #Необхоим для работы скилла
    Font1 = pygame.font.Font(None, 30)
    Font2 = pygame.font.Font(None, 100)
    SPRITE=("play.png", "Continue.png", "Exit1.png", "hero_stand.png", "hero_left.png", "hero_down.png", "hero_right.png", "Skils.png", "Inventory.png", "Stena_1.png", "Stena_2.png","house_orange_long.png", "house_orange_short.png","house_orange_big.png","house_orange_big_2.png","house_red_short.png", "house_red_big.png","Roaps.png","Object.png", "Shoot_2.png", "hole.png", "Enemy_down.png", "Enemy_down_rare.png","Enemy_down_mimi_bos.png","Enemy_down_bos.png")
    SPRITE_SURF = []
    inventory = []
    skils_1 = [] #Список скилов громилы
    skils_2 = [] #Список скилов хакера
    skils_3 = [] #Список скилов механика
    need_p_1 = [] #Необходимые очки для изучения для 1 класса
    need_i_1 = []
    need_s_1 = []
    need_p_2 = [] #Необходимые очки для изучения для 2 класса
    need_i_2 = []
    need_s_2 = []
    need_p_3 = [] #Необходимые очки для изучения для 3 класса
    need_i_3 = []
    need_s_3 = []
    text1 = '1 скилл: Не изучен'
    text2 = '2 скилл: Не изучен'
    text3 = '3 скилл: Не изучен'
    Dead_text = " "
    Dead_text2 = " "
    Dead2 = Font2.render(Dead_text2, 1, (225, 0, 50))
    Dead = Font2.render(Dead_text, 1, (225, 0, 50))
    text_skil_1 = Font1.render(text1, 1, (255, 255, 255))
    text_skil_2 = Font1.render(text2, 1, (255, 255, 255))
    text_skil_3 = Font1.render(text3, 1, (255, 255, 255))
    random_sp_x = ((690, 810),(378, 552),(767, 818),(85, 587))
    random_sp_y = ((480, 527),(188, 227),(164, 218),(525, 605))
    hand = []       #Вещи в руках
    lernd_skill = [] #Изученные скиллы
    skil_lern = [] 
    LEVEL = ((0, 0, 0),(1, 100, 2), (2, 200, 2), (3, 400, 1), (4, 700, 2), (5, 1100, 2), (6, 1600, 2), (7, 2200, 3), (8, 2900, 3), (9, 3600, 2), (10, 4100, 4),(11, 4900, 4),(12, 6000, 4),(13, 6500, 4),(14, 7000, 4),(15, 100000, 4))
    CHARACTERS = ('', 'sila','intelekt', 'protect')
    for i in range(len(SPRITE)):
        SPRITE_SURF.append(pygame.image.load(SPRITE[i]).convert_alpha())
    class Hero(pygame.sprite.Sprite):
        def __init__(self ,Name, Surname, lvl, sila, intelekt, protect, hp, st, sheld, reg_hp, reg_st, reg_sheld,surf, x, y, group, ids): #Общий родительский класс
            pygame.sprite.Sprite.__init__(self)
            self.lvl = lvl                      #Уровень
            self.Name = Name
            self.Surname = Surname
            self.expirience_point = 5           #Очки изучения 
            self.exp = 0                        #Опыт
            self.sila = sila
            self.intelekt = intelekt
            self.protect = protect
            self.hp = hp
            self.st = st
            self.sheld = sheld
            self.reg_hp = reg_hp                #Первоначальные характеристики
            self.reg_st = reg_st
            self.reg_sheld = reg_sheld
            self.lernd_skill = lernd_skill
            self.image = surf
            self.rect = self.image.get_rect(center=(x, y))
            self.add(group)
            self.ids = ids                      #ID
            self.speed = 3                      #Скорость
            self.timer = 80                     #таймеры для разных умений 
            self.inv = 0                        #условия для разных умений
            self.skill = 0
            self.weapon = 0
            self.rel = 0
            self.dmg_up = 0
            self.sh = 0
            self.sh_timer = 80
            self.act_tp = 0
            self.timer_for_hill = 0
            self.timer_for_tp = 0
            self.hp_for_hil = self.hp           #Хп для умения аптечка
        def turn(self, surf):
            self.image = surf
        def lvlup(self):                        #Увеличение опыта
            self.lvl += 1
            self.expirience_point += LEVEL[self.lvl][2]
        def update(self, x, y):                 #Передвижение
                self.rect.x += x
                self.rect.y += y
        def distr_experience_point(self): #Распределение очков
            global hp_for_hill
            if self.ids == 1:
                self.hp = int(self.reg_hp + self.reg_hp * (self.sila / 60) +  self.reg_hp * ((self.protect - 3) / 40)) #Зависимость хп от кол-ва силы и защиты
                self.st = int(self.reg_st + self.reg_st * (self.sila / 60))
                self.sheld = int(self.reg_sheld + self.reg_sheld * (self.protect / 40))
                self.hp_for_hill = self.hp
            elif self.ids == 2:
                self.hp = int(self.reg_hp + self.reg_hp * (self.sila / 20) +  self.reg_hp * ((self.intelekt - 3) / 20)) #Зависимость хп от кол-ва силы и интелекта
                self.st = int(self.reg_st + self.reg_st * (self.intelekt / 30 ))
                self.sheld = int(self.reg_sheld + self.reg_sheld * (self.protect  / 40))
                self.hp_for_hill = self.hp
            else:
                self.hp = int(self.reg_hp + self.reg_hp * (self.sila / 30) +  self.reg_hp * ((self.protect - 2) / 25)) #Зависимость хп от кол-ва силы и защиты
                self.st = int(self.reg_st + self.reg_st * (self.intelekt / 50) +self.reg_st * ((self.sila - 2) / 30))
                self.sheld = int(self.reg_sheld + self.reg_sheld * (self.protect / 40) + self.reg_sheld  * ((self.intelekt - 3) / 25))
                self.hp_for_hill = self.hp
            
        def lern_skil(self): #Распределение скилов в зависимости от ID
            i = 1
            if self.id == 1:
                skill = skils_1
            elif self.id == 2:
                skill = skils_1
            else:
                skill = skils_1
            self.lernd_skill = lernd_skill
            
        def lerning_skill(self, skil_lern): #Открытие доступа для использования умений 
            skil_lern = skil_lern_1
            if len(skil_lern) == 1:
                self.skill = 1
            elif len(skil_lern) == 2:
                self.skill = 2
            elif len(skil_lern) == 3:
                self.skill = 3
        
        def __str__(self):
            return "Имя" + '-' + str(self.Name) + " " + "Фамилия" + '-' + str(self.Surname) + " " +  "Сила" + '-' + str(self.sila) + " " + "Интелект" + '-' + str(self.intelekt) + " " + "Защита" + '-' + str(self.protect) + " " +  "Умения" + '-' + str(lernd_skill)
    class Enemy(pygame.sprite.Sprite): #Враг
        def __init__(self, x, y, name, xp, sheld, dmg, exp, group, surf, inv_group, weapoon):
            pygame.sprite.Sprite.__init__(self)
            self.image = surf
            self.rect = self.image.get_rect(center=(x, y))
            self.name = name
            self.add(group)
            self.reg_xp = xp
            self.reg_sheld = sheld
            self.reg_dmg = dmg
            self.exp = exp
            self.xp = int(self.reg_xp + (self.reg_sheld * 0.2)) #здоровье зависит от общих характеристик
            self.speed = 3
            self.inv_box = pygame.Rect((x-200, y-200, 400, 400)) #Невидимый объект обозначающий поле зрения 
            self.timer = weapoon.timer_for_enemy + 10             #Задржка для выстрела
            self.reg_timer = weapoon.timer_for_enemy + 10          #Данные для восстановления таймера           

    class Gromila(Hero):                        #Громила клас, имеющий большее кол-во хп
        ids = 1
    class Hacker(Hero):                         #Хакер класс, имеющий превосходство на дальних дистанциях
        ids = 2
    class Mexanik(Hero):                        #Механик класс, имеющий среднее кол-во характеристик
        ids = 3

    class Skils:                                #Общий класс умений, из которого будут наслдедоваться необходимое число характеристик для изучения умения 
        def __init__(self, Name, n_s, n_i, n_p, ids):
            self.Name = Name
            self.n_s = int(n_s)
            self.n_i = int(n_i)
            self.n_p = int(n_p)
            if ids == 1:
                skils_1.append(self.Name)
                need_s_1.append(self.n_s)
                need_i_1.append(self.n_i)
                need_p_1.append(self.n_p)
            if ids == 2:
                skils_2.append(self.Name)
                need_s_2.append(self.n_s)
                need_i_2.append(self.n_i)
                need_p_2.append(self.n_p)
            if ids == 3:
                skils_3.append(self.Name)
                need_s_3.append(self.n_s)
                need_i_3.append(self.n_i)
                need_p_3.append(self.n_p)    
    class weapons(pygame.sprite.Sprite):
        def __init__(self, name, dmg, timer):
            pygame.sprite.Sprite.__init__(self)
            self.name = name
            self.dmg = dmg                          # Урон
            self.reg_timer = timer                  #Таймеры для выстрела и умений
            self.timer = 0
            self.timer_for_enemy = timer
            self.up_damage_timer = 120

    class Obj(pygame.sprite.Sprite):               #
        def __init__(self, x, y, surf, group):
            pygame.sprite.Sprite.__init__(self)
            self.image = surf
            self.rect = self.image.get_rect(center = (x, y))
            self.add(group)
            
    class Shot(pygame.sprite.Sprite):                   #Пуля
        def __init__(self, x, y, surf, group, t_x, t_y, surf_hole, group_hole, identity):
            pygame.sprite.Sprite.__init__(self)
            self.image = surf
            self.hole_image = surf_hole
            self.rect = self.image.get_rect(center=(x, y))
            self.t_x = t_x
            self.t_y = t_y
            self.inv_box = pygame.Rect((self.t_x, self.t_y-15, 15, 30))
            self.group = group
            self.add(group)
            self.group_hole = group_hole
            self.d_x = self.t_x - self.rect.x
            self.d_y = self.t_y - self.rect.y
            self.angle = math.atan2(self.d_y, self.d_x)
            self.speed = 15
            self.timer = 200
            self.identity = identity
            
        def montiont(self):         #Движение пули
            if self.rect.colliderect(self.inv_box) or (self.rect.x < 0 and self.rect.y < 0) or pygame.sprite.spritecollideany(self, bild) or pygame.sprite.spritecollideany(self, Stenki):
                self.group.remove(self)
                self.hole()
                return
            self.rect.x += self.speed * math.cos(self.angle)
            self.rect.y += self.speed * math.sin(self.angle)
        def hole(self): #Появление дыры от пули 
            self.image = self.hole_image
            self.add(self.group_hole)
        def remove(self):
            self.group_hole.remove(self)
            del self
        def damage(self, who_damage, weapoon):          #Урон по врагу
            if hero.dmg_up == 1:
                who_damage.xp -= (int(weapoon.dmg)+5)
            else:
                who_damage.xp -= int(weapoon.dmg)
            if who_damage.xp <= 0:
                who_damage.kill()
                hero.exp += who_damage.exp
        def damage_hero(self, who_damage, weapoon):     #Урон по персонажу
            who_damage.hp -= int(weapoon.dmg)
            if who_damage.hp <= 0:
                who_damage.kill()
            
    bild = pygame.sprite.Group()                        #группы для разных объектов
    hud = pygame.sprite.Group()
    Font = pygame.sprite.Group()
    menu = pygame.sprite.Group()
    Hero = pygame.sprite.Group()
    Stenki = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    holes = pygame.sprite.Group()
    enemy = pygame.sprite.Group()
    enemy_see = pygame.sprite.Group()
    house_or = Obj(401, 442, SPRITE_SURF[11], bild)        #Создание разных бъектов
    house_or_sh = Obj(752, 403, SPRITE_SURF[12], bild)
    house_or_bg = Obj(661, 104, SPRITE_SURF[13], bild)
    house_or_bg_2 = Obj(765, 104, SPRITE_SURF[14], bild)
    house_r_sh = Obj(156, 429, SPRITE_SURF[15], bild)
    house_r_bg = Obj(479, 117, SPRITE_SURF[16], bild)
    roaps = Obj(480,312, SPRITE_SURF[17], Font)
    objekt = Obj(480,312, SPRITE_SURF[18], Font)
    play = Obj(460, 220, SPRITE_SURF[0], menu)
    ehit = Obj(460, 410, SPRITE_SURF[2], menu)
    stena_1 =Obj(-5, (H/2),SPRITE_SURF[9], Stenki)
    stena_2 =Obj((W+5), (H/2), SPRITE_SURF[9], Stenki)
    stena_3 =Obj((W/2), -5, SPRITE_SURF[10], Stenki)
    stena_4 =Obj(W/2, (H+5), SPRITE_SURF[10], Stenki)
    inventor = Obj((W-150), (H-75), SPRITE_SURF[8], hud)
    skils = Obj((W-75), (H-75), SPRITE_SURF[7], hud)
    #Умения для Громилы
    Sprint = Skils("Спринт", 12, 3, 6, 1)       #Увеличивается скорость
    hill = Skils("Аптечка", 13, 5, 7, 1)           #Аптечка
    sheld = Skils("Щит", 14, 5, 9, 1)        #Получает неуязвимость на время 
    #Умения для Хакера
    Inviz = Skils("Инвиз", 3, 12, 2, 2)         #Невидим для врагов в течении некоторого времени                            
    hill = Skils("Аптечка", 5, 13, 2, 2)           #Аптечка
    teleport = Skils("Телепорт", 5, 15, 3, 2)     #Позволяет телепортироваться в любую точку на дороге                                                           
    #Умения для Механика
    Weapon_hand = Skils("Рука-оружие", 5, 6, 6, 3) #Позволяет стрелять из 2 оружий одновременно увеличивая скорострельность 
    hill = Skils("Аптечка", 6, 7, 8, 3)            #Аптечка 
    up_dmg = Skils("Увел.Урон", 7, 10, 9, 3)        #Увеличивает урон на 5 едениц
    #Оружие
    vector_v2 = weapons("Вектор v2", 4, 15)
    M56_44 = weapons('М56_44', 18, 40)
    type_41 = weapons("type_41", 10, 30)
    d_34 = weapons("d_34", 7 , 20)
    digle = weapons("digle", 13, 35)
    berrets = weapons("berets", 4, 16)
    bbsd_89 = weapons("bbsd_89", 6, 18)

    
    def save_inf(sil, intt, prott, ppoint):     #Обновление характеристик после распределения очков
        print(hero.sila, hero.intelekt, hero.protect, hero.expirience_point)
        hero.sila = sil
        hero.intelekt = intt
        hero.protect = prott
        hero.expirience_point = ppoint
        hero.distr_experience_point()
    def save_invent(inventory_save, hand_save): #Обновление инвентаря
        inventory = inventory_save
        hand = hand_save

    hand.append('d_34')
    inventory.append('M56_44')
    inventory.append('digle')
    inventory.append('type_41')
    inventory.append('berrets')
    inventory.append('bbsd_89')
    inventory.append('vector_v2')
        
    while  True:
        if hero_type == "Gr":
            hero = Gromila(ANSWER, ANSWER_2, 0, 8, 2, 6, 150, 40, 70, 100, 40, 70,SPRITE_SURF[3], 100, 600, Hero, 1)
        elif hero_type == "Ha":
            hero = Hacker(ANSWER, ANSWER_2, 0, 2, 8, 1, 100, 70, 40, 60, 70, 40,SPRITE_SURF[3], 100, 600, Hero, 2)
        elif hero_type == "Mex":
            hero = Mexanik(ANSWER, ANSWER_2, 0, 2, 4, 5, 70, 60, 50, 70, 60, 50,SPRITE_SURF[3], 100, 600, Hero, 3)
        break
    Ch = 0
    play = 2
    x = 0
    y = 0
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and ((i.pos[0] > 258 and i.pos[0] < 660)and(i.pos[1] > 133 and i.pos[1] < 303)) and play != 1:
                    play = 0
                elif i.button == 1 and ((i.pos[0] > 258 and i.pos[0] < 660)and(i.pos[1] > 320 and i.pos[1] < 498)) and play != 1:
                    pygame.quit()
                elif i.button == 1 and ((i.pos[0] > 791 and i.pos[0] < 829)and(i.pos[1] > 526 and i.pos[1] < 569)) and play == 1:
                    inventory_save, hand_save = run(inventory, hand)
                    run(inventory, hand)
                    save_invent(inventory_save, hand_save)
                elif i.button == 1 and (((i.pos[0] >854 and i.pos[0] < 916) and (i.pos[1] > 543 and i.pos[1] < 559)) or ((i.pos[0] > 861 and i.pos[0] < 900) and (i.pos[1] > 563 and i.pos[1] < 569)) or ((i.pos[0]>869 and i.pos[0]<906) and (i.pos[1]>530 and i.pos[1]<539))):
                    global save_info_sil, save_info_int, save_info_prot, save_info_point
                    if hero.ids == 1:
                        skils_i = skils_1
                        need_s = need_s_1
                        need_i = need_i_1
                        need_p = need_p_1
                    elif hero.ids == 2:
                        skils_i = skils_2
                        need_s = need_s_2
                        need_i = need_i_2
                        need_p = need_p_2
                    elif hero.ids == 3:
                        skils_i = skils_3
                        need_s = need_s_3
                        need_i = need_i_3
                        need_p = need_p_3
                    save_info_sil, save_info_int, save_info_prot, save_info_point, skil_lern_1 = run_skill(hero.hp, hero.st, hero.sheld, lernd_skill, skils_i, need_s, need_i, need_p, hero.sila, hero.intelekt, hero.protect, hero.expirience_point,skil_lern)
                    run_skill(hero.hp, hero.st, hero.sheld, lernd_skill, skils_i, need_s, need_i, need_p, hero.sila, hero.intelekt, hero.protect, hero.expirience_point,skil_lern)
                    save_inf(save_info_sil, save_info_int, save_info_prot, save_info_point)
                    hero.lerning_skill(skil_lern_1)
                elif i.button == 1 and play == 1 and hero.hp > 0 and hero.weapon.timer <=0 and hero.act_tp == 0 or hero.rel == 1 and i.button == 1 and play == 1 and hero.hp > 0 and hero.act_tp == 0:
                    shoot_chek = 1
                    iy = i.pos[1]
                    ix = i.pos[0]
                    herox = hero.rect.x+hero.rect[2]//2
                    heroy = hero.rect.y+hero.rect[3]//2
                    bullet = Shot(herox, heroy, SPRITE_SURF[19], shot, ix, iy, SPRITE_SURF[20], holes, 1)
                    hero.weapon.timer
                    if hero.weapon.timer <=0:
                        hero.weapon.timer = hero.weapon.reg_timer
                if i.button == 1 and hero.act_tp == 1:
                    tx = i.pos[0]
                    ty = i.pos[1]
                    if (tx > 6 and ty>240 and tx<80 and ty<604 or tx>=80 and ty>234 and tx< 946 and ty<309 or tx>78 and ty> 544 and tx<904 and ty<619 or tx>600 and ty>=309 and tx<670 and ty<536 or tx>829 and ty>16 and tx<907 and ty<547 or tx>285 and ty>18 and tx< 363 and ty<233)and hero.timer_for_tp <=0:
                        hero.rect.x = i.pos[0]
                        hero.rect.y = i.pos[1]
                        hero.act_tp = 0
                        hero.timer_for_tp = 400
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hero.hp>0:
            hero.turn(SPRITE_SURF[4])
            x = -(hero.speed)
        if keys[pygame.K_RIGHT] and hero.hp>0:
            hero.turn(SPRITE_SURF[6])
            x = hero.speed
        if keys[pygame.K_UP] and hero.hp>0:
            hero.turn(SPRITE_SURF[3])
            y = -(hero.speed)
        if keys[pygame.K_DOWN] and hero.hp>0:
            hero.turn(SPRITE_SURF[5])
            y = hero.speed
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            x = 0
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            y = 0
        hero.update(x, y)
        if keys[pygame.K_1] and hero.skill > 0: #Скилл 1
            skil_activ = 1
            if hero.ids == 1:
                hero.speed = 5
            elif hero.ids == 2:
                hero.inv = 1
            elif hero.ids == 3:
                hero.rel = 1
        if keys[pygame.K_2] and hero.skill >1:  #Скилл 2
            skil_2_activ = 1
            if hero.timer_for_hill <=0:
                if hero.hp_for_hil - hero.hp > 50:
                    hero.hp += 50
                elif hero.hp_for_hil - hero.hp < 50:
                    hero.hp += (hero.hp_for_hil - hero.hp)
                hero.timer_for_hill = 400
        if keys[pygame.K_3] and hero.skill > 2: #Скилл 3
            skil_3_activ = 1
            if hero.ids == 1:
                hero.sh = 1
            elif hero.ids == 2:
                hero.act_tp = 1
            elif hero.ids == 3:
                hero.dmg_up = 1
            
        if pygame.sprite.spritecollideany(hero, Stenki) or pygame.sprite.spritecollideany(hero, bild):
            if x != 0:
                x = -x
            if y != 0:
                y = -y
            hero.update(x, y)
        if play == 0:
            sc.fill(BLACK)
            play = 1
        elif play == 1:
            text = 'Hp:' + str(hero.hp) + ' ' + 'lvl:' + str(hero.lvl)+ ' ' + 'Score:' + str(hero.exp) +' '+ 'Points:' + str(hero.expirience_point)
            text_hp = Font1.render(text, 1, (255, 255, 255))
            for piu in shot:
                piu.montiont()
            for hole in holes:
                hole.timer -= 1
                if hole.timer <=0:
                    hole.remove()
            if len(enemy.sprites()) < 1:
                chos = randint(0, 3)
                x = randint(random_sp_x[chos][0],random_sp_x[chos][1])
                y = randint(random_sp_y[chos][0],random_sp_y[chos][1])
                random = randint(0, 100)
                if random <= 70:
                    raider = Enemy(x, y, "raider", 30, 35, 7, 100, enemy,SPRITE_SURF[21],enemy_see,type_41)
                elif random > 70 and random <=90:
                    raider = Enemy(x, y,"rar_raider", 50, 50, 80, 50, enemy, SPRITE_SURF[22],enemy_see,berrets)
                elif random > 90 and random <= 97:
                    raider = Enemy(x, y,"mini_boss", 90, 80, 60, 100, enemy, SPRITE_SURF[23],enemy_see,d_34)
                elif random > 97 and random <=100:
                    raider = Enemy(x, y,'boss', 110, 100, 25, 150, enemy, SPRITE_SURF[24],enemy_see,M56_44)
            
                    
            elif hero.rect.colliderect(raider.inv_box) and hero.inv ==0:
                enemyx = raider.rect.x+raider.rect[2]//2
                enemyy = raider.rect.y+raider.rect[3]//2
                hx = hero.rect.x+hero.rect[2]//2
                hy = hero.rect.y+hero.rect[3]//2
                for raider in enemy:
                    if pygame.sprite.spritecollideany(hero, shot) and bullet.identity == 2 and hero.sh == 0:
                        bullet.damage_hero(hero, M56_44)
                    raider.timer -= 1
                    if raider.timer <= 0 and hero.hp>0:
                        bullet = Shot(enemyx, enemyy, SPRITE_SURF[19], shot, hx, hy, SPRITE_SURF[20], holes, 2)
                if raider.timer <= 0:
                    raider.timer = raider.reg_timer

                if pygame.sprite.spritecollideany(raider, shot) and bullet.identity == 1:
                    bullet.damage(raider, weapan)
                    bullet.kill()


            if hand[0] == 'vector_v2':
                weapan = vector_v2
            elif hand[0] == 'M56_44':
                weapan = M56_44
            elif hand[0] == 'type_41':
                weapan = type_41
            elif hand[0] == 'd_34':
                weapan = d_34
            elif hand[0] == 'digle':
                weapan = digle
            elif hand[0] == 'berrets':
                weapan = berrets
            elif hand[0] == 'bbsd_89':
                weapan = bbsd_89
            hero.weapon = weapan
            
            
            if hero.exp >= LEVEL[hero.lvl+1][1]:
                hero.lvlup()
            if skil_activ == 1:
                text1 = '1 скилл: Осталось' + str(hero.timer)
                text_skil_1= Font1.render(text1, 1, (255, 255, 255))
                hero.timer -=1
                if hero.timer <=0:
                    text1 = '1 скилл: Готов'
                    text_skil_1= Font1.render(text1, 1, (255, 255, 255))
                    skil_activ = 0
                    hero.speed = 3
                    hero.inv = 0
                    hero.rel = 0
                    hero.timer = 80
            if skil_2_activ == 1:
                hero.timer_for_hill -=1
                text2 = '2 скилл: Перезарядка' + str(hero.timer_for_hill)
                text_skil_2= Font1.render(text2, 1, (255, 255, 255))
                if hero.timer_for_hill <=0:
                    text2 = '2 скилл: Готов'
                    text_skil_2= Font1.render(text2, 1, (255, 255, 255))
                    skil_2_activ = 0 
            if skil_3_activ == 1:
                if hero.ids == 3:
                    text3 = '3 Скилл: Осталось' + str(hero.weapon.up_damage_timer)
                    text_skil_3= Font1.render(text3, 1, (255, 255, 255))
                    hero.weapon.up_damage_timer -= 1
                    if hero.weapon.up_damage_timer <= 0:
                        text3 = '3 Скилл: Готов'
                        text_skil_3= Font1.render(text3, 1, (255, 255, 255))
                        skil_3_activ = 0
                        hero.dmg_up = 0
                        hero.weapon.up_damage_timer = 120
                if hero.ids == 1:
                    text3 = '3 Скилл: Осталось' + str(hero.sh_timer)
                    text_skil_3= Font1.render(text3, 1, (255, 255, 255))
                    hero.sh_timer -= 1
                    if hero.sh_timer <=0:
                        text3 = '3 Скилл: Готов'
                        text_skil_3= Font1.render(text3, 1, (255, 255, 255))
                        skil_3_activ = 0
                        hero.sh = 0
                        hero.sh_timer = 80
                if hero.ids == 2:
                    text3 = '3 Скилл: Перезарядка' + str(hero.timer_for_tp)
                    text_skil_3= Font1.render(text3, 1, (255, 255, 255))
                    hero.timer_for_tp -=1

                    if hero.timer_for_tp <= 0:
                        text3 = '3 Скилл: Готов'
                        text_skil_3= Font1.render(text3, 1, (255, 255, 255))
                    if hero.timer_for_tp >0:
                        hero.act_tp = 0
                        
            if shoot_chek == 1:
                hero.weapon.timer -=1
                if hero.weapon.timer <=0:
                    shoot_chek = 0
            if hero.hp <= 0:
                Dead_text = "Игра окончена"
                Dead = Font2.render(Dead_text, 1, (225, 0, 50))
                Dead_text2 = "перезапустите игру"
                Dead2 = Font2.render(Dead_text2, 1, (225, 0, 50))
                sc.blit(Dead2, (100,400))
            sc.blit(Dead,(480,312))
            sc.blit(road, road_rect)
            shot.draw(sc)
            enemy.draw(sc)
            enemy_see.draw(sc)
            holes.draw(sc)
            Hero.draw(sc)
            Stenki.draw(sc)
            hud.draw(sc)
            bild.draw(sc)
            Font.draw(sc)
            sc.blit(text_hp, (100,20))
            sc.blit(text_skil_1,(700,20))
            sc.blit(text_skil_2,(700,40))
            sc.blit(text_skil_3,(700,60))
            sc.blit(Dead,(150,212))
            sc.blit(Dead2, (150,290))
        elif play == 2:
            menu.draw(sc)
            pygame.display.update()

        pygame.time.delay(20)
        pygame.display.update()
