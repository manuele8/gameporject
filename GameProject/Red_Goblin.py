import pygame
from Enemies import Enemy

imgs = []
for x in range(10):
    img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("red_goblin_moving/1_enemies_1_walk_00" + str(x) + ".png"), (64, 64)), False, False)
    imgs.append(img)
for x in range(10, 20):
    img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("red_goblin_moving/1_enemies_1_walk_0" + str(x) + ".png"), (64, 64)), False, False)
    imgs.append(img)

class Red_Goblin(Enemy):
    maxhealth = 4.5
    def __init__(self):
        super().__init__()
        self.imgss = imgs[:]
        self.img = None
        self.max_health = Red_Goblin.maxhealth
        self.original_health = 4.5
        self.health = self.max_health
        self.speed = 0.04
        self.red_goblin_count = 0
        self.subtract_lives = 2
        self.money = 5
        self.name = "Red_Goblin"

    def draw(self, win):
        self.img = self.imgss[self.red_goblin_count]
        super().draw(win)

    def move(self, dt):
        self.red_goblin_count += 1
        if self.red_goblin_count >= len(self.imgss):
            self.red_goblin_count = 0
        super().move(dt)

    def class_maxhp_add(self, level):
        Red_Goblin.maxhealth = self.original_health * (1 + level // 5 * self.percentage)
        self.max_health = Red_Goblin.maxhealth
        self.health = self.max_health