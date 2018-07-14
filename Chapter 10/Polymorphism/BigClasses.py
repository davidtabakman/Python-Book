# -*- coding: utf-8 -*-


class BigThing(object):

    def __init__(self, thing):
        self.__thing = thing

    def size(self):
        if isinstance(self.__thing, int) or isinstance(self.__thing, float) or isinstance(self.__thing, long):
            return self.__thing
        else:
            return len(self.__thing)


class BigCat(BigThing):

    def __init__(self, thing, weight):
        super(BigCat, self).__init__(thing)
        self.__weight = weight

    def size(self):
        if self.__weight > 20:
            return "Very Fat"
        elif self.__weight > 15:
            return "Fat"
        else:
            return "OK"
