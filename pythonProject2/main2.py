import pygame
import random
import os
import time
from pygame import mixer
import math




pygame.init()

lunghezza, altezza = 800, 600

# Background Sound


screen = pygame.display.set_mode((lunghezza, altezza))

background = pygame.transform.scale(pygame.image.load("Space.png"), (lunghezza, altezza))
background_menu = pygame.transform.scale(pygame.image.load("summoning_by_jaygraphixx_dcvokto-fullview.png"), (lunghezza, altezza))

pygame.display.set_caption("The Last Angel")
icon = pygame.image.load("angel.png")
pygame.display.set_icon(icon)




font_2 = "TheDevilNet-evKx.ttf"

# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

playerImg = pygame.image.load("spaceship.png")
laserImg = pygame.image.load("bomb.png")
enemyImg = pygame.image.load("cartoon.png")
bulletImg = pygame.image.load("bullet.png")
font = pygame.font.Font("freesansbold.ttf", 32)
bullet_state = "ready"
score_value = 0
lives = 3



class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def collision(self, obj):
        return collide(self, obj)


class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ship_img = None
        self.laser_img = None
        self.lasers = []



    def draw(self):
        screen.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw()

    def move_lasers(self, vel, obj):
        for laser in self.lasers:
            laser.move(vel)
            if laser.y <= 0:
                self.lasers.remove(laser)
            elif laser.collision(obj):
                global lives
                lives -= 1
                self.lasers.remove(laser)


class Player(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img = playerImg
        self.laser_img = bulletImg

    def move_lasers(self, vel, objs):
        for laser in self.lasers:
            laser.move(vel)
            if laser.y <= 0:
                self.lasers.remove(laser)
                global bullet_state
                bullet_state = "ready"
            else:
                for obj in objs:
                    if laser.collision(obj):
                        esplosione_sound = mixer.Sound("explosion.wav")
                        esplosione_sound.play()
                        objs.remove(obj)
                        self.lasers.remove(laser)
                        bullet_state = "ready"
                        global score_value
                        score_value += 1
    def shoot(self):
        global bullet_state
        bullet_state = "fire"
        laser = Laser(self.x + 16, self.y - 20, self.laser_img)
        self.lasers.append(laser)

class Enemy(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img = enemyImg
        self.laser_img = laserImg

    def shoot(self):
        laser = Laser(self.x , self.y, self.laser_img)
        self.lasers.append(laser)


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def collide(obj1, obj2):
    distance = math.sqrt(math.pow(obj1.x - obj2.x, 2) + math.pow(obj1.y - obj2.y, 2))
    if distance < 27:
        return True
    else:
        return False

def game_over(enemies):
    for i in range(len(enemies)):
        if enemies[i].y > 410:
            return True
        else:
            return False

def game_over_display(text):
    lost_label = pygame.font.SysFont("comicsans", 60).render(text, 1, (255, 255, 255))
    screen.blit(lost_label, (200, 270))
    pygame.display.update()
    time.sleep(2)
    main_menu()
 






def main():
    mixer.music.load("background.wav")
    mixer.music.play(-1)
    player = Player(370, 480)
    running = True
    FPS = 300
    clock = pygame.time.Clock()

    testX = 10
    testY = 10

    enemies = []
    wave_lenght = 0
    enemyY_position = 50
    enemyX_change = 1
    enemyY_change = 40
    lives = 3

    laser_vel = 4

    level = 0
    main_font = pygame.font.SysFont("comicsans", 50)


    playerX_change = 0


    while running:
        clock.tick(FPS)

        screen.blit(background, (0, 0))
        show_score(testX, testY)
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        screen.blit(lives_label, (650, 10))
        screen.blit(level_label, (330, 10))




        if len(enemies) == 0:
            level += 1
            wave_lenght += 1
            enemyX_position = 100
            enemyX_change = 1
            for i in range(wave_lenght):
                enemy = Enemy(enemyX_position, enemyY_position)
                enemies.append(enemy)
                enemyX_position = enemyX_position + 65

        for enemy in enemies:
            enemy.draw()

        player.draw()

        for i in range(len(enemies)):
            enemies[i].x += enemyX_change
            if enemies[i].x <= 0:
                for j in range(len(enemies)):
                    enemyX_change = 1
                    enemies[j].y += enemyY_change
            elif enemies[i].x > 736:
                for j in range(len(enemies)):
                    enemyX_change = -1
                    enemies[j].y += enemyY_change





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -3
                if event.key == pygame.K_RIGHT:
                    playerX_change = 3
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound("laser.wav")
                        bullet_sound.play()
                        player.shoot()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0



        for enemy in enemies[:]:
            enemy.move_lasers(laser_vel, player)
            if random.randrange(0 , 2*FPS)== 1:
                enemy.shoot()


        player.move_lasers(-laser_vel, enemies)

        player.x += playerX_change
        if player.x < 0:
            player.x = 0
        elif player.x > 736:
            player.x = 736
        if lives <= 0 or game_over(enemies):
            game_over_display("GAME OVER")




        pygame.display.update()

def main_menu():
    mixer.music.load("wow.wav")
    mixer.music.play(-1)
    menu = True
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        main()
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.blit(background_menu, (0, 0))
        title=text_format("The  Last Angel", font_2, 60, yellow)
        if selected=="start":
            text_start=text_format("START", font_2, 50, white)
        else:
            text_start = text_format("START", font_2, 50, red)
        if selected=="quit":
            text_quit = text_format("QUIT", font_2, 50, white)
        else:
            text_quit = text_format("QUIT", font_2, 50, red)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (140, 55))
        screen.blit(text_start, (310, 220))
        screen.blit(text_quit, (330, 300))
        pygame.display.update()

#Initialize the Game
main_menu()
pygame.quit()
quit()










