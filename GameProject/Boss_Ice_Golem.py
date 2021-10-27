import pygame
from Enemies import Enemy

imgs = []
for x in range(10):
    img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("boss_ice_golem_moving/0_Golem_Walking_00" + str(x) + ".png"), (128, 128)), False, False)
    imgs.append(img)
for x in range(10, 24):
    img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("boss_ice_golem_moving/0_Golem_Walking_0" + str(x) + ".png"), (128, 128)), False, False)
    imgs.append(img)

class Boss_Ice_Golem(Enemy):
    maxhealth = 20
    def __init__(self):
        super().__init__()
        self.imgss = imgs[:]
        self.img = None
        self.max_health = Boss_Ice_Golem.maxhealth
        self.original_health = 20
        self.health = self.max_health
        self.speed = 0.03
        self.path = [(-110, 380), (-5, 380), (44, 380), (87, 380), (132, 425), (185, 425), (221, 425), (257, 425), (289, 425), (320, 425), (357, 425), (392, 426), (440, 427), (480, 428), (516, 428), (553, 429), (587, 430), (630, 390), (650, 370), (660, 354), (650, 325), (640, 296), (620, 250), (600, 230), (509, 229), (482, 223), (438, 221), (408, 220), (370, 220), (337, 219), (321, 202), (315, 183), (315, 152), (315, 109), (320, 84), (330, 59), (335, 0), (366, 0), (402, 0), (436, 0), (480, 0), (516, 0), (563, 0), (604, 0), (642, 0), (690, 0), (730, 0), (770, 0), (808, 0), (840, 0), (883, 0), (918, 0), (951, 0), (983, 0)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_pos = 0
        self.boss_ice_golem_count = 0
        self.name = "Boss_Ice_Golem"
        self.subtract_lives = 5
        self.money = 20

    def draw(self, win, menu):
        self.img = self.imgss[self.boss_ice_golem_count]
        self.textsurface = self.font.render(f"{round(self.health, 1)} / {round(self.max_health, 1)}" , False, (0, 0, 0))
        super().draw(win, menu)

    def move(self, dt):
        self.boss_ice_golem_count += 1
        if self.boss_ice_golem_count >= len(self.imgss):
            self.boss_ice_golem_count = 0
        super().move(dt)

    def draw_health_bar(self, win):
        lenght = 50
        health_bar = (self.health/self.max_health)*lenght
        pygame.draw.rect(win, (255, 0, 0), (self.x + 38, self.y + 13, lenght, 10))
        pygame.draw.rect(win, (0, 255, 0), (self.x + 38, self.y + 13, health_bar, 10))
        #win.blit(self.textsurface, (self.x + 38 + self.lenght // 2 - self.textsurface.get_width() // 2, self.y + 13 - self.high // 2 + self.textsurface.get_height() // 2))
    def class_maxhp_add(self, level):
        Boss_Ice_Golem.maxhealth = self.original_health * (1 + (level - 1) // 5 * self.percentage)
        self.max_health = Boss_Ice_Golem.maxhealth
        self.health = self.max_health