import pygame
from Towers import Towers
import math
imgs = []
img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("kale1_12.png"), (200, 200)), False, False)


class DamageTower(Towers):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgss = imgs[:]
        self.imgtw = img
        self.imgch = None
        self.range = 300
        self.effect = 0.2
        self.effected_towers = []


    def inrange(self, objs):
        for obj in objs:
            if obj.imgch == None:
                point = (obj.x + obj.imgtw.get_width(), obj.y)
            else:
                point = (obj.x + obj.imgtw.get_width()/2, obj.y - obj.imgch.get_height()/2 - 15)
            dist = math.sqrt((self.x + self.imgtw.get_width()//2 - point[0]) ** 2 + (
                        self.y + self.imgtw.get_height()//2 - point[1]) ** 2)
            if dist <= self.range:
                self.effected_towers.append(obj)
        for element in self.effected_towers:
            element.damage = element.original_damage*(1 + self.effect)