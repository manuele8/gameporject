import pygame
from Towers import Towers
import math
imgs = []
img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("imageonline-co-whitebackgroundremoved.png"), (100, 110)), False, False)
class DamageTower(Towers):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgss = imgs[:]
        self.imgtw = img
        self.imgch = None
        self.range = 100
        self.effect = 0.2
        self.effected_towers = []


    def inrange(self, objs):
        for obj in objs:
            dist = math.sqrt((self.x + self.imgtw.get_width() // 2 - obj.x - obj.imgtw.get_width() / 2) ** 2 + (
                        self.y + self.imgtw.get_height() // 2 - obj.y - obj.imgtw.get_height() / 2) ** 2)
            if dist <= self.range:
                self.effected_towers.append(obj)
        for element in self.effected_towers:
            element.damage = element.original_damage*(1 + self.effect)