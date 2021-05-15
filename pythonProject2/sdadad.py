import pygame
import time
from sad import Navicella
WIDTH, HEIGHT = 800, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Navicelle")

#immagini

def main():
    def drawwindow():
        pygame.display.update()
    loop = True
    FPS = 60
    clock = pygame.time.Clock()
    while loop:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        drawwindow()

main()
