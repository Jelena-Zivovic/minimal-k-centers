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
    solver = EvolutionarySolver(g, 100, iterations, 0.9, 5, 1)
    solver.solve(k)
    end = time.perf_counter()
    print((iterations, k, end - start))

def test_final(k, solver):
    now = time.perf_counter()
    solver.solve(k)
    end = time.perf_counter()
    print("Vreme: ", end - now, type(solver))


def main():
    n = 1500
    weights, adjacency_list = sources.generateData(n)    
    g = Graph(adjacency_list, weights, list(range(n)))
    bf_solver = BruteForceSolver(g)
    berkley_solver = BerkleySolver(g, 3)
    greedy_solver = GreedySolver(g)
    sc_solver = ScatterSolver(g, 100, 20, 4, 15)
    simulated_annealing_solver = SimulatedAnnealingSolver(g)
    ts = TabuSolver(g, 3000, 1)
    variable_neighborhood_search_solver = VariableNeighbourhoodSearch(g)
    dominating_set_solver = DominatingSet(g)
    e_solver = EvolutionarySolver(g, 200, 500, 0.9, 5, 1)
    solvers = [berkley_solver, greedy_solver, sc_solver, simulated_annealing_solver, 
            ts] 

    print('START TESTING')
    threads = []
    for i in range(len(solvers)):
        t = threading.Thread(target=test_final, args = [15, solvers[i]])
        t.start()
        threads.append(t)


    for t in threads:
        t.join()
if __name__ == "__main__":
    main()
