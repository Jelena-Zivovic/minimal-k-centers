from solver import KCenterSolver
import random


class VariableNeighbourhoodSearch(KCenterSolver):
    def __init__(self, graph):
        super().__init__(graph)
        self.current_solution = [False] * self.graph.cardV

    def __repr__(self):
        return "Variable search neighbourhood: "

    def __initialize(self, k):
        indices_of_first_solution = random.sample(
            range(0, self.graph.cardV), k)
        for i in range(self.graph.cardV):
            if i in indices_of_first_solution:
                self.current_solution[i] = True

    def invert(self, random_index):
        if self.current_solution[random_index]:
            self.current_solution[random_index] = False

            min_value = float('inf')
            min_index = -1

            for i in range(self.graph.cardV):
                if i != random_index and (not self.current_solution[i]):
                    self.current_solution[i] = True
                    if self.evaluate(self.current_solution) < min_value:
                        min_value = self.evaluate(self.current_solution)
                        min_index = i
                    self.current_solution[i] = False

            self.current_solution[min_index] = True
            return random_index, min_index
        else:
            self.current_solution[random_index] = True

            min_value = float('inf')
            min_index = -1

            for i in range(self.graph.cardV):
                if i != random_index and self.current_solution[i]:
                    self.current_solution[i] = False
                    if self.evaluate(self.current_solution) < min_value:
                        min_value = self.evaluate(self.current_solution)
                        min_index = i
                    self.current_solution[i] = True

            self.current_solution[min_index] = False
            return min_index, random_index

    def restore(self, index_true, index_false):

        if index_true != -1 or index_false == -1:
            return

        self.current_solution[index_true] = True
        self.current_solution[index_false] = False

    def get_neighbour(self, env):
        if env == 0:
            return -1, -1
        for i in range(env):
            random_index = random.sample(range(self.graph.cardV), 1)[0]
            index_true, index_false = self.invert(random_index)
            return index_true, index_false

    def solve(self, k):
        iters = 500
        maxEnv = 5
        self.__initialize(k)
        current_value = self.evaluate(self.current_solution)
        best_value = current_value

        for i in range(iters):
            env = 0
            while env < maxEnv:
                index_true, index_false = self.get_neighbour(env)
                new_value = self.evaluate(self.current_solution)
                if new_value < current_value:
                    current_value = new_value
                    env = 0
                else:
                    self.restore(index_true, index_false)
                    env += 1

                if new_value < best_value:
                    best_value = new_value

        print(self, end = " ")
        print(best_value)
        return best_value
