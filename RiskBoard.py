'''
Created on Dec 2, 2013

@author: C15JREYNOR
'''
import Region
import networkx as nx
import CustomExceptionList as CEL
import pygame
class RiskBoard:
    
    def __init__(self):
        regionPicture = pygame.image.load("circle.png").convert()
        self.graph = nx.Graph()
        self.regions = {}
        self.regions["Center"] = Region.Region(image=regionPicture, player=None, units=0, name="Center", position=(300, 300))  
        self.regions["Left"] = Region.Region(image=regionPicture, player=None, units=0, name="Left", position=(50, 300))
        self.regions["Top"] = Region.Region(image=regionPicture, player=None, units=0, name="Top", position=(300, 20))
        self.regions["Right"] = Region.Region(image=regionPicture, player=None, units=0, name="Right", position=(500, 300))
        self.regions["Bottom"] = Region.Region(image=regionPicture, player=None, units=0, name="Bottom", position=(300, 450))
        
        self.graph.add_node(self.regions["Center"])  # Center Region
        self.graph.add_node(self.regions["Left"])  # Left Region
        self.graph.add_node(self.regions["Top"])  # Top Region
        self.graph.add_node(self.regions["Right"])  # Right Region
        self.graph.add_node(self.regions["Bottom"])  # Bottom Region
        
        self.graph.add_edge(self.regions["Center"], self.regions["Left"])
        self.graph.add_edge(self.regions["Center"], self.regions["Top"])
        self.graph.add_edge(self.regions["Center"], self.regions["Right"])
        self.graph.add_edge(self.regions["Center"], self.regions["Bottom"])
        # for neighbor in self.graph.neighbors(self.regions["Center"]):
        #   print neighbor
            
    def getRegions(self):
        if self.regions != None:
            return self.regions.items()
        else:
            raise CEL.DetailedException("Get regions was called on a board that had no regions!")
        
    def getNeighbors(self, region):
        return self.graph.neighbors(self.regions[region])
    
    def hasValidMove(self, player):
        for region in self.regions:
            if(self.regions[region].getPlayer() == player and self.regions[region].canMove()):
                return True
        return False
        
