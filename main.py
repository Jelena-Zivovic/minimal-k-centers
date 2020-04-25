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
import threading

def generateJSON(n):
    with open('file' + str(n) + '.json', "w") as file:
            weights, adjacency_list = sources.generateData(n)
            json.dump(adjacency_list, file)
        

def testing(iterations, k, g):
    start = time.perf_counter()
    solver = EvolutionarySolver(g, 100, iteartions, 0.9, 5)
    solver.solve(k)
    end = time.perf_counter()
    print((iterations, k, end - start))

def main():
    n = 100
    weights, adjacency_list = sources.generateData(n)    
    g = Graph(adjacency_list, weights, list(range(n)))
        
    # bf_solver = BruteForceSolver(g)
    # bf_solver.solve(k)
    # berkley_solver = BerkleySolver(g, 3)
    # berkley_solver.solve(k)
    # greedy_solver = GreedySolver(g)
    # greedy_solver.solve(k)
    threads = []
    for iteartions in [20, 50, 100, 200, 500, 1000, 2500]: 
        for k in [2, 5, 10, 25, 50]:
            thread = threading.Thread(target="testing", args=[iteartions, k, g])
            threads.append(thread)
            thread.start()

    for t in threads:
        t.join()

    # sc_solver = ScatterSolver(g, 100, 20, 4, 15)
    # sc_solver.solve(k)    
    # simulated_annealing_solver = SimulatedAnnealingSolver(g)
    # simulated_annealing_solver.solve(k)
    # tabu_solver1 = TabuSolver(g, 3000, 1)
    # tabu_solver1.solve(k);
    # tabu_solver2 = TabuSolver(g, 3000, 2)
    # tabu_solver2.solve(k);
    

    # variable_neighborhood_search_solver = VariableNeighbourhoodSearch(g)
    # variable_neighborhood_search_solver.solve(k)    
    # dominating_set_solver = DominatingSet(g)
    # dominating_set_solver.solve(k)


if __name__ == "__main__":
    main()
