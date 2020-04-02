from graph import Graph
from _solvers.berkley import BerkleySolver
from _solvers.greedy import GreedySolver
from _solvers.sa import SimulatedAnnealingSolver
from _solvers.es import EvolutionarySolver
from _solvers.tabu import TabuSolver
from _solvers.vns import VariableNeighbourhoodSearch
from _solvers.bruteforce import BruteForceSolver

import sources


def main():
    n = 20
    k = 3
    weights, adjacency_list = sources.generateData(n)
    g = Graph(adjacency_list, weights, list(range(n)))
    bf_solver = BruteForceSolver(g)
    bf_solver.solve(k)
    berkley_solver = BerkleySolver(g, 200)
    berkley_solver.solve(k)
    greedy_solver = GreedySolver(g)
    greedy_solver.solve(k)
    evol_solver = EvolutionarySolver(g, 100, 20, 0.9, 25)
    evol_solver.solve(k)
    simulated_annealing_solver = SimulatedAnnealingSolver(g)
    simulated_annealing_solver.solve(k, 100)
    tabu_solver = TabuSolver(g, 3000)
    tabu_solver.solve(k);
    variable_neighborhood_search_solver = VariableNeighbourhoodSearch(g)
    variable_neighborhood_search_solver.solve(k, 100, 5)


if __name__ == "__main__":
    main()