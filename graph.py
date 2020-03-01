from abc import ABC, abstractmethod
import sources, math





class Graph:
    def __init__(self, adjacency_list: dict, weights: list, vertices: list):
        self.adjacency_list = adjacency_list
        self.weights = weights
        self.vertices = vertices
        self.cardV = len(vertices)
        self.cardE = len(weights)

    def __str__(self):
        return str(self.adjacency_list)


    def get_neighbours(self, n):
        return self.adjacency_list[n]


class KCenterSolver(ABC):
    def __init__(self, graph:Graph):
        self.graph = graph
    
    def solve(self, k):
        pass



class BerkleySolver(KCenterSolver):
    def __init__(self, graph):
        super().__init__(graph)

    
    def ADJmid(self, x, mid):
        threshold = self.graph.weights[mid]
        return [t  for (w, t) in self.graph.adjacency_list[x] if w <= threshold]

    def solve(self, k):
        if k == self.graph.cardV:
            return            
        low = 1
        high = int(self.graph.cardE)
        S1 = set()
        while high != low + 1:
            mid = math.floor((low + high) / 2)
            S = set()
            T :list = self.graph.vertices.copy()
            
            while bool(T):
                
                x = T.pop()
                S.add(x)
                #print('----------------------------------')
                #print('x = ' + str(x))           
                for v in self.ADJmid(x, mid):
                    if v in T:
                        T.remove(v)
                    for w in self.ADJmid(v, mid):
                        #print('v = {}, w = {}, T = {} '.format(v, w, T))
                        if w in T:
                            T.remove(w)
                        
            if len(S) <= k:
                high = mid
                S1 = S.copy()
                print(S1)
                return S
            else:
                low = mid
        print(S1)
        return S1   

def main()
:
    n = 10
    weights, adjacency_list = sources.generateData(n)
    g = Graph(adjacency_list, weights, list(range(1, n+1)))
    solver = BerkleySolver(g)
    
    solver.solve(2)


if __name__ == "__main__":
    main()