from abc import ABC, abstractmethod
import sources, math
import numpy as np




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
    @abstractmethod    
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
        low = 0
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

class GreedySolver(KCenterSolver):
    def __init__(self, graph):
        super().__init__(graph)
        self.solution = self.graph.cardV * [False]


    def printSolution(self):
        for i in range(len(self.solution)):
            if self.solution[i]:
                print(i, end = ' ')
        print()


    def finMin(self, i):
        neighbours_of_i = self.graph.get_neighbours(i)
        #min_w = neighbours[0][0]
        min_w = float('inf')
        for neighbour in neighbours_of_i:
            if self.solution[neighbour[1]]:
                min_w = min(neighbour[0], min_w)
        
        return min_w


    def solve(self, k):
        
        self.solution[np.random.randint(0, self.graph.cardV)] = True
        for t in range(1, k):
            bestCenter = -1
            currentMax = -1
            for i in range(0, self.graph.cardV):
                if not self.solution[i]:
                    min_i = self.finMin(i)
                    if min_i > currentMax:
                        currentMax = min_i
                        bestCenter = i
            self.solution[bestCenter] = True
            
        self.printSolution()

def main():
    n = 100
    weights, adjacency_list = sources.generateData(n)
    g = Graph(adjacency_list, weights, list(range(n)))
    solver = GreedySolver(g)
    ber_solver = BerkleySolver(g)
    solver.solve(10)
    ber_solver.solve(10)


if __name__ == "__main__":
    main()