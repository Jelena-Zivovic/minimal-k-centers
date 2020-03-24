from abc import ABC, abstractmethod
import sources, math
import numpy as np
import random





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
        self.solution = self.graph.cardV * [False]


    def evaluate(self, individual):
        min_dist = self.graph.cardV * [float('inf')]
        for ind in range(len(individual)):
            if individual[ind]:
                for (w, i) in self.graph.get_neighbours(ind):
                    if w < min_dist[i]:
                        min_dist[i] = w
        return sum(min_dist) 
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
            
        #self.printSolution()
        print('------GREEDY-------')
        print(self.evaluate(self.solution))

class EvolutionarySolver(KCenterSolver):
    def __init__(self, graph, pop_size, iters):
        super().__init__(graph)
        self.pop_size = pop_size
        self.population = []
        self.iters = iters

    def __initialize(self, k):
        for i in range(self.pop_size):
            idx = random.sample(range(self.graph.cardV), k)
            new_individual = self.graph.cardV * [False]
            for i in idx:
                new_individual[i] = True
            self.population.append(new_individual)

    def __selection(self, population: list):
        tournament_size = 5
        contestants = random.sample(population, tournament_size)
        best = max(contestants, key = lambda x: x[1])
        return best[0]

    def __crossover(self, child1:list, child2:list):
        return (child1, child2)

    def __mutate(self, child:list):
        index1 = random.randint(0, self.graph.cardV-1)
        changed_val = child[index1]
        child[index1] = not child[index1]
        while True:
            index2 = random.randint(0, self.graph.cardV-1)
            if changed_val != child[index2]:
                child[index2] = not child[index2]
                break

        return child

    def solve(self, k):
        self.__initialize(k)
        
        for iteration in range(self.iters):
            fitnesses = list(map(lambda x: self.evaluate(x), self.population))
            pop_with_fit = list(zip(self.population, fitnesses))
            pop_with_fit.sort(key = lambda t: t[1], reverse = True)
            new_population = []
            for i in range(int(self.pop_size/8)):
                new_population.append(pop_with_fit[i][0])

            for i in range(int(self.pop_size/8), self.pop_size, 2):
                parent1 = self.__selection(pop_with_fit)
                parent2 = self.__selection(pop_with_fit)
                child1, child2 = self.__crossover(parent1, parent2)
                self.__mutate(child1)
                self.__mutate(child2)
                new_population.append(child1)
                new_population.append(child2)

            self.population = new_population
        print('-----EVOLUTIONARY------------')
        print(self.evaluate(self.population[0]))

def main():
    n = 10
    weights, adjacency_list = sources.generateData(n)
    g = Graph(adjacency_list, weights, list(range(n)))
    greedy_solver = GreedySolver(g)
    evol_solver = EvolutionarySolver(g, 1000, 300)
    greedy_solver.solve(5)
    evol_solver.solve(5)


if __name__ == "__main__":
    main()
