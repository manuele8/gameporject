import pygame
from Towers import Towers
imgs = []
img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("Magic-Tower-Game-Assets2-11.png"), (200, 210)), False, False)
for i in range(1, 10):
    imgs.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("Magic-Tower-Game-Assets2-0" + str(i) + ".png"), (200, 210)), False, False))
imgs.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("Magic-Tower-Game-Assets2-10.png"), (200, 210)), False,False))

class ElectricTower(Towers):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgss = imgs[:]
        self.imgtw = img
        self.imgch = None
        self.range = 200
        self.original_range = self.range

    def draw(self, win):
        if self.tower_count >= self.fps * self.COOLDOWN:
            self.tower_count = 0
        self.imgch = self.imgss[int(self.tower_count * len(self.imgss) / (self.fps * self.COOLDOWN))]
        super().draw(win)

    def increment_tower_count(self):
        self.tower_count += 1

    def reset_tower_count(self):
        self.tower_count = 0