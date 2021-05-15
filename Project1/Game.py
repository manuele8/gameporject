import pygame
import random
import time
import os

pygame.font.init()

# Set Height and Length and Create Window
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame game")

# Load Ship Images
RED_SHIP_IMAGE = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SHIP_IMAGE = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SHIP_IMAGE = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
YELLOW_SHIP_IMAGE = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
# Load Laser Images
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
# Load Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


# Classes
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height  and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Ship:
    COOLDOWN = 30
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_image, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)



    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1


    def get_width(self):
        return self.ship_image.get_width()

    def get_height(self):
        return self.ship_image.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_image, self.laser_image = YELLOW_SHIP_IMAGE, YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_image.get_height() + 10))
        pygame.draw.rect(window, (255, 0, 0), (self.)






class Enemy(Ship):
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        COLOR_MAP = {
            "red": (RED_SHIP_IMAGE, RED_LASER),
            "green": (GREEN_SHIP_IMAGE, GREEN_LASER),
            "blue": (BLUE_SHIP_IMAGE, BLUE_LASER)
        }
        self.ship_image, self.laser_image = COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_image)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 20, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    run = True
    FPS = 100
    main_font = pygame.font.SysFont("comicsans.ttf", 50)
    lost_font = pygame.font.SysFont("comicsans.ttf", 60)
    clock = pygame.time.Clock()
    player = Player(300, 650)
    player_vel = 5
    laser_vel = 4
    level = 0
    lives = 5
    wave_length = 5
    enemy_vel = 1
    enemies = []
    lost = False
    lost_count = 0



    def redraw_window():
        WIN.blit(BG, (0, 0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)
        player.draw(WIN)
        if lost:
            lost_label = lost_font.render("You lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (int(WIDTH/2 - lost_label.get_width()/2), 350))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                              random.choice(["red", "green", "blue"]))
                enemies.append(enemy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2 * FPS) == 1:
                enemy.shoot()
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)



        player.move_lasers(-laser_vel, enemies)


main()







