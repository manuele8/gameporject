import pygame
import math
imgs = []
img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("archer_tower/R28e63f9ec521e7e9eebe413956c40ee4.png"), (100, 140)), False, False)
imgs.append(img)
imgs.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load("archer_tower/Screenshot (274).png"), (180, 85)), False, False))
class Towers:
    def __init__(self, x, y):
        self.imgss = imgs
        self.x = x
        self.y = y
        self.range = 150
        self.tower_count = 0
        self.damage = 0.01
        self.selected_value = False

    def draw(self, win):
        if self.tower_count >= len(self.imgss):
            self.tower_count = 0
        self.imgtw = self.imgss[0]
        self.imgarch = self.imgss[1]
        win.blit(self.imgtw, (self.x, self.y))
        win.blit(self.imgarch, (self.x - 85, self.y - 20))
        self.tower_count += 1
        self.imgarch.convert_alpha(win)
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        if self.selected_value:
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            win.blit(surface, (self.x + self.imgtw.get_width()//2 - self.range, self.y + self.imgtw.get_height()//2 - self.range))

    def inrange(self, objs):
        for obj in objs:
            dist = math.sqrt((self.x + self.imgtw.get_width()//2 - obj.x)**2 + (self.y + self.imgtw.get_height()//2 - obj.y)**2)
            if dist <= self.range:
                obj.health -= self.damage

    def selected(self, tuple):
        if abs(tuple[0] - self.x - self.imgtw.get_width()//2) <= 50 and abs(tuple[1] - self.y - self.imgtw.get_height()//2) <= 70:
            self.selected_value = True
        else:
            self.selected_value = False
