import random
import math
import pygame
from pygame import mixer



# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("Space.png")

# Background Sound
mixer.music.load("background.wav")
mixer.music.play(-1)


# Icon and Title
pygame.display.set_caption("Candy Super-Candy")
icon = pygame.image.load("candy.png")
pygame.display.set_icon(icon)

# Player Image
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy Image
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
wave_lenght = 18
enemyX_position = 100
enemyY_position = 50
count = 0


for i in range(wave_lenght):
    enemyImg.append(pygame.image.load("cartoon.png"))
    enemyX.append(enemyX_position)
    enemyY.append(enemyY_position)
    enemyX_change.append(1)
    enemyY_change.append(40)
    enemyX_position = enemyX_position + 65
    count += 1
    if count == 6:
        enemyY_position += 70
        enemyX_position = 100
        count = 0


# Bullet Image
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
testX = 10
testY = 10

# Game Over Text
over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))



def player(x, y):
    screen.blit(playerImg, (x, y))


def Enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((255, 165, 0))

    # Background Image
    screen.blit(background, (0, 0))

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
                    bulletX = playerX
                    bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player Movement
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    player(playerX, playerY)
    show_score(testX, testY)

    # Enemy Movement
    for i in range (wave_lenght):

        # Game Over
        if enemyY[i] > 410:
            for j in range (wave_lenght):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            for j in range(wave_lenght):
                enemyX_change[j] = 1
                enemyY[j] += enemyY_change[j]
        elif enemyX[i] > 736:
            for j in range(wave_lenght):
                enemyX_change[j] = -1
                enemyY[j] += enemyY_change[i]
        # Collisione
        collisione = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collisione:
            esplosione_sound = mixer.Sound("explosion.wav")
            esplosione_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 734)
            enemyY[i] = random.randint(50, 150)
        Enemy(enemyX[i], enemyY[i], i)


    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    pygame.display.update()











































