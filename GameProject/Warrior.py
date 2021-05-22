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
    def __init__(self):
        super().__init__()
        self.imgss = imgs[:]
        self.img = None
        self.max_health = 2
        self.health = self.max_health
        self.speed = 0.055
        self.warrior_count = 0

    def draw(self, win):
        if self.warrior_count >= len(self.imgss):
            self.warrior_count = 0
        self.img = self.imgss[self.warrior_count]
        super().draw(win)
        self.warrior_count += 1
