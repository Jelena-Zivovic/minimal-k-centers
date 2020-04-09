from graph import Graph
from _solvers.berkley import BerkleySolver
from _solvers.greedy import GreedySolver
from _solvers.sa import SimulatedAnnealingSolver
from _solvers.es import EvolutionarySolver
from _solvers.tabu import TabuSolver
from _solvers.vns import VariableNeighbourhoodSearch
from _solvers.bruteforce import BruteForceSolver
from _solvers.dsh import DominatingSet
from _solvers.scatter import ScatterSolver

import sources
import time
import json
import multiprocessing

def generateJSON(n):
    with open('file' + str(n) + '.json', "w") as file:
            weights, adjacency_list = sources.generateData(n)
            json.dump(adjacency_list, file)
        


def main():
    n = 50
    k = 9
    weights, adjacency_list = sources.generateData(n)

    g = Graph(adjacency_list, weights, list(range(n)))

    # bf_solver = BruteForceSolver(g)
    # bf_solver.solve(k)
    # berkley_solver = BerkleySolver(g, 3)
    # berkley_solver.solve(k)
    # greedy_solver = GreedySolver(g)
    # greedy_solver.solve(k)
    # evol_solver = EvolutionarySolver(g, 100, 20, 0.9, 25, 1)
    # evol_solver.solve(k)
    # sc_solver = ScatterSolver(g, 100, 20, 4, 15)
    # sc_solver.solve(k)    
    # simulated_annealing_solver = SimulatedAnnealingSolver(g)
    # simulated_annealing_solver.solve(k)
    tabu_solver1 = TabuSolver(g, 3000, 1)
    tabu_solver1.solve(k);
    tabu_solver2 = TabuSolver(g, 3000, 2)
    tabu_solver2.solve(k);
    

    # variable_neighborhood_search_solver = VariableNeighbourhoodSearch(g)
    # variable_neighborhood_search_solver.solve(k)    
    # dominating_set_solver = DominatingSet(g)
    # dominating_set_solver.solve(k)


if __name__ == "__main__":
    main()
