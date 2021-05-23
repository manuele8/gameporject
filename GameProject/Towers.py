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
        self.tower_count = 0
        self.damage = 0.6
        self.distance_x = 50
        self.distance_y = 70
        self.imgch_x = 85
        self.imgch_y = 20
        self.selected_value = False
        self.hit_obj = None
        self.flipped = False
        self.append_objects = []
        self.cooldown = 0
        self.COOLDOWN = 0.6
        self.fps = 60
        self.change_target_array = []
        self.cont = 0

    def draw(self, win):
        win.blit(self.imgtw, (self.x, self.y))
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
        if self.append_objects != []:
            min_health = min(self.append_objects)
            for obj in objs:
                if obj.health == min_health:
                    dist = math.sqrt((self.x + self.imgtw.get_width() // 2 - obj.x - obj.get_width() / 2) ** 2 + (
                            self.y + self.imgtw.get_height() // 2 - obj.y - obj.get_height() / 2) ** 2)
                    if dist <= self.range:
                        self.hit_obj = obj
                        self.Attack(self.hit_obj)
                        if self.Change_Target(obj):
                            self.tower_count = 0
                        else:
                            self.tower_count += 1
                        break

        else:
            self.tower_count = 0
        self.append_objects = []

    def Attack(self, obj):
        if self.cooldown == 0:
            obj.health -= self.damage
            self.cooldown = 1
        elif self.cooldown > 0 and self.cooldown <= 1:
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

    def Obj_Position(self, obj):
        if self.x + self.imgtw.get_width() // 2 - obj.x - obj.get_width() / 2 < 0:
            return True
        return False





    def selected(self, tuple):
        if abs(tuple[0] - self.x - self.imgtw.get_width()//2) <= self.distance_x and abs(tuple[1] - self.y - self.imgtw.get_height()//2) <= self.distance_y:
            self.selected_value = True
        else:
            self.selected_value = False
