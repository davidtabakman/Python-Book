# -*- coding: utf-8 -*-
import pygame
from Plane import CrazyPlane


class Tile(object):

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__plane = None

    def get_coord(self):
        return self.__x, self.__y

    def set_plane(self, plane):
        self.__plane = plane

    def get_plane(self):
        return self.__plane

