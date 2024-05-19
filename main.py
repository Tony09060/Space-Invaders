import pygame
from pygame.locals import *

#define fps
clock = pygame.time.Clock()
fps = 60


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Space Invaders')

#load images
bg = pygame.image.load("Images/bg.png")

def drawBg():
    screen.blit(bg, (0, 0))

#create spaceship class(object):
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/spaceShip.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

def update(self):
    #set movement speed
    speed = 8

    #get key press
    key = pygame.key.get_preesed()
    if key[pygame.K_LEFT]:
        self.rect.x -= speed
    if key[pygame.K_RIGHT]:
        self.rect.x += speed

#create sprite groups
spaceship_group = pygame.sprite.Group()

#create player
spaceship = Spaceship(300, 500)
spaceship_group.add(spaceship)

run = True
while run:
    clock.tick(fps)

    #draw

    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update spaceship
    spaceship.update()

    drawBg()

    #draw sprite groups
    spaceship_group.draw(screen)

    pygame.display.update()

pygame.quit()
