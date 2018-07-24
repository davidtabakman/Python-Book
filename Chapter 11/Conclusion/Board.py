# -*- coding: utf-8 -*-
import pygame
from Tile import Tile
from Plane import CrazyPlane


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BACKGROUND_COLOR = WHITE
LINE_COLOR = BLACK


class Board(object):

    def __init__(self, surface, width, height):
        """Create a new board on a surface
        Args:
            surface - a screen on which the painting will comence
            width - number of tiles in a row
            height - number of tiles in a column
        """
        self.__surface = surface
        self.__width = width
        self.__height = height
        #Create a matrix of tiles
        self.__tiles = []
        for x in xrange(0, 10):
            self.__tiles.append([])
            for y in xrange(0, 10):
                self.__tiles[x].append(Tile(x, y))

        screen_width = self.get_surface().get_width()
        screen_height = self.get_surface().get_height()
        self.__delta_x = screen_width / self.__width
        self.__delta_y = screen_height / self.__height

    def get_surface(self):
        return self.__surface

    def get_tiles(self):
        return self.__tiles

    def draw(self):
        """Draws the board on a surface (background, lines and planes)
        """
        #Background color
        self.get_surface().fill(BACKGROUND_COLOR)
        #Draw lines
        screen_width = self.get_surface().get_width()
        screen_height = self.get_surface().get_height()
        delta_x = screen_width / self.__width
        delta_y = screen_height / self.__height

        x = 0
        while x <= screen_width:
            pygame.draw.line(self.get_surface(), LINE_COLOR, (x, 0), (x, screen_height), 1)
            x += delta_x

        y = 0
        while y <= screen_height:
            pygame.draw.line(self.get_surface(), LINE_COLOR, (0, y), (screen_width, y), 1)
            y += delta_y

        for tile in self.get_tiles():
            for tile2 in tile:
                if tile2.get_plane() is not None:
                    try:
                        self.get_surface().blit(tile2.get_plane().get_image(), self.get_tile_coord(tile2))
                    except Exception, e:
                        print "error: failed to draw plane at {} because {}".format(tile2.get_coord(), e)

    def get_tile_coord(self, tile):
        """Gets the coordinates on the surface of a tile
        Args:
            tile - Tuple (x, y) - x is the tile's x coordinate
            y is the tile's y coordinate
        """
        coord = tile.get_coord()

        return coord[0] * self.__delta_x, coord[1] * self.__delta_y

    def add_plane(self, tile=(0, 0)):
        """Adds a new plane at a specific tile (default 0,0)
        """
        plane = CrazyPlane()
        #Reshape the plane to fit one tile
        try:
            plane.set_image(pygame.transform.scale(plane.get_image(), (self.__delta_x, self.__delta_y)))
            self.get_tiles()[tile[0]][tile[1]].set_plane(plane)
        except Exception, e:
            print "error: failed to add plane at {} because: {}".format(tile, e)

