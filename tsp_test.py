import random
from localSearch import LocalSearch
from tsp import TSP


tsp = TSP(num_cities=10)
ls = LocalSearch()
initial_route = [i for i in range(tsp.num_cities)]
random.shuffle(initial_route)

best_route, best_fitness = ls.hillClimb(initial_route, tsp)
print("With hill climbing:")
print(f"Best route: {best_route} with fitness: {best_fitness}")

best_route, best_fitness = ls.simulatedAnnealing(initial_route, tsp)
print("With simulated annealing:")
print(f"Best route: {best_route} with fitness: {best_fitness}")

population = tsp.generatorSuccessStates(initial_route)

best_route, best_fitness = ls.geneticAlgorithmTsp(population, tsp)
print("With genetic algorithm:")
print(f"Best route: {best_route} with fitness: {best_fitness}")

