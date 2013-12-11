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
import random
class RiskBoard:
    
    def __init__(self, size):
        self._regionPicture = "circle.png"
        self._graph = nx.Graph()
        self._regions = {}
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self._regions["tl1"] = Region.Region(image=self._regionPicture, name="tl1", position=(int(size[0] * .01), int(size[1] * .08)))
        self._regions["tl2"] = Region.Region(image=self._regionPicture, name="tl2", position=(int(size[0] * .1), int(size[1] * .07)))
        self._regions["tl3"] = Region.Region(image=self._regionPicture, name="tl3", position=(int(size[0] * .11), int(size[1] * .13)))
        self._regions["tl4"] = Region.Region(image=self._regionPicture, name="tl4", position=(int(size[0] * .07), int(size[1] * .11)))
        self._regions["tl5"] = Region.Region(image=self._regionPicture, name="tl5", position=(int(size[0] * .16), int(size[1] * .15)))
        self._regions["tl6"] = Region.Region(image=self._regionPicture, name="tl6", position=(int(size[0] * .04), int(size[1] * .14)))
        
        self._regions["ce1"] = Region.Region(image=self._regionPicture, name="ce1", position=(int(size[0] * .41), int(size[1] * .52)))
        self._regions["ce2"] = Region.Region(image=self._regionPicture, name="ce2", position=(int(size[0] * .53), int(size[1] * .56)))
        self._regions["ce3"] = Region.Region(image=self._regionPicture, name="ce3", position=(int(size[0] * .57), int(size[1] * .42)))
        self._regions["ce4"] = Region.Region(image=self._regionPicture, name="ce4", position=(int(size[0] * .48), int(size[1] * .49)))
        self._regions["ce5"] = Region.Region(image=self._regionPicture, name="ce5", position=(int(size[0] * .53), int(size[1] * .51)))
        self._regions["ce6"] = Region.Region(image=self._regionPicture, name="ce6", position=(int(size[0] * .52), int(size[1] * .47)))
        self._regions["ce7"] = Region.Region(image=self._regionPicture, name="ce7", position=(int(size[0] * .43), int(size[1] * .44)))
        
 
        
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
        # for neighbor in self.graph.neighbors(self._regions["Center"]):
        #   print neighbor
            
    def getRegions(self):
        if self._regions != None:
            return self._regions.items()
        else:
            raise CEL.DetailedException("Get _regions was called on a board that had no _regions!")
        
    def getCountRegions(self, player):
        if self._regions != None:
            count = 0
            for region in self._regions.items():
                if region[1].getPlayer() == player:
                    count = count + 1
            return count
        else:
            raise CEL.DetailedException("Get _regions was called on a board that had no _regions!")
        
    def getNeighbors(self, region):
        if region != None:
            return self._graph.neighbors(self._regions[region])
    
    def areNeighbors(self, region1, region2):
        if region1 != None and region2 != None:
            neighbors = self._graph.neighbors(region1)
            for region in neighbors:
                if(region == region2):
                    return True
            return False
    
    def hasValidMove(self, player):
        if player != None:
            for region in self._regions:
                if(self._regions[region].getPlayer() == player and self._regions[region].canMove()):
                    return True
        return False
        
