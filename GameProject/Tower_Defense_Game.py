import pygame
from Enemies import Enemy
from Warrior import Warrior
from Goblin import Goblin
from Red_Goblin import Red_Goblin
from Little_Barbarian import Little_Barbarian
from Towers import Towers
from Archer_Tower import ArcherTower
from Range_Tower import RangeTower
from Damage_Tower import DamageTower
import random
import time




pygame.font.init()
pygame.mixer.init()
music = pygame.mixer.music.load('World of Warcraft - Nightsong - Music HD ツ.wav')
pygame.mixer.music.play(-1)
class Game:
    def __init__(self):
        self.height = 700
        self.width = 1100
        self.base_fps = 60
        self.t = 0
        self.dt = 0
        self.lives = 10
        self.money = 100
        self.level = 0
        self.image_lives = pygame.transform.scale(pygame.image.load('heart.png'), (64, 64))
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.transform.scale(pygame.image.load("Tower-Defense-2D-Game-Kit8.jpg"), (self.width, self.height))
        self.enemies = []
        self.add_health = 0.4
        self.attack_towers = [ArcherTower(530, 330), ArcherTower(450, 130)]
        self.support_towers = [DamageTower(430, 330)]
        self.wavelenght = 0
        self.font = pygame.font.SysFont('comicsans', 95)
        self.array = []
        self.timer = time.time()
        self.count = 0
        self.score = 0
        self.bonus = False
        self.health_bar = False
        self.go = False

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            if time.time() - self.timer > 2:
                if self.count < self.wavelenght:
                    self.timer = time.time()
                    self.enemies.append(random.choice([Goblin(), Red_Goblin(), Warrior(), Little_Barbarian()]))
                    self.count += 1
                else:
                    if len(self.enemies) == 0:
                        self.count = 0
                        self.level += 1
                        self.wavelenght += 5
                        Enemy.add_healtha += self.add_health
                        print(self.level, self.wavelenght)
            self.textsurface = self.font.render(f"{self.lives}", False, (255, 255, 255))
            self.textscore = self.font.render(f"{self.score}", False, (255, 0, 0))
            self.dt = clock.tick(
                self.base_fps)  # dt (delta time), the duration of the last frame, usually not less than 1/fps seconds
            self.t += self.dt
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.array.append(pygame.mouse.get_pos())
                    for tw in self.attack_towers:
                        tw.selected(pygame.mouse.get_pos())
                    for tw in self.support_towers:
                        tw.selected(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.health_bar:
                            self.go = True
                            self.health_bar = True
                        else:
                            self.go = False
                            self.health_bar = False


                        '''if not self.bonus and self.score >= 10:
                            for enemy in self.enemies[:]:
                                enemy.health -= 3
                            self.bonus = True
                        else:
                            for enemy in self.enemies[:]:
                                enemy.health -= 0.2'''
            if self.lives <= 0:
                print("Hai perso!")
                run = False
            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.textsurface, (self.width - self.textsurface.get_width() - self.image_lives.get_width() - 10, self.textsurface.get_height()/10))
        self.win.blit(self.textscore, (self.textscore.get_width() / 2, self.textscore.get_height() / 4))
        self.win.blit(self.image_lives, (self.width - self.image_lives.get_width() - 5, 2))
        '''for element in self.array:
            pygame.draw.circle(self.win, (200, 100, 100), element, 10)'''
        for enemy in self.enemies[:]:
            enemy.draw(self.win)
            if self.go:
                enemy.draw_health_bar(self.win)
            enemy.move(self.dt)
            if enemy.get_health() <= 0:
                self.enemies.remove(enemy)
                self.score += 1
            if enemy.x + enemy.get_width() > self.width:
                self.enemies.remove(enemy)
                self.lives -= enemy.subtract_lives
        for tw in self.attack_towers:
            tw.draw(self.win)
            tw.inrange(self.enemies)
        for tw in self.support_towers:
            tw.draw(self.win)
            tw.inrange(set(self.attack_towers))

        pygame.display.update()

g = Game()
g.run()