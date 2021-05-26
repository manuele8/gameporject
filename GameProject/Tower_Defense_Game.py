import pygame
from Enemies import Enemy
from Warrior import Warrior
from Goblin import Goblin
from Red_Goblin import Red_Goblin
from Little_Barbarian import Little_Barbarian
from Boss_Ice_Golem import Boss_Ice_Golem
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
        self.image_lives = pygame.transform.scale(pygame.image.load('hearts.png'), (38, 38))
        self.image_money = pygame.image.load('coins.png')
        self.image_pause = pygame.transform.scale(pygame.image.load('button_30_red.png'), (50, 52))
        self.image_play = pygame.transform.scale(pygame.image.load('button_21_red.png'), (50, 52))
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.transform.scale(pygame.image.load("Tower-Defense-2D-Game-Kit8.jpg"), (self.width, self.height))
        self.enemies = []
        self.add_health = 0.4
        self.attack_towers = [ArcherTower(530, 330), ArcherTower(450, 130)]
        self.support_towers = [DamageTower(550, 130)]
        self.wavelenght = 0
        self.font = pygame.font.SysFont('comicsans', 60)
        self.array = []
        self.array2 = []
        self.timer = time.time()
        self.count = 0
        self.score = 0
        self.boss_count = 1
        self.pos = (self.width**2, self.height ** 2)
        self.bonus = False
        self.health_bar = False
        self.go = False
        self.paused = False
        
    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            #print(self.paused)
            if not self.paused:
                if time.time() - self.timer > random.randrange(10, 20) / 10:
                    if self.level % 5 == 0 and self.level != 0 and self.count < self.boss_count:
                        self.timer = time.time()
                        self.enemies.append(Boss_Ice_Golem())
                        if self.level != 5:
                            self.add_health_enemies()
                        self.count += 1
                    elif (self.level % 5 != 0 or self.level == 0) and self.count < self.wavelenght:
                        self.timer = time.time()
                        self.enemies.append(random.choice([Goblin(), Red_Goblin(), Warrior(), Little_Barbarian()]))
                        if self.level % 5 == 1 and self.level != 1:
                            self.add_health_enemies()
                        self.count += 1
                    else:
                        if len(self.enemies) == 0:
                            self.array2 = []
                            self.count = 0
                            self.level += 1
                            if not self.level % 5 == 0:
                                self.wavelenght += 3
                            print(self.level, self.wavelenght)
            self.textsurface = self.font.render(f"{self.lives}", False, (255, 255, 255))
            self.textscore = self.font.render(f"{self.score}", False, (255, 0, 0))
            self.textmoney = self.font.render(f"{self.money}", False, (255, 255, 255))
            self.dt = clock.tick(
                self.base_fps)  # dt (delta time), the duration of the last frame, usually not less than 1/fps seconds
            self.t += self.dt
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            if not self.paused:
                                self.paused = True
                            else:
                                self.paused = False
                            break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                if not self.paused:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.array.append(pygame.mouse.get_pos())
                        for tw in self.attack_towers:
                            tw.selected(pygame.mouse.get_pos())
                        for tw in self.support_towers:
                            tw.selected(pygame.mouse.get_pos())
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            self.enemies = []
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
            self.pause(self.pos)
            self.play(self.pos)
            if self.lives <= 0:
                print("Hai perso!")
                run = False
            self.draw()

        pygame.quit()

    def pause(self, tuple):
        if not self.paused:
            if tuple[0] <= self.width - 5 and tuple[0] >= (self.width - self.image_pause.get_width() - 5):
                if tuple[1] <= 5 + self.image_pause.get_height() and tuple[1] >= 5:
                    self.paused = True
                    self.pos = (self.width ** 2, self.height ** 2)

    def add_health_enemies(self):
        last_element = self.enemies[len(self.enemies) - 1]
        self.array2.append(last_element.name)
        if self.array2.count(last_element.name) == 1:
            last_element.class_maxhp_add(self.level)
        elif self.array2.count(last_element.name) > 1:
            last_element.max_health = last_element.maxhealth
            last_element.health = last_element.max_health
        print(last_element.name + ": ", last_element.maxhealth, last_element.max_health, last_element.health,
              last_element.original_health)

    def play(self, tuple):
        if self.paused:
            if tuple[0] <= self.width - 5 - self.image_pause.get_width() - 10 and tuple[0] >= self.width - self.image_play.get_width() - 5 - self.image_pause.get_width() - 10:
                if tuple[1] <= 5 + self.image_pause.get_height() and tuple[1] >= 5:
                    self.paused = False
                    self.pos = (self.width ** 2, self.height ** 2)
    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.textsurface, (17 + self.image_lives.get_width(), 9))
        #self.win.blit(self.textscore, (self.textscore.get_width() / 2, self.textscore.get_height() / 4))
        self.win.blit(self.textmoney, (17 + self.image_lives.get_width(), 17 + self.image_lives.get_height()))
        self.win.blit(self.image_lives, (10, 10))
        self.win.blit(self.image_money, (15, 20 + self.image_lives.get_height()))
        self.win.blit(self.image_pause, (self.width - self.image_pause.get_width() - 5, 5))
        self.win.blit(self.image_play, (self.width - self.image_play.get_width() - 5 - self.image_pause.get_width() - 10, 5))
        #for element in self.array:
            #pygame.draw.circle(self.win, (200, 100, 100), element, 10)
        for enemy in self.enemies[:]:
            enemy.draw(self.win)
            if self.go:
                enemy.draw_health_bar(self.win)
            if not self.paused:
                enemy.move(self.dt)
            if enemy.get_health() <= 0:
                self.enemies.remove(enemy)
                self.money += enemy.money
                self.score += 1
            if enemy.x + enemy.get_width() > self.width:
                self.enemies.remove(enemy)
                self.lives -= enemy.subtract_lives
        for tw in self.attack_towers:
            tw.draw(self.win)
            if not self.paused:
                tw.inrange(self.enemies)
        for tw in self.support_towers:
            tw.draw(self.win)
            if not self.paused:
                tw.inrange(self.attack_towers)

        pygame.display.update()

g = Game()
g.run()