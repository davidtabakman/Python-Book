# -*- coding: utf-8 -*-
import pygame
from Board import Board

#Constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
IMAGE = 'tyler1.jpg'

#Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

#Craete clock
clock = pygame.time.Clock()

#Create board
board = Board(screen, 10, 10)
board.add_plane((1, 10))

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    #Game stuff
    board.draw()

    #Render
    pygame.display.flip()
    clock.tick()