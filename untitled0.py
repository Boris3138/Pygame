# -*- coding: utf-8 -*-
import pygame
import random

WIDTH = 700
HEIGHT = 800
FPS = 60

GREY = (50, 54, 61)
WINDOW = (0, 230, 255)
UPP = (128, 0, 0)
TR = (120, 80, 50)
EE = (21, 144, 51)
FLOOR = (80, 90, 100)
BLUE = (0, 200, 255)
WHITE = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (160, 100, 80)
GREEN = (102, 255, 0)
BROWN1 = (101, 67, 33)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Burger")
clock = pygame.time.Clock()

class Toast(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 20))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 20))
        self.image.fill(random.choice([WHITE, GREEN, BROWN1, RED]))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(3, 6)
        self.speedx = random.randrange(0, 1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speedy = random.randrange(3, 6)
            
mobs = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Toast()
all_sprites.add(player)
for i in range(7):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    
    # new = pygame.sprite.groupcollide(mobs, player, True, True)
    # for i in new:
        # m = Mob()
        # all_sprites.add(m)
        # mobs.add(m)
    
    # new = pygame.sprite.groupcollide(mobs, player, False)
    # if new:
        # pygame.union_ip(player, mobs)
        
    screen.fill(BLUE)
    pygame.draw.rect(screen, FLOOR, (0, 700, 700, 100))
    pygame.draw.rect(screen, GREY, (0, 200, 200, 500))
    pygame.draw.rect(screen, GREY, (250, 100, 200, 600))
    pygame.draw.rect(screen, GREY, (500, 300, 200, 400))
    pygame.draw.rect(screen, WINDOW, (60, 300, 75, 75))
    pygame.draw.rect(screen, WINDOW, (60, 450, 75, 75))
    pygame.draw.rect(screen, WINDOW, (315, 200, 75, 75))
    pygame.draw.rect(screen, WINDOW, (315, 350, 75, 75))
    pygame.draw.rect(screen, WINDOW, (315, 500, 75, 75))
    pygame.draw.rect(screen, WINDOW, (569, 400, 75, 75))
    pygame.draw.rect(screen, WINDOW, (569, 550, 75, 75))
    pygame.draw.rect(screen, TR, (100, 650, 35, 90))
    pygame.draw.rect(screen, TR, (250, 650, 35, 90))
    pygame.draw.rect(screen, TR, (450, 650, 35, 90))
    pygame.draw.rect(screen, TR, (600, 650, 35, 90))
    pygame.draw.circle(screen, EE, [117, 600], 60)
    pygame.draw.circle(screen, EE, [267, 600], 60)
    pygame.draw.circle(screen, EE, [467, 600], 60)
    pygame.draw.circle(screen, EE, [617, 600], 60)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()