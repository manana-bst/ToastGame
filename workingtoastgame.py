import pygame
import random

pygame.init() 

canvas = pygame.display.set_mode((500, 500)) 

# game window settings
width = 300
height = 500
screen_size = (width, height)
pygame.display.set_caption('Car Game')
exit = False

# colors
gray = (105, 105, 105)
green = (129, 199, 129)
red = (200, 0, 0)
white = (240, 240, 240)
yellow = (247, 181, 82)

# sprite settings
frame_files = ['sneaky-toast-walk-1.png', 'sneaky-toast-walk-2.png', 'sneaky-toast-walk-3.png', 'sneaky-toast-walk-4.png', 'sneaky-toast-walk-5.png', 'sneaky-toast-walk-6.png', 'sneaky-toast-walk-7.png', 'sneaky-toast-walk-8.png']  # List of frame file paths
frames = [pygame.image.load(frame) for frame in frame_files]

frame_index = 0
frame_delay = 100
last_update = pygame.time.get_ticks()

player_rect = frames[frame_index].get_rect()
player_rect.center = (250, 350)

# obstacle settings
obstacle_image = pygame.image.load('toaster.png')
obstacle_image = pygame.transform.scale(obstacle_image, (50, 50))
obstacle_rect = obstacle_image.get_rect() 
obstacle_rect.center = (random.choice([150, 250, 350]), -50)

# player speed settings
player_speed = 10
     
# game settings
gameover = False
speed = 2
score = 0

# marker size
marker_width = 10
marker_height = 50

# road + edge markers
road = (100, 0, 300, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# x coordinates of lanes
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# lane markers animation settings
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
             
    # player control key settings
    keys = pygame.key.get_pressed()

    # ! hold left / right arrow keys to change lanes, hold nothing to stay centered
    if keys[pygame.K_LEFT] and player_rect.left > left_lane:
         player_rect.center = (left_lane, player_rect.center[1])
    if keys[pygame.K_RIGHT] and player_rect.right < right_lane:
         player_rect.center = (right_lane, player_rect.center[1])
    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
         player_rect.center = (center_lane, player_rect.center[1])
             
    # sprite animation settings
    current_time = pygame.time.get_ticks()
    if current_time - last_update > frame_delay:
        frame_index = (frame_index + 1) % len(frames)
        last_update = current_time 

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

    # obstacle
    obstacle_rect.y += speed
    if obstacle_rect.top > height:
         obstacle_rect.center = (random.choice([150, 250, 350]), -50)
    
    if player_rect.colliderect(obstacle_rect):
         print("Game Over!")
         running = False

    # draw sprite
    canvas.blit(frames[frame_index], player_rect)

    # draw obstacle
    canvas.blit(obstacle_image, obstacle_rect)

    pygame.display.update()

pygame.quit()