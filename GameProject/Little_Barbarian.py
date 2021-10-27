import pygame
from Enemies import Enemy

imgs = []
for x in range(10):
    img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("little_barbarian_moving/6_enemies_1_walk_00" + str(x) + ".png"), (64, 64)), False, False)
    imgs.append(img)
for x in range(10, 20):
    img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("little_barbarian_moving/6_enemies_1_walk_0" + str(x) + ".png"), (64, 64)), False, False)
    imgs.append(img)

class Little_Barbarian(Enemy):
    maxhealth = 1.5
    def __init__(self):
        super().__init__()
        self.imgss = imgs[:]
        self.img = None
        self.max_health = Little_Barbarian.maxhealth
        self.original_health = 1.5
        self.health = self.max_health
        self.speed = 0.06
        self.money = 2
        self.little_barbarian_count = 0
        self.name = "Little_Barbarian"


    def draw(self, win, menu):
        self.img = self.imgss[self.little_barbarian_count]
        self.textsurface = self.font.render(f"{round(self.health, 1)} / {round(self.max_health, 1)}" , False, (0, 0, 0))
        super().draw(win, menu)


    def move(self, dt):
        self.little_barbarian_count += 1
        if self.little_barbarian_count >= len(self.imgss):
            self.little_barbarian_count = 0
        super().move(dt)

    def class_maxhp_add(self, level):
        Little_Barbarian.maxhealth = self.original_health * (1 + level // 5 * self.percentage)
        self.max_health = Little_Barbarian.maxhealth
        self.health = self.max_health