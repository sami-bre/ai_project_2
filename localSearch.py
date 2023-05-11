import random,math

class LocalSearch:
    def __init__(self) -> None:
        pass
  
    def hillClimb(self,initialState,problem):

        current = initialState

        while True:
            
            neighborStates = problem.generatorSuccessStates(current)

            maxState = neighborStates[0]

            for State in neighborStates:
                maxState = State  if problem.fitness(State) > problem.fitness(maxState) else maxState
        
            currentFitness = problem.fitness(current)

            if problem.fitness(maxState) > currentFitness:
                current = maxState
            else:
                return current,currentFitness
    
    def randomRestartHillClimbing(self,initialState,problem):
        goalStates = []
        for i in range(0,20):
           randomState = [random.choice([0,1]) for i in initialState]

           goalState = self.hillClimb(randomState,problem)

           goalStates.append(goalState)
        
        goalStates.sort(key=lambda s:s[1])
        return goalStates[-1]

    def _TSchedule(self,T):
        return T * 0.99

    def simulatedAnnealing(self,randomState,problem):
        T = 100
        current = randomState

        while True:
            
            T  = self._TSchedule(T)

            if(T < 0.001):
                return current ,problem.fitness(current)
            
            neighborStates = problem.generatorSuccessStates(current) 
    
            nextState = neighborStates[random.randint(0,len(neighborStates)-1)]
            
            deltaE = problem.fitness(nextState) - problem.fitness(current) 
            

            if deltaE > 0:
                current = nextState
            else:
                if random.random() < math.e**(deltaE/T):
                    current = nextState    
        
    def _selectParents(self,pop):
        parents =[]
        for i in range(0,2):
            x,y = random.choices(pop,k=2)
            winner = x[0] if x[1] > y[1] else y[0]
            parents.append(winner)

        return parents
    
    def _reproduceKnapsack(self,px,py):
        lp = len(px)-3 
        cp = random.randint(2,lp)

        return px[0:cp] + py[cp:]

    def _mutateKnapsack(self,child):
    
        possibleVals = [x for x in range(0, len(child))]

        x, y = random.choices(possibleVals, k=2)

        mutatedChild = child[:]

        mutatedChild[x], mutatedChild[y] = mutatedChild[y] , mutatedChild[x]

        return mutatedChild



    def geneticAlgorithmKnapsack(self,population,problem):

        mutateRate = 0.1

        generation = 0

        while True:

            if generation == 400:
                population.sort( key=lambda s: problem.fitness(s))
                return population[-1],problem.fitness(population[-1])

            populationWithFitness = []

            newPopulation= []
            
            for state in population:
                populationWithFitness.append((state,problem.fitness(state)))


            for i in range(0,len(population)):
                parentX,parentY = self._selectParents(populationWithFitness)
                child  = self._reproduceKnapsack(parentX ,parentY )

                if random.random() < mutateRate:
                    child = self._mutateKnapsack(child)

                newPopulation.append(child)
            
            population = newPopulation
        
            generation+=1

    def _reproduceTsp(self, parent1, parent2):
        # Generate two random crossover points
        crossover_points = sorted(random.sample(range(len(parent1)), 2))

        # Extract the sub-tours to be crossed over from each parent
        sub_tour_1 = parent1[crossover_points[0]:crossover_points[1]]
        sub_tour_2 = parent2[crossover_points[0]:crossover_points[1]]

        # Generate a child using order crossover
        child = [-1] * len(parent1)
        child[crossover_points[0]:crossover_points[1]] = sub_tour_1
        remaining_indices = [i for i in range(len(parent1)) if parent1[i] not in sub_tour_1]
        remaining_values = [v for v in parent2 if v not in sub_tour_1]
        for i, value in zip(remaining_indices, remaining_values):
            # what does the zip function do?
            # a: it creates a list of tuples
            # a: each tuple contains one index and one value
            # a: the index is from the list of indices that are not in the sub-tour
            # a: the value is from the list of values that are not in the sub-tour
            if child[i] == -1:
                child[i] = value

        return child


    def _mutateTsp(self, individual):
        # Generate two random mutation points
        mutation_points = random.sample(range(len(individual)), 2)

        # Swap the cities at the mutation points
        individual[mutation_points[0]], individual[mutation_points[1]] = \
            individual[mutation_points[1]], individual[mutation_points[0]]

        return individual

    def geneticAlgorithmTsp(self, population, problem):
        mutate_rate = 0.1
        generation = 0

        while True:
            if generation == 400:
                population.sort(key=lambda s: problem.fitness(s))
                return population[-1], problem.fitness(population[-1])

            population_with_fitness = []

            new_population = []

            for state in population:
                population_with_fitness.append((state, problem.fitness(state)))

            for i in range(0, len(population)):
                parent_x, parent_y = self._selectParents(population_with_fitness)
                child = self._reproduceTsp(parent_x, parent_y)

                if random.random() < mutate_rate:
                    child = self._mutateTsp(child)

                new_population.append(child)

            population = new_population

            generation += 1