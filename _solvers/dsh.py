from solver import KCenterSolver
import random
from graph import Graph
import networkx as nx

class DominatingSet(KCenterSolver):
    def __init__(self, graph):
        super().__init__(graph)
        
    def parametricBottleneck(self, weight):
        G = {}
        weights = []
        vertices = []
        for v in self.graph.adjacency_list:
            edges_v = []
            for edge in self.graph.adjacency_list[v]:
                if edge[0] < weight:
                    edges_v.append(edge)
                    
            if len(edges_v) != 0:
                G[v] = edges_v
                vertices.append(v)
                weights.extend([w[0] for w in edges_v])
                
        vertices.sort()
        weights.sort()      
        return Graph(G, weights, vertices)
            
    def isGraphConnected(self, G):
        #dfs se koristi za proveru
        
        visited = set([])
        visited.add(G.vertices[0])
        path = [G.vertices[0]]
        
        while len(path) > 0:
            
            if len(visited) == len(G.vertices):
                return True
            
            n = path[-1]
            
            has_unvisited = False
            
            for (w, m) in G.get_neighbours(n):
               
                if m not in visited:
                    path.append(m)
                    visited.add(m)
                    has_unvisited = True
                    break
            
            if (not has_unvisited):
                path.pop()
                
        return False
        
        
        
        
    def solve(self, k):
        
        for w in self.graph.weights:
            G = self.parametricBottleneck(w)
            
            
            

            
        
