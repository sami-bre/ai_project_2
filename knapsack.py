import random,math

class Knapsack:

    def __init__(self,items,weightLimit):
        self.weightLimit = weightLimit
        self.items = items

    def fitness(self,row):
        score = 0
        weight = 0
        for i in range(0,len(row)):
            if row[i] == 0:
                continue
            weight += self.items[i].weight
            score += self.items[i].price
        
        if weight > self.weightLimit:
            score = 0

        return score

    def generatorSuccessStates(self,state):
        neighbourStates = []
        for i in range(0,len(state)): 
            newNeighour = state[:]
            newNeighour[i] = 0 if newNeighour[i] == 1 else 1
            neighbourStates.append(newNeighour)
            
        return neighbourStates











