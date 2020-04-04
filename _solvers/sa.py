from solver import KCenterSolver
import random


class SimulatedAnnealingSolver(KCenterSolver):
    def __init__(self, graph):
        super().__init__(graph)
        self.current_solution = [False] * self.graph.cardV

    def __initialize(self, k):
        indices_of_first_solution = random.sample(
            range(0, self.graph.cardV), k)
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

    def solve(self, k):
        iters = 100
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
