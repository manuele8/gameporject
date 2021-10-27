import pygame
from Enemies import Enemy

imgs = []
for x in range(10):
    img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("warrior_moving/8_enemies_1_walk_00" + str(x) + ".png"), (64, 64)), False, False)
    imgs.append(img)
for x in range(10, 20):
    img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("warrior_moving/8_enemies_1_walk_0" + str(x) + ".png"), (64, 64)), False, False)
    imgs.append(img)

class Warrior(Enemy):
    maxhealth = 2
    def __init__(self):
        super().__init__()
        self.imgss = imgs[:]
        self.img = None
        self.max_health = Warrior.maxhealth
        self.original_health = 2
        self.health = self.max_health
        self.speed = 0.055
        self.warrior_count = 0
        self.money = 3
        self.name = "Warrior"


    def draw(self, win, menu):
        self.img = self.imgss[self.warrior_count]
        self.textsurface = self.font.render(f"{round(self.health, 1)} / {round(self.max_health, 1)}" , False, (0, 0, 0))
        super().draw(win, menu)


    def move(self, dt):
        self.warrior_count += 1
        if self.warrior_count >= len(self.imgss):
            self.warrior_count = 0
        super().move(dt)

    def class_maxhp_add(self, level):
        Warrior.maxhealth = self.original_health * (1 + level // 5 * self.percentage)
        self.max_health = Warrior.maxhealth
        self.health = self.max_health