from pprint import pprint
import random
import sys

from item import Item
from localSearch import LocalSearchs
from knapsack import Knapsack

def readitems(itemData):
    items = []
    for i in range(2,len(itemData)):
        name,weight,price,n_item = itemData[i].split(",")
        for i in range(0,int(n_item)):
            item = Item(name,float(weight),float(price))
            items.append(item)
    return items
    
def generateRandomRow(length):
    row = []
    for i in range(0,length):
       row.append(random.choice([0,1]))
    return row

print(sys.argv)
algorithm = sys.argv[1]

textFile =sys.argv[2] 

# open and close the above file in a with block instead
with open(textFile) as textData:
    itemData = textData.read().split("\n")


weightLimit = int(itemData[0])

items = readitems(itemData)

row = generateRandomRow(len(items))

knapsack = Knapsack(items,weightLimit)

localSearchs = LocalSearchs()

hillClimb = localSearchs.randomRestartHillClimbing(row,knapsack)

simulatedAnnealing = localSearchs.simulatedAnnealing(row,knapsack)

population = knapsack.generatorSuccessStates(row)

geneticAlgorithm = localSearchs.geneticAlgorithm(population,knapsack)


dataprint = ""

match algorithm:
    case "ga":
        dataprint = f"geneticAlgorithm : {geneticAlgorithm}"
    case "hc":
        dataprint = f"hillClimb: {hillClimb}"
    case "sa":
        dataprint = f"simulatedAnnealing : {simulatedAnnealing}"
    case "all":
        dataprint = f"""
                          hillClimb: {hillClimb}
                          simulatedAnnealing : {simulatedAnnealing}
                          geneticAlgorithm : {geneticAlgorithm}"""
    case _:
        dataprint = f"algorithm not found: {algorithm}"

result = f"""
             =============================================================================
             ========================  KNAPSACK LOCAL SEREACH  ===========================
             =============================================================================
                       {dataprint}
            """
print(result)