# -*- coding: utf-8 -*-
import random


def get_adjacent_tiles(coord):
    possible_x = []
    possible_y = []
    if coord[0] == 0:
        possible_x.append(0)
        possible_x.append(1)
    elif coord[0] == 9:
        possible_x.append(8)
        possible_x.append(9)
    else:
        possible_x.append(coord[0] - 1)
        possible_x.append(coord[0])
        possible_x.append(coord[0] + 1)

    if coord[1] == 0:
        possible_y.append(0)
        possible_y.append(1)
    elif coord[1] == 9:
        possible_y.append(8)
        possible_y.append(9)
    else:
        possible_y.append(coord[1] - 1)
        possible_y.append(coord[1])
        possible_y.append(coord[1] + 1)

    possible_coord = []
    for x in possible_x:
        for y in possible_y:
            if not (x, y) == coord:
                possible_coord.append((x, y))

    return possible_coord


class ControlTower(object):

    def __init__(self, tiles):
        self.__tiles = tiles

    def get_tiles(self):
        return self.__tiles

    def get_tile_at_coord(self, coord):
        return self.get_tiles()[coord[0]][coord[1]]

    def move_plane(self, coord_from, coord_to):
        """Moves a plane from a tile to another tile.
        If there is a plane on coord_from, doesn't move
        If there is no plane on coord_to, doesn't move
        """
        try:
            first_tile = self.get_tile_at_coord(coord_from)
            second_tile = self.get_tile_at_coord(coord_to)
            if first_tile.get_plane() is not None:
                if second_tile.get_plane() is None:
                    second_tile.set_plane(first_tile.get_plane())
                    first_tile.set_plane(None)
        except IndexError:
            print "error: failed to move plane from {} to {} because: one of the tiles is out of the " \
                  "board".format(coord_from, coord_to)
        except Exception, e:
            print "error: failed to move plane from {} to {} because: {}".format(coord_from, coord_to, e)

    def move_plane_random(self, coord_from):
        try:
            adjacent_tiles = get_adjacent_tiles(coord_from)
            self.move_plane(coord_from, adjacent_tiles[random.randint(0, len(adjacent_tiles) - 1)])
        except IndexError:
            print "error: failed to move plane from {} because: the tile is out of the board".format(coord_from)
        except Exception, e:
            print "error: failed to move plane from {} because: {}".format(coord_from, e)

    def get_adjacent_planes(self, coord):
        """Lists all adjacent planes coordinates to a plane at a coordinate
        Return Value:
            Empty list if no adjacent planes found or there is no plane at the given coordinate
            List of adjacent planes coordinates if there are any
        """
        try:
            adjacent_planes = []
            #Check adjacent tiles
            for coord in get_adjacent_tiles(coord):
                if not self.get_tile_at_coord(coord).get_plane() is None:
                    adjacent_planes.append(coord)
            return adjacent_planes
        except Exception, e:
            print "error checking intervention at {} because {}".format(coord, e)
            return []

    def move_plane_algorithm(self, coord):
        adjacent_planes = self.get_adjacent_planes(coord)
        adjacent_tiles = get_adjacent_tiles(coord)
        possible_coord = []
        for tile in adjacent_tiles:
            if not adjacent_planes.count(tile) > 0 and not tile == coord:
                possible_coord.append(tile)
        possible_coord.sort(key=self.coord_priority)
        coord_to = possible_coord[0]

        self.move_plane(coord, coord_to)

    def coord_priority(self, coord):
        return len(self.get_adjacent_planes(coord)) / float(len(get_adjacent_tiles(coord)))

    def control_coord(self, coord):
        """Checks if a specific coordinate needs intervention, if yes applies algorithm
        if not moves randomly
        Return value:
            1 if move was random
            0 if algorithm was applied
        """
        if self.get_tile_at_coord(coord).get_plane() is None:
            return 0
        if len(self.get_adjacent_planes(coord)) == 0:
            self.move_plane_random(coord)
            return 1
        else:
            self.move_plane_algorithm(coord)
            return 0


