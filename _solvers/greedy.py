from solver import (KCenterSolver, np)

class GreedySolver(KCenterSolver):
    def __init__(self, graph):
        super().__init__(graph)

    def __repr__(self):
        return "Greedy "


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
            
        print(self, end= " ")
        print(self.evaluate(self.solution))
