from solver import KCenterSolver
import random

class ScatterSolver(KCenterSolver):
    def __init__(self, graph, p_size, b, subset_size, number_of_subs):
        super().__init__(graph)
        self.p_size = p_size
        self.b = b
        self.subset_size = subset_size
        self.number_of_sets = number_of_subs
    
    def div_gen_method(self, k: int):
        solutions = list()    
        for i in range(100):
            tmp_solution = [False] * self.graph.cardV
            idxs = random.sample(range(self.graph.cardV), k)
            for i in range(self.graph.cardV):
                if i in idxs:
                    tmp_solution[i] = True
            solutions.append(tmp_solution)
        return solutions

    def improve_solution(self, solution: list, k: int):
        first_solution = solution[:]
        for i in range(20):
            value_of_solution = self.evaluate(solution)
            transformed = self.transform_solution(solution)
            idx_to_change = random.randint(0, k-1)
            while True:
                idx2_to_change = random.randint(0, self.graph.cardV-1)
                if idx2_to_change not in transformed:
                    break
            solution[transformed[idx_to_change]] = False
            solution[idx2_to_change] = True
            if self.evaluate(solution) < value_of_solution:
                break
        else:
            return first_solution
        return solution


    def create_subsets(self, ref_best_solutions: list):
        subsets = []
        for i in range(self.number_of_sets):
            subsets.append(random.sample(ref_best_solutions, self.subset_size))
        return subsets


    def combinate(self, s, k):
        final_solution = []
        for i in range(self.graph.cardV):
            tmp = False
            for j in range(self.subset_size):
                tmp = tmp or s[j][i]
            final_solution.append(tmp)
        while sum(final_solution) != k:
            idx = random.randint(0, self.graph.cardV-1)
            final_solution[idx] = False
        
        return final_solution
    
    def updateRefSet(self, refSet, improved):
        val = self.evaluate(improved)
        has_changed = False
        for i in range(len(refSet)):
            if val < self.evaluate(refSet[i]):
                refSet.insert(i, improved)
                has_changed = True
        if has_changed:
            refSet.pop()


    def solve(self, k):
        P = []
        solutions = self.div_gen_method(k)
        for solution in solutions:
            improved_solution = self.improve_solution(solution, k)
            if improved_solution not in P:
                P.append(improved_solution)
            if self.p_size == len(P):
                break
        
        ref_best_solutions = sorted(P, key = lambda sol: self.evaluate(sol))[0:self.b]
        new_solutions: bool = True
        
        while new_solutions:
            subsets_of_solutions:list = self.create_subsets(ref_best_solutions)
            new_solutions = False
            while len(subsets_of_solutions):
                s = subsets_of_solutions.pop(0)
                trial_solution = self.combinate(s, k)
                improved_solution = self.improve_solution(trial_solution, k)
                hasChangedRefSet = self.updateRefSet(ref_best_solutions, improved_solution)
                
                if hasChangedRefSet:
                    new_solutions = True
        print('----------SCATTER SEARCH--------------')        
        print(self.evaluate(ref_best_solutions[0]))