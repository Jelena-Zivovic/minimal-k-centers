from graph import Graph
from _solvers.berkley import BerkleySolver
from _solvers.greedy import GreedySolver
from _solvers.sa import SimulatedAnnealingSolver
from _solvers.es import EvolutionarySolver
from _solvers.tabu import TabuSolver
from _solvers.vns import VariableNeighbourhoodSearch
from _solvers.hibrid import Hibrid

import sources


def main():
    n = 100
    weights, adjacency_list = sources.generateData(n)
    g = Graph(adjacency_list, weights, list(range(n)))
    greedy_solver = GreedySolver(g)
    #evol_solver = EvolutionarySolver(g, 10000, 20, 0.9, 25)
    greedy_solver.solve(50)
    #evol_solver.solve(50)
    simulated_annealing_solver = SimulatedAnnealingSolver(g)
    simulated_annealing_solver.solve(50, 100)
    #tabu_solver = TabuSolver(g)
    #tabu_solver.solve(4);
    variable_neighborhood_search_solver = VariableNeighbourhoodSearch(g)
    variable_neighborhood_search_solver.solve(50, 100, 5)
    hibrid_solver = Hibrid(g)
    hibrid_solver.solve(50)

if __name__ == "__main__":
    main()
