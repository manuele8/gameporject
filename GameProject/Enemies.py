import pygame
import math

class Enemy:
    def __init__(self):
        self.imgss = []
        self.img = None
        self.max_health = 3
        self.health = self.max_health
        self.regenhealth = 0
        self.path = [(-50, 430), (55, 430), (104, 430), (147, 430), (192, 475), (245, 475), (281, 475), (317, 475), (349, 475), (380, 475), (417, 475), (452, 476), (500, 477), (540, 478), (576, 478), (613, 479), (647, 480), (666, 440), (678, 420), (679, 404), (673, 375), (663, 346), (652, 323), (631, 303), (600, 280), (569, 279), (542, 273), (498, 271), (468, 270), (430, 270), (397, 269), (381, 252), (350, 233), (345, 202), (345, 159), (357, 134), (369, 109), (395, 50), (426, 50), (462, 50), (496, 50), (540, 50), (576, 50), (623, 50), (664, 50), (702, 50), (750, 50), (790, 50), (830, 50), (868, 50), (900, 50), (943, 50), (978, 50), (1011, 50), (1043, 50)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_pos = 0
        self.speed = 0.05
        self.overflow_dist = 0
        self.subtract_lives = 1
        self.flipped = False

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        self.draw_health_bar(win)
        self.regen_health()

    def move(self, dt):
        x1, y1 = self.path[self.path_pos]

        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (610, 275)

            if abs(self.x - x2) < 0.0000001 and abs(self.y - y2) < 0.0000001:
                return
        else:
            x2, y2 = self.path[self.path_pos + 1]

        dir_vector = x2 - x1, y2 - y1
        dir_vector_len = math.sqrt((dir_vector[0] ** 2 + dir_vector[1] ** 2))

        dir_vector_norm = dir_vector[0] / dir_vector_len, dir_vector[1] / dir_vector_len

        self.x += dir_vector_norm[0] * self.speed * dt
        self.y += dir_vector_norm[1] * self.speed * dt


        distance_from_last_path_pos = math.sqrt(((self.x - x1) ** 2 + (self.y - y1) ** 2))
        segment_length = dir_vector_len

        if distance_from_last_path_pos >= segment_length:  # checks if a path segment has been exceeded and includes that into the next .move() call
            self.overflow_dist = math.sqrt(((self.x - x2) ** 2 + (self.y - y2) ** 2))
            self.path_pos += 1
        if dir_vector_norm[0] < 0 and not self.flipped:
            self.flipped = True
            for x, img in enumerate(self.imgss):
                self.imgss[x] = pygame.transform.flip(img, True, False)
        if dir_vector_norm[0] > 0 and self.flipped:
            self.flipped = False
            for x, img in enumerate(self.imgss):
                self.imgss[x] = pygame.transform.flip(img, True, False)



    def get_height(self):
        return self.img.get_height()

    def get_width(self):
        return self.img.get_width()

    def draw_health_bar(self, win):
        lenght = 50
        health_bar = (self.health/self.max_health)*lenght
        if not self.flipped:
            pygame.draw.rect(win, (255, 0, 0), (self.x - 3, self.y - 5, lenght, 10))
            pygame.draw.rect(win, (0, 255, 0), (self.x - 3, self.y - 5, health_bar, 10))
        else:
            pygame.draw.rect(win, (255, 0, 0), (self.x + 15, self.y - 5, lenght, 10))
            pygame.draw.rect(win, (0, 255, 0), (self.x + 15, self.y - 5, health_bar, 10))

    def get_health(self):
        return (self.health)

    def regen_health(self):
        if self.health + self.regenhealth <= self.max_health:
            self.health += self.regenhealth
        else:
            self.health = self.max_health


