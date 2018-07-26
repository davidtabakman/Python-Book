# -*- coding: utf-8 -*-
import pygame
from Board import Board
from Control import ControlTower

#Constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

#Craete clock
clock = pygame.time.Clock()


#Create board
board = Board(screen, 10, 10)
control = ControlTower(board.get_tiles())
board.add_plane((0, 1))
control.move_plane_random((0, 1))


finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    #Game stuff
    for x in xrange(0, 10):
        for y in xrange(0, 10):
            control.control_coord((x, y))
    board.draw()

    #Render
    pygame.display.flip()
    clock.tick(60)