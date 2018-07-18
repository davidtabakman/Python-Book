# -*- coding: utf-8 -*-
import pygame

MOVING_IMAGE = "ball.png"
GREEN = (0, 255, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y, vx=0, vy=0):
        super(Ball, self).__init__()
        self.image = pygame.image.load(MOVING_IMAGE).convert()
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = vx
        self.__vy = vy

    def update_v(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    def update_loc(self):
        self.rect.x += self.__vx
        self.rect.y += self.__vy

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self.__vx, self.__vy