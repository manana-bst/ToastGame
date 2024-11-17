from turtle import Screen
import pygame
import os

pygame.init() 

# CREATING CANVAS 
canvas = pygame.display.set_mode((500, 500)) 

# game window settings
width = 300
height = 500
screen_size = (width, height)
pygame.display.set_caption('Car Game')
exit = False

# colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# game settings
gameover = False
speed = 2
score = 0

# sprite
class Vehicle(pygame.sprite.Sprite):
     def __init__(self, image, x, y):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load('graphics/sneaky-toast-walk.gif')
          self.rect = self.image.get_rect()
          self.rect.center = [x,y]

# marker size
marker_width = 10
marker_height = 50

# road and edge markers
road = (100, 0, 300, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# x coordinates of lanes
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# animating movement of lane markers
lane_marker_move_y = 0

# game loop
clock = pygame.time.Clock()
fps = 120
running = True

while running:

    clock.tick(fps)
	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
	        running = False	
    
    # draw grass
    canvas.fill(green)

    # draw road
    pygame.draw.rect(canvas, gray, road)

    # draw edge markers
    pygame.draw.rect(canvas, yellow, left_edge_marker)
    pygame.draw.rect(canvas, yellow, right_edge_marker)

    # draw + animate lane markers
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
         lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
         pygame.draw.rect(canvas, white, (left_lane + 45, y +lane_marker_move_y, marker_width, marker_height))
         pygame.draw.rect(canvas, white, (center_lane+ 45, y + lane_marker_move_y, marker_width, marker_height))

    pygame.display.update()

pygame.quit()


