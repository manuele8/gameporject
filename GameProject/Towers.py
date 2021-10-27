import time
import pygame
import math

class Towers:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.imgss = []
        self.imgtw = None
        self.imgch = None
        self.range = 150
        self.original_range = self.range
        self.tower_count = 0
        self.damage = 0.3
        self.original_damage = self.damage
        self.distance_x = 50
        self.distance_y = 70
        self.imgch_x = 85
        self.imgch_y = 20
        self.selected_value = False
        self.hit_obj = None
        self.flipped = False
        self.append_objects = []
        self.cooldown = 0
        self.COOLDOWN = 0.55
        self.fps = 60
        self.change_target_array = [3]
        self.enemies = []
        self.cont = 0
        self.area = False

    def draw(self, win):
        win.blit(self.imgtw, (self.x, self.y))
        if self.imgch != None:
            win.blit(self.imgch, (self.x - self.imgch_x, self.y - self.imgch_y))
            self.imgch.convert_alpha(win)
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        if self.selected_value:
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            win.blit(surface, (self.x + self.imgtw.get_width()//2 - self.range, self.y + self.imgtw.get_height()//2 - self.range))

    def inrange(self, objs):
        for obj in objs:
            dist = math.sqrt((self.x + self.imgtw.get_width()//2 - obj.x - obj.get_width()/2)**2 + (self.y + self.imgtw.get_height()//2 - obj.y - obj.get_height()/2)**2)
            if dist <= self.range:
                self.append_objects.append(obj.health)
                self.enemies.append(obj)
        if not self.area:
            if self.append_objects != []:
                min_health = min(self.append_objects)
                for obj in objs:
                    if obj.health == min_health:
                        dist = math.sqrt((self.x + self.imgtw.get_width() // 2 - obj.x - obj.get_width() / 2) ** 2 + (
                                self.y + self.imgtw.get_height() // 2 - obj.y - obj.get_height() / 2) ** 2)
                        if dist <= self.range:
                            self.hit_obj = obj
                            self.Attack(self.hit_obj)
                            self.Flip_Image(self.hit_obj)
                            if self.Change_Target(self.hit_obj):
                                self.tower_count = 0
                            else:
                                self.tower_count += 1
                            break

            else:
                self.tower_count = 0
                if self.flipped:
                    for x, imgg in enumerate(self.imgss):
                        self.imgss[x] = pygame.transform.flip(imgg, True, False)
                    self.flipped = False
        else:
            if self.enemies != []:
                self.hit_obj = self.enemies[0]
                self.AttackGroup(self.enemies)
                self.Flip_Image(self.hit_obj)
                if self.Change_Target(self.hit_obj):
                    self.tower_count = 0
                else:
                    self.tower_count += 1
            else:
                self.tower_count = 0
                if self.flipped:
                    for x, imgg in enumerate(self.imgss):
                        self.imgss[x] = pygame.transform.flip(imgg, True, False)
                    self.flipped = False
        self.append_objects = []
        self.enemies = []

    def Attack(self, obj):
        if self.cooldown == 0:
            obj.health -= self.damage
            self.cooldown = 1
        if self.cooldown > 0 and self.cooldown <= 1:
            self.cooldown -= 1 / (60 * self.COOLDOWN)
        else:
            self.cooldown = 0

    def AttackGroup(self, objs):
        if self.cooldown == 0:
            for obj in objs:
                obj.health -= self.damage
            self.cooldown = 1
        if self.cooldown > 0 and self.cooldown <= 1:
            self.cooldown -= 1 / (60 * self.COOLDOWN)
        else:
            self.cooldown = 0

    def Change_Target(self, obj):
        self.change_target_array.append(obj)
        if len(self.change_target_array) > 2:
            self.change_target_array.pop(0)
        if len(self.change_target_array) == 2:
            if self.change_target_array[0] != self.change_target_array[1]:
                return True
            return False
        return True

    def Flip_Image(self, obj):
        if self.x + self.imgtw.get_width() // 2 - obj.x - obj.get_width() / 2 < 0 and not self.flipped:
            for x, imgg in enumerate(self.imgss):
                self.imgss[x] = pygame.transform.flip(imgg, True, False)
            self.flipped = True
        elif self.x + self.imgtw.get_width() // 2 - obj.x - obj.get_width() / 2 > 0 and self.flipped:
            for x, imgg in enumerate(self.imgss):
                self.imgss[x] = pygame.transform.flip(imgg, True, False)
            self.flipped = False





    def selected(self, tuple):
        if abs(tuple[0] - self.x - self.imgtw.get_width()//2) <= self.distance_x and abs(tuple[1] - self.y - self.imgtw.get_height()//2) <= self.distance_y:
            self.selected_value = True
        else:
            self.selected_value = False
