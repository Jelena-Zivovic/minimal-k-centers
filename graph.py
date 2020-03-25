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
    def __init__(self, graph, pop_size, iters, mutation_rate):
        super().__init__(graph)
        self.pop_size = pop_size
        self.population = []
        self.iters = iters
        self.mutation_rate = mutation_rate

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

    def __crossover(self, parent1:list, parent2:list, k):
        return (parent1, parent2)
        child1 = parent1[:]
        child2 = parent2[:]
        index1 = []
        index2 = []
        for i in range(len(parent1)):
            if parent1[i]:
                index1.append(i)
            if parent2[i]:
                index2.append(i)

        samp1 = random.sample(index1, int(k/2))
        samp2 = random.sample(index2, int(k/2))
        for s1, s2 in zip(samp1, samp2):
            tmp = child1[s1] 
            child1[s1] = child2[s1]  
            child2[s1] = tmp

            tmp = child2[s2] 
            child2[s2] = child1[s2] 
            child1[s2] = tmp
            

        return (child1[:], child2[:])

    def __mutate(self, child:list):
        if random.random() > self.mutation_rate:
            return child
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
                child1, child2 = self.__crossover(parent1, parent2, k)
                self.__mutate(child1)
                self.__mutate(child2)
                new_population.append(child1)
                new_population.append(child2)

            self.population = new_population
        print('-----EVOLUTIONARY------------')
        print(self.evaluate(self.population[0]))
        
class SimulatedAnnealingSolver(KCenterSolver):
    def __init__(self, graph):
        super().__init__(graph)
        self.current_solution = [False] * self.graph.cardV
        
        
    def __initialize(self, k):
        indices_of_first_solution = random.sample(range(0, self.graph.cardV), k)
        for i in range(self.graph.cardV):
            if i in indices_of_first_solution:
                self.current_solution[i] = True
        
    def invert(self):
        index_true = -1
        index_false = -1
        while True:
            random_number = random.sample(range(self.graph.cardV), 1)[0]
            if self.current_solution[random_number]:
                index_true = random_number
                break
            else:
                index_false = random_number
                break
        
        while True:
            random_number = random.sample(range(self.graph.cardV), 1)[0]
            
            if self.current_solution[random_number]:
                if index_true == -1:
                    index_true = random_number
                    break
            else:
                if index_false == -1:
                    index_false = random_number
                    break
        
        self.current_solution[index_true] = False
        self.current_solution[index_false] = True 
        
        return index_true, index_false
        
    def restore(self, index_true, index_false):
        self.current_solution[index_true] = True 
        self.current_solution[index_false] = False 
        
    def solve(self, k, iters):
        
        self.__initialize(k)
        current_value = self.evaluate(self.current_solution)
        best_value = current_value
        
        
        for i in range(1, iters):
            index_true, index_false = self.invert()
            new_value = self.evaluate(self.current_solution)
            if new_value < current_value:
                current_value = new_value
            else:
                p = 1.0 / i ** 0.5
                q = random.uniform(0, 1)
                if p > q:
                    current_value = new_value
                else:
                    self.restore(index_true, index_false)
            if new_value < best_value:
                best_value = new_value
        
        print("---------SIMULATED ANNEALING---------")
        print(best_value)
            
        
        
    

def main():
    n = 100
    weights, adjacency_list = sources.generateData(n)
    g = Graph(adjacency_list, weights, list(range(n)))
    greedy_solver = GreedySolver(g)
    evol_solver = EvolutionarySolver(g, 100, 100, 1)
    greedy_solver.solve(50)
    evol_solver.solve(50)
    simulated_annealing_solver = SimulatedAnnealingSolver(g)
    simulated_annealing_solver.solve(50, 100)


if __name__ == "__main__":
    main()
