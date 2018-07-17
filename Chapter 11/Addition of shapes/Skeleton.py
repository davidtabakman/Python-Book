# -*- coding: utf-8 -*-
import pygame
import math

#Constants
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
IMAGE = 'tyler1.jpg'

#Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

#Fill screen and show
img = pygame.image.load(IMAGE)
screen.blit(img, (0, 0))
pygame.display.flip()


#Exercise 1
def draw_lines_circle(surface):
    """ Draws 100 lines of the length of 350 from the center of the screen in a circle
    """
    center = [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2]
    #delta - angle between every line and the next one
    delta = math.pi / 50
    curr_angle = 0
    while curr_angle < math.pi * 2:
        to_point_x = center[0] + (350 * math.cos(curr_angle))
        to_point_y = center[1] + (350 * math.sin(curr_angle))
        to_point = (to_point_x, to_point_y)
        pygame.draw.line(surface, RED, center, to_point, 1)
        curr_angle += delta
    pygame.display.flip()


#draw_lines_circle(screen)


#Exercise 2
pygame.draw.circle(screen, WHITE, (100, 100), 10)
pygame.display.flip()


finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

pygame.quit()