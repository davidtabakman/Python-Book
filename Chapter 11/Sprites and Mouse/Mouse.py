# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
import pygame
import math

#Constants
LEFT = 1
SCROLL = 2
RIGHT = 3
WINDOW_WIDTH = 612
WINDOW_HEIGHT = 408
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BACKGROUND = "sky_background.jpg"
SPRITE = "plane.png"
CENTER = [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2]

#Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

#Load images
bg = pygame.image.load(BACKGROUND)
screen.blit(bg, (0, 0))
player_image = pygame.image.load(SPRITE).convert()
player_image.set_colorkey(GREEN)
pygame.display.flip()

#Clock
clock = pygame.time.Clock()

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            screen.blit(player_image, pygame.mouse.get_pos())

    pygame.display.flip()
    clock.tick(60)



pygame.quit()
