# -*- coding: utf-8 -*-
import pygame

PLANE_IMAGE = "plane.png"
GREEN = (0, 255, 0)


class CrazyPlane():

    def __init__(self):
        self.__image = pygame.image.load(PLANE_IMAGE).convert()
        self.__image.set_colorkey(GREEN)

    def get_image(self):
        return self.__image

    def set_image(self, image):
        self.__image = image
