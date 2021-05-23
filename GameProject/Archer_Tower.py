import pygame
from Towers import Towers
imgs = []
img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("archer_tower/R28e63f9ec521e7e9eebe413956c40ee4.png"), (100, 110)), False, False)
for i in range(10):
    imgs.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("archer_tower/archer/imageonline-co-whitebackgroundremoved (" + str(i) + ").png"), (150, 80)), True, False))

class ArcherTower(Towers):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgss = imgs[:]
        self.imgtw = img
        self.imgch = None
        self.imgch_x = 25
        self.imgch_y = 23
        self.range = 200

    def draw(self, win):
        if self.tower_count >= self.fps * self.COOLDOWN:
            self.tower_count = 0
        self.imgch = self.imgss[int(self.tower_count * len(self.imgss) / (self.fps * self.COOLDOWN))]
        super().draw(win)

    def increment_tower_count(self):
        self.tower_count += 1

    def reset_tower_count(self):
        self.tower_count = 0