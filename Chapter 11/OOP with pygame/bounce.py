# -*- coding: utf-8 -*-
from shapes import Ball
import pygame
import random

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
CENTER = [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2]
REFRESH_RATE = 60

#Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

#Load images
bg = pygame.image.load(BACKGROUND)
screen.blit(bg, (0, 0))
pygame.display.flip()

#Clock
clock = pygame.time.Clock()

#Init sprites
balls_list = pygame.sprite.Group()


#Ball collision check
def collision_check(ball):
    """Checks if the ball collides with the screen borders.
    Changes the speed accordingly
    """
    if ball.get_pos()[0] + ball.rect.width >= WINDOW_WIDTH:
        ball.update_v(ball.get_v()[0] * -1, ball.get_v()[1])
    elif ball.get_pos()[0] <= 0:
        ball.update_v(ball.get_v()[0] * -1, ball.get_v()[1])
    if ball.get_pos()[1] + ball.rect.height >= WINDOW_HEIGHT:
        ball.update_v(ball.get_v()[0], ball.get_v()[1] * -1)
    elif ball.get_pos()[1] <= 0:
        ball.update_v(ball.get_v()[0], ball.get_v()[1] * -1)


finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT:
                x, y = pygame.mouse.get_pos()
                vx = random.randint(-3, 3)
                vy = random.randint(-3, 3)
                ball = Ball(x, y, vx, vy)
                balls_list.add(ball)
    screen.blit(bg, (0, 0))
    for ball in balls_list:
        collision_check(ball)
        ball.update_loc()
    balls_list.draw(screen)

    pygame.display.flip()
    clock.tick(REFRESH_RATE)

pygame.quit()