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
    
    def _reproduce(self,px,py):
        lp = len(px)-3 
        cp = random.randint(2,lp)

        return px[0:cp] + py[cp:]

    def _mutate(self,child):
    
        possibleVals = [x for x in range(0, len(child))]

        x, y = random.choices(possibleVals, k=2)

        mutatedChild = child[:]

        mutatedChild[x], mutatedChild[y] = mutatedChild[y] , mutatedChild[x]

        return mutatedChild



    def geneticAlgorithm(self,population,problem):

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
                child  = self._reproduce(parentX ,parentY )

                if random.random() < mutateRate:
                    child = self._mutate(child)

                newPopulation.append(child)
            
            population = newPopulation
        
            generation+=1
    