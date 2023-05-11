from pprint import pprint
import random
import sys

from item import Item
from localSearch import LocalSearch
from knapsack import Knapsack

def readItems(itemData):
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

def generatePopulation(length):
    rows = []
    for i in range(0,length):
        row = []
        for i in range(0,length):
            row.append(random.choice([0,1]))
        rows.append(row)
    return rows


print(sys.argv)
algorithm = sys.argv[1]

textFile =sys.argv[2] 

# open and close the above file in a with block instead
with open(textFile) as textData:
    itemData = textData.read().split("\n")


weightLimit = int(itemData[0])

items = readItems(itemData)

row = generateRandomRow(len(items))

knapsack = Knapsack(items,weightLimit)

localSearch = LocalSearch()

hillClimb = localSearch.randomRestartHillClimbing(row,knapsack)

simulatedAnnealing = localSearch.simulatedAnnealing(row,knapsack)

population = generatePopulation(len(items))

geneticAlgorithm = localSearch.geneticAlgorithmKnapsack(population,knapsack)


dataPrint = ""

match algorithm:
    case "ga":
        dataPrint = f"geneticAlgorithm : {geneticAlgorithm}"
    case "hc":
        dataPrint = f"hillClimb: {hillClimb}"
    case "sa":
        dataPrint = f"simulatedAnnealing : {simulatedAnnealing}"
    case "all":
        dataPrint = f"""
                          hillClimb: {hillClimb}
                          simulatedAnnealing : {simulatedAnnealing}
                          geneticAlgorithm : {geneticAlgorithm}"""
    case _:
        dataPrint = f"algorithm not found: {algorithm}"

result = f"""
             =============================================================================
             ========================  KNAPSACK LOCAL SEARCH  ===========================
             =============================================================================
                       {dataPrint}
            """
print(result)