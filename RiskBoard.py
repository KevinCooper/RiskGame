'''
Created on Dec 2, 2013

@author: C15JREYNOR
'''
import Region
import networkx as nx
class RiskBoard:
    
    def __init__(self):
        self.graph = nx.Graph()
        regions = {}
        regions["Center"] = Region.Region(player=None, units=0, name="Center")  
        regions["Left"] =Region.Region(player=None, units=0, name="Left")
        regions["Top"] =Region.Region(player=None, units=0, name="Top")
        regions["Right"] =Region.Region(player=None, units=0, name="Right")
        regions["Bottom"] =Region.Region(player=None, units=0, name="Bottom")
        
        self.graph.add_node(regions["Center"])# Center Region
        self.graph.add_node(regions["Left"])# Left Region
        self.graph.add_node(regions["Top"])# Top Region
        self.graph.add_node(regions["Right"])# Right Region
        self.graph.add_node(regions["Bottom"])# Bottom Region
        self.graph.add_edge(regions["Center"], regions["Left"])
        self.graph.add_edge(regions["Center"], regions["Top"])
        self.graph.add_edge(regions["Center"], regions["Right"])
        self.graph.add_edge(regions["Center"], regions["Bottom"])
        for neighbor in self.graph.neighbors(regions["Center"]):
            print neighbor
        
