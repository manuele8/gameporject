import pygame
from Towers import Towers
import math
imgs = []
img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("imageonline-co-whitebackgroundremoved.png"), (100, 110)), False, False)
class RangeTower(Towers):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgss = imgs[:]
        self.imgtw = img
        self.imgch = None
        self.range = 130
        self.effect = 0.2
        self.effected_towers = []

    #tw.x + tw.imgtw.get_width(), tw.y + tw.imgtw.get_height()
    def inrange(self, objs):
        for obj in objs:
            if obj.imgch == None:
                point = (obj.x + obj.imgtw.get_width(), obj.y)
            else:
                point = (obj.x + obj.imgtw.get_width()/2 + 10, obj.y - obj.imgch.get_height()/2 + 30)
            dist = math.sqrt((self.x + self.imgtw.get_width()//2 - point[0]) ** 2 + (
                        self.y + self.imgtw.get_height()//2 - point[1]) ** 2)
            if dist <= self.range:
                self.effected_towers.append(obj)
        for element in self.effected_towers:
            element.range = element.original_range*(1 + self.effect)