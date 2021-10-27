import pygame
img = pygame.transform.scale(pygame.image.load('Rectangle_example.svg.png'), (200, 600))
pygame.font.init()
class Menu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = img
        self.font = pygame.font.SysFont('comicsans', 33)
        self.lenght = self.img.get_width()
        self.high = self.img.get_height()
        self.add = 0


    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def draw_inside(self, win, name, money, speed, health, max_health):
        self.textsurface1 = self.font.render(f"{name}",False, (255, 0, 0))
        self.textsurface2 = self.font.render(f"Health left: {round(health, 2)}",False, (0, 0, 0))
        self.textsurface3 = self.font.render(f"Max Health: {round(max_health, 2)}",False, (0, 0, 0))
        self.textsurface4 = self.font.render(f"Money: {money}",False, (0, 0, 0))
        self.textsurface5 = self.font.render(f"Speed: {speed}",False, (0, 0, 0))

        win.blit(self.textsurface1, (self.x + self.lenght // 2 - self.textsurface1.get_width() // 2, self.y + self.add + self.textsurface1.get_height() * 4))
        self.add += 50
        win.blit(self.textsurface2, (self.x + self.lenght // 2 - self.textsurface2.get_width() // 2, self.y + self.textsurface2.get_height() * 4 + self.add))
        self.add += 50
        win.blit(self.textsurface3, (self.x + self.lenght // 2 - self.textsurface3.get_width() // 2, self.y + self.textsurface3.get_height() * 4 + self.add))
        self.add += 50
        win.blit(self.textsurface4, (self.x + self.lenght // 2 - self.textsurface4.get_width() // 2, self.y + self.textsurface4.get_height() * 4 + self.add))
        self.add += 50
        win.blit(self.textsurface5, (self.x + self.lenght // 2 - self.textsurface5.get_width() // 2, self.y + self.textsurface5.get_height() * 4 + self.add))
        self.add = 0