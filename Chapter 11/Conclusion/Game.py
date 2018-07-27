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
board.add_plane((0, 0))
board.add_plane((0, 1))
board.add_plane((0, 2))
board.add_plane((0, 3))
board.add_plane((0, 4))
board.add_plane((0, 5))
board.add_plane((0, 6))
board.add_plane((0, 7))
board.add_plane((0, 8))
board.add_plane((0, 9))

finish = False
score = 0
moves = 0
tries = 0
crashes = 0
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    #Game stuff
    for x in xrange(0, 10):
        for y in xrange(0, 10):
            if not control.get_tile_at_coord((x, y)).get_plane() is None:
                moves += 1
            score += control.control_coord((x, y))
    if moves >= 4000:
        print "score: {}, moves: {}".format(score, moves)
        finish = True
    board.draw()

    #Render
    pygame.display.flip()
    clock.tick(1000)