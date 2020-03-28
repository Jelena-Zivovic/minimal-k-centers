from solver import KCenterSolver


class TabuSolver(KCenterSolver):
    def __init__(self, graph):
        super().__init__(graph)


    def __initalize(self, k):
        return None

    


    def get_neighbours(self):
        neighbours = []

        transformed_solution = self.transform_solution(self.current_solution)
        for point in transformed_solution:
            print()    

    def solve(self, k):
        self.current_solution = self.__initalize(k)
        self.best_value = self.evaluate(self.current_solution)    
        T = []
        while True:
            self.get_neighbours()
