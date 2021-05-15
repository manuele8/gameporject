import pygame
from pygame import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]




# Load Images
Pikachu_img = pygame.image.load("pikachu.png")




class Pokemon:
    def __init__(self, x, y, level, health, img):
        self.x = x
        self.y = y
        self.level = level
        self.health = health
        self.img = img

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))



def main():
    run = True
    fullscreen = False
    pokemon_1 = Pokemon(300, 400, 1, 100, Pikachu_img)
    def redraw_window():
        global screen
        pokemon_1.draw(screen)
        pygame.display.update()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)




        redraw_window()
main()




