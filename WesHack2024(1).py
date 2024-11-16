import pygame
from sys import exit
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((500,550))
pygame.display.set_caption('Taxi Taxi')


    #Images
sky_surface = pygame.image.load('Graphics/PinkSky.jfif')
ground_img = pygame.image.load('Graphics/Road.jpg')

    #Defined Variables
ground_scroll = 0
scroll_speed = 4

class Toast(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Graphics/sneaky-toast-walk.gif')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

toast_group = pygame.sprite.Group()
Burnet = Toast(50, int(500/2))
toast_group.add(Burnet)


run = True
while run:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(sky_surface,(0, 0))

    toast_group.draw(screen)

    screen.blit(ground_img,(ground_scroll, 240))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    toast_group.draw(screen)

    pygame.display.update()

pygame.quit()

