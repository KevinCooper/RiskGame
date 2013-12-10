'''
@author: Kevin Cooper
@version: 0.0.2
@date: 01 Dec 13
@class: CS 359
'''
import Region
import networkx as nx
import CustomExceptionList as CEL
class RiskBoard:
    
    def __init__(self, size):
        self._regionPicture = "circle.png"
        self._graph = nx.Graph()
        self._regions = {}
        self._regions["Center"] = Region.Region(image=self._regionPicture,  name="Center", position=(500, 300))  
        self._regions["Left"] = Region.Region(image=self._regionPicture,  name="Left", position=(50, 300))
        self._regions["Top"] = Region.Region(image=self._regionPicture,  name="Top", position=(500, 20))
        self._regions["Right"] = Region.Region(image=self._regionPicture,  name="Right", position=(900, 300))
        self._regions["Bottom"] = Region.Region(image=self._regionPicture,  name="Bottom", position=(500, 600))
        
        self._graph.add_node(self._regions["Center"])  # Center Region
        self._graph.add_node(self._regions["Left"])  # Left Region
        self._graph.add_node(self._regions["Top"])  # Top Region
        self._graph.add_node(self._regions["Right"])  # Right Region
        self._graph.add_node(self._regions["Bottom"])  # Bottom Region
        
        self._graph.add_edge(self._regions["Center"], self._regions["Left"])
        self._graph.add_edge(self._regions["Center"], self._regions["Top"])
        self._graph.add_edge(self._regions["Center"], self._regions["Right"])
        self._graph.add_edge(self._regions["Center"], self._regions["Bottom"])
        # for neighbor in self.graph.neighbors(self._regions["Center"]):
        #   print neighbor
            
    def getRegions(self):
        if self._regions != None:
            return self._regions.items()
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
        
