# -*- coding: utf-8 -*-
import pygame
import math

#Constants
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 580
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
IMAGE = 'tyler1.jpg'
REFRESH_RATE = 60
CENTER = [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2]
RADIUS = 30

#Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

#Load Image
img = pygame.image.load(IMAGE)

#Timer
clock = pygame.time.Clock()

#Create ball
ball_pos = CENTER
ball_velocity = [10, 10]


#Ball collision check
def collision_check():
    """Checks if the ball collides with the screen borders.
    Changes the speed accordingly
    """
    if ball_pos[0] + RADIUS >= WINDOW_WIDTH:
        ball_velocity[0] *= -1
    elif ball_pos[0] - RADIUS <= 0:
        ball_velocity[0] *= -1
    if ball_pos[1] + RADIUS >= WINDOW_HEIGHT:
        ball_velocity[1] *= -1
    elif ball_pos[1] - RADIUS <= 0:
        ball_velocity[1] *= -1


finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    screen.fill(BLACK)
    screen.blit(img, (0, 0))
    # update ball's position
    collision_check()
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    pygame.draw.circle(screen, WHITE, ball_pos, RADIUS)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)
pygame.quit()