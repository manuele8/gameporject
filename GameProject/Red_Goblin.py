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
    def __init__(self):
        super().__init__()
        self.imgss = imgs[:]
        self.img = None
        self.max_health = 4
        self.health = self.max_health
        self.speed = 0.04
        self.red_goblin_count = 0
        self.subtract_lives = 2

    def draw(self, win):
        if self.red_goblin_count >= len(self.imgss):
            self.red_goblin_count = 0
        self.img = self.imgss[self.red_goblin_count]
        super().draw(win)
        self.red_goblin_count += 1