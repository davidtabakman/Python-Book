# -*- coding: utf-8 -*-


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
            first_tile = self.get_tiles()[coord_from[0]][coord_from[1]]
            second_tile = self.get_tiles()[coord_to[0]][coord_to[1]]
            if first_tile.get_plane() is not None:
                if second_tile.get_plane() is None:
                    second_tile.set_plane(first_tile.get_plane())
                    first_tile.set_plane(None)
        except IndexError:
            print "error: failed to move plane from {} to {} because: one of the tiles is out of the board".format(coord_from, coord_to)
        except Exception, e:
            print "error: failed to move plane from {} to {} because: {}".format(coord_from, coord_to, e)

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
            #Upper tiles
            for x in xrange(coord[0] - 1, coord[0] + 2):
                if self.get_tile_at_coord((x, coord[1] - 1)).get_plane() is not None:
                    return True
            #Side tiles
            if self.get_tile_at_coord((coord[0] - 1, coord[1])).get_plane() is not None:
                return True
            if self.get_tile_at_coord((coord[0] + 1, coord[1])).get_plane() is not None:
                return True
            #Bottom tiles
            for x in xrange(coord[0] - 1, coord[0] + 2):
                if self.get_tile_at_coord((x, coord[1] + 1)).get_plane() is not None:
                    return True
            #No intervention needed
            return False
        except Exception, e:
            print "error checking intervention at {} because {}".format(coord, e)
            return False

