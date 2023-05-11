import random
import math

class TSP:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.cities = [(random.uniform(0, 1), random.uniform(0, 1)) for i in range(num_cities)]
        self.distances = [[self._distance(self.cities[i], self.cities[j]) for j in range(num_cities)] for i in range(num_cities)]

    def fitness(self, route):
        dist = 0
        for i in range(len(route)-1):
            dist += self.distances[route[i]][route[i+1]]
        dist += self.distances[route[-1]][route[0]]
        return 1.0 / (dist + 1)

    def generatorSuccessStates(self, route):
        neighbours = []
        for i in range(1, len(route)-1):
            for j in range(i+1, len(route)):
                neighbour = route[:]
                neighbour[i:j] = reversed(neighbour[i:j])
                neighbours.append(neighbour)
        return neighbours
    
    def _distance(self, p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
