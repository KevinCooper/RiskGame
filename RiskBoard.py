'''
@author: Kevin Cooper
@version: 0.0.3
@date: 01 Dec 13
@class: CS 359
'''
import Region
import networkx as nx
import CustomExceptionList as CEL
import pygame


class RiskBoard:
    '''
    A board implementation for the Risk like game.  Keeps track of all nodes\
    and edges between the nodes.
    '''

    def __init__(self, size):
        '''
        size - 2 item integer tuple

        Initializes the different pre-programmed regions.  The location is\
        proportional to the size that is given.
        '''
        self._graph = nx.Graph()
        self._regions = {}
        self._index = 0
        size = (pygame.display.Info().current_w,\
                pygame.display.Info().current_h)
        self._regions["tl1"] = Region.Region(name="tl1", position=(int(size[0]\
                                                 * .01), int(size[1] * .08)))
        self._regions["tl2"] = Region.Region(name="tl2", position=(int(size[0]\
                                                 * .1), int(size[1] * .07)))
        self._regions["tl3"] = Region.Region(name="tl3", position=(int(size[0]\
                                                 * .11), int(size[1] * .13)))
        self._regions["tl4"] = Region.Region(name="tl4", position=(int(size[0]\
                                                 * .07), int(size[1] * .11)))
        self._regions["tl5"] = Region.Region(name="tl5", position=(int(size[0]\
                                                 * .16), int(size[1] * .15)))
        self._regions["tl6"] = Region.Region(name="tl6", position=(int(size[0]\
                                                 * .04), int(size[1] * .14)))

        self._regions["ce1"] = Region.Region(name="ce1", position=(int(size[0]\
                                                 * .41), int(size[1] * .52)))
        self._regions["ce2"] = Region.Region(name="ce2", position=(int(size[0]\
                                                 * .53), int(size[1] * .56)))
        self._regions["ce3"] = Region.Region(name="ce3", position=(int(size[0]\
                                                 * .57), int(size[1] * .42)))
        self._regions["ce4"] = Region.Region(name="ce4", position=(int(size[0]\
                                                 * .48), int(size[1] * .49)))
        self._regions["ce5"] = Region.Region(name="ce5", position=(int(size[0]\
                                                 * .53), int(size[1] * .51)))
        self._regions["ce6"] = Region.Region(name="ce6", position=(int(size[0]\
                                                 * .52), int(size[1] * .47)))
        self._regions["ce7"] = Region.Region(name="ce7", position=(int(size[0]\
                                                 * .43), int(size[1] * .44)))

        for region in self._regions.items():
            self._graph.add_node(region[1])

        self._graph.add_edge(self._regions["tl5"], self._regions["ce7"])
        self._graph.add_edge(self._regions["tl1"], self._regions["tl2"])
        self._graph.add_edge(self._regions["tl1"], self._regions["tl4"])
        self._graph.add_edge(self._regions["tl5"], self._regions["tl6"])
        self._graph.add_edge(self._regions["tl6"], self._regions["tl3"])
        self._graph.add_edge(self._regions["tl2"], self._regions["tl5"])
        self._graph.add_edge(self._regions["tl2"], self._regions["tl3"])

        self._graph.add_edge(self._regions["ce1"], self._regions["ce2"])
        self._graph.add_edge(self._regions["ce2"], self._regions["ce3"])
        self._graph.add_edge(self._regions["ce3"], self._regions["ce4"])
        self._graph.add_edge(self._regions["ce4"], self._regions["ce5"])
        self._graph.add_edge(self._regions["ce5"], self._regions["ce6"])
        self._graph.add_edge(self._regions["ce6"], self._regions["ce7"])
        self._graph.add_edge(self._regions["ce2"], self._regions["ce5"])
        self._graph.add_edge(self._regions["ce1"], self._regions["ce4"])

    def __iter__(self):
        return self

    def __len__(self):
        return len(self._regions.items())

    def next(self):
        '''
        return - Region object

        Custom iterator that removes the need to do the strange [1] syntax to \
        only get the region from the dictionary when you run .items() on it.
        '''
        if(self._index == len(self._regions)):
            self._index = 0
            raise StopIteration
        temp = self._regions.items()[self._index][1]
        self._index = self._index + 1
        return temp

    def getRegions(self):
        '''
        NO LONGER IMPLEMENTED
        Custom iterator removes need for this

        return - a list of tuples

        Returns a list of all the region items on the board.  The format for\
        each tuple is ("name", Region)
        '''
        if self._regions != None:
            return self._regions.items()
        else:
            raise CEL.DetailedException("Get _regions was called on a board\
                 that had no _regions!")

    def getCountRegions(self, player):
        '''
        player - Player object

        return - integer

        Returns an integer representing how many regions are owned by\
        the player
        '''
        if self._regions != None:
            count = 0
            for region in self:
                if region.getPlayer() == player:
                    count = count + 1
            return count
        else:
            raise CEL.DetailedException("Get _regions was called on a\
             board that had no _regions!")

    def getNeighbors(self, region):
        '''
        Debugging method.  Not implemented in Release code.
        '''
        if region != None:
            return self._graph.neighbors(self._regions[region])

    def areNeighbors(self, region1, region2):
        '''
        region1 - Region object
        region2 - Region object

        return - boolean True/False

        Returns the value True if the two regions have an edge between them.\
        Returns the value False is there is no edge between the two regions.
        '''
        if region1 != None and region2 != None:
            neighbors = self._graph.neighbors(region1)
            for region in neighbors:
                if(region == region2):
                    return True
            return False

    def hasValidMove(self, player):
        '''
        player - Player object

        return - True/False

        Returns True if the player has a valid move, else False.
        '''
        if player != None:
            for region in self._regions:
                if(self._regions[region].getPlayer() == player and\
                             self._regions[region].canMove()):
                    return True
        return False
