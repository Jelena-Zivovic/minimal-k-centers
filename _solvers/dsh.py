from solver import KCenterSolver
import random
from graph import Graph
import copy

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
            
    def is_graph_connected(self, G):
        #dfs se koristi za proveru
        
        if len(G.vertices) == 0:
            return False
        
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
        
    
    def dominating_set_alg(self, g):
        cov_cnt = dict()
        for v in g.vertices:
            cov_cnt[v] = len(g.adjacency_list[v]) + 1 
       
        
        score = copy.deepcopy(cov_cnt)
        D = set([])
        
        
        for i in range(len(g.vertices)):
            min_score_node = -1
            min_score = float('inf')
            
            for s in score:
                if score[s] < min_score:
                    min_score = score[s]
                    min_score_node = s 
            
            exist = False
            y = []
            
            for v in g.vertices:
                neighbors = [n[1] for n in g.get_neighbours(v)]
               

                if (min_score_node in neighbors) and cov_cnt[v] == 1:
                    D.add(min_score_node)
                    exist = True
                    cov_cnt[v] = 0
                    y.append(v)
                    
            if not exist:
                for a in y:
                    if cov_cnt[a] > 0:
                        cov_cnt[a] -= 1
                        score[a] += 1 
            score[min_score_node] = float('inf')
                    
                
        
        return D
                

        
    def solve(self, k):
        
        for w in self.graph.weights:
            G = self.parametricBottleneck(w)
            
            #print(self.is_graph_connected(G))
            
            if (self.is_graph_connected(G)):
            
                D = self.dominating_set_alg(G)
                
                if len(D) == k:
                    print("-------DHS--------")
                    print(D)
                    return list(D)
            
            
            

            
        
