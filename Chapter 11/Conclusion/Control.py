# -*- coding: utf-8 -*-
import random

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
            coord_to_x = coord_from[0]
            coord_to_y = coord_from[1]
            if coord_to_x == 0:
                coord_to_x += random.randrange(0, 2, 1)
            elif coord_to_x == 9:
                coord_to_x -= random.randrange(0, 2, 1)
            else:
                coord_to_x += random.randrange(-1, 2, 1)
            if coord_to_y == 0:
                if coord_to_x == coord_from[0]:
                    coord_to_y += 1
                else:
                    coord_to_y += random.randrange(0, 2, 1)
            elif coord_to_y == 9:
                if coord_to_x == coord_from[0]:
                    coord_to_y -= 1
                else:
                    coord_to_y -= random.randrange(0, 2, 1)
            else:
                if coord_to_x == coord_from[0]:
                    coord_to_y += random.randrange(-1, 2, 2)
                else:
                    coord_to_y += random.randrange(-1, 2, 1)

            self.move_plane(coord_from, (coord_to_x, coord_to_y))
        except IndexError:
            print "error: failed to move plane from {} because: the tile is out of the board".format(coord_from)
        except Exception, e:
            print "error: failed to move plane from {} because: {}".format(coord_from, e)

    def intervention_required(self, coord):
        """Checks if an intervention is required at a specific coordinate on the board
        Return Value:
            True if there are two planes adjacent
            False if not
        """
        try:
            center_tile = self.get_tile_at_coord(coord)
            if center_tile.get_plane() is None:
                return False
            #Check adjacent tiles
            from_x = coord[0] - 1
            to_x = coord[0] + 2
            if coord[0] == 0:
                from_x += 1
            elif coord[0] == 9:
                to_x -= 1
            from_y = coord[1] - 1
            to_y = coord[1] + 2
            if coord[1] == 0:
                from_y += 1
            elif coord[1] == 9:
                to_y -= 1
            #Upper tiles
            if not coord[1] == 0:
                for x in xrange(from_x, to_x):
                    if self.get_tile_at_coord((x, from_y)).get_plane() is not None:
                        return True
            #Side tiles
            if not coord[0] == 0:
                if self.get_tile_at_coord((coord[0] - 1, coord[1])).get_plane() is not None:
                    return True
            elif not coord[0] == 9:
                if self.get_tile_at_coord((coord[0] + 1, coord[1])).get_plane() is not None:
                    return True
            #Bottom tiles
            if not coord[1] == 9:
                for x in xrange(from_x, to_x):
                    if self.get_tile_at_coord((x, to_y-1)).get_plane() is not None:
                        return True
            #No intervention needed
            return False
        except Exception, e:
            print "error checking intervention at {} because {}".format(coord, e)
            return False

    def control_coord(self, coord):
        """Checks if a specific coordinate needs intervention, if yes applies algorithm
        if not moves randomly
        Return value:
            1 if move was random
            0 if algorithm was applied
        """
        if self.get_tile_at_coord(coord) is None:
            return 0
        if self.intervention_required(coord) is False:
            self.move_plane_random(coord)
            return 1

