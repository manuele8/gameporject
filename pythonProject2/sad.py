import pygame

player_image = None
p_laser_image = None
enemy_image = None
e_laser_image = None
boss_image = None
b_laser_image = None

class Navicella:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ship_image = None
        self.laser_image = None
        self.lasers = []
        self.count_down = 0

    def draw(self, win):
        win.blit(self.ship_image, (self.x, self.y))

    def prendi_altezza(self):
        return self.ship_image.get_width()

    def prendi_lunghezza(self):
        return self.ship_image.get_height()

class Giocatore(Navicella):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_image = player_image
        self.laser_image = p_laser_image

class Nemico(Navicella):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hits = 0
        self.ship_image = enemy_image
        self.laser_image = e_laser_image

class Boss(Nemico):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y)
        self.ship_image = boss_image
        self.laser_image = b_laser_image
        self.max_health = health



