import pygame
from Enemies import Enemy

imgs = []
for x in range(10):
    img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("goblin_moving/2_enemies_1_walk_00" + str(x) + ".png"), (64, 64)), False, False)
    imgs.append(img)
for x in range(10, 20):
    img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("goblin_moving/2_enemies_1_walk_0" + str(x) + ".png"), (64, 64)), False, False)
    imgs.append(img)

class Goblin(Enemy):
    maxhealth = 0.5
    def __init__(self):
        super().__init__()
        self.imgss = imgs[:]
        self.img = None
        self.max_health = Goblin.maxhealth
        self.original_health = 0.5
        self.health = self.max_health
        self.speed = 0.1
        self.goblin_count = 0
        self.name = "Goblin"

    def draw(self, win):
        self.img = self.imgss[self.goblin_count]
        super().draw(win)

    def move(self, dt):
        self.goblin_count += 1
        if self.goblin_count >= len(self.imgss):
            self.goblin_count = 0
        super().move(dt)

    def class_maxhp_add(self, level):
        Goblin.maxhealth = self.original_health * (1 + level // 5 * self.percentage)
        self.max_health = Goblin.maxhealth
        self.health = self.max_health