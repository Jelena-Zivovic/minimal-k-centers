from solver import KCenterSolver    
import math

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


