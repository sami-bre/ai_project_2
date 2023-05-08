import random

# Define the genetic algorithm parameters
pop_size = 50
elite_size = 10
mutation_rate = 0.1
generations = 100

def fitness(individual, items, max_weight):
    total_value = sum(item[2] * individual[i] for i, item in enumerate(items))
    total_weight = sum(item[1] * individual[i] for i, item in enumerate(items))
    if total_weight > max_weight:
        return 0
    else:
        return total_value

def selection(population):
    return random.choice(population)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(individual):
    mutated_individual = list(individual)
    mutation_point = random.randint(0, len(individual) - 1)
    mutated_individual[mutation_point] = not mutated_individual[mutation_point]
    return mutated_individual

def generate_individual(items):
    return [random.randint(0, item[3]) for item in items]

def read_items_data(file_path):
    with open(file_path) as f:
        max_weight = int(f.readline().strip())
        f.readline()  # Ignore headers
        items = []
        for line in f:
            item_data = line.strip().split(",")
            name = item_data[0]
            weight = float(item_data[1])
            value = int(item_data[2])
            n_items = int(item_data[3])
            items.append((name, weight, value, n_items))
        return items, max_weight

# Read the items data from file
items, max_weight = read_items_data("items_data.txt")

# Generate the initial population
population = [generate_individual(items) for _ in range(pop_size)]

# Evolve the population over generations
for i in range(generations):
    print("Generation {}...".format(i))
    
    # Evaluate the fitness of each individual in the population
    fitnesses = [(individual, fitness(individual, items, max_weight)) for individual in population]
    
    # Sort the individuals by fitness in descending order
    fitnesses.sort(key=lambda x: x[1], reverse=True)
    
    # Select the elite individuals for the next generation
    elite = [individual for individual, fitness in fitnesses[:elite_size]]
    
    # Select the parents for the next generation
    parents = [selection(population) for _ in range(pop_size - elite_size)]
    
    # Create the offspring for the next generation through crossover and mutation
    offspring = []
    for parent1, parent2 in zip(parents[::2], parents[1::2]):
        child1, child2 = crossover(parent1, parent2)
        offspring.append(mutation(child1) if random.random() < mutation_rate else child1)
        offspring.append(mutation(child2) if random.random() < mutation_rate else child2)
    
    # Create the next generation by combining the elite individuals and the offspring
    population = elite + offspring
    
    # Print the fitness of the best individual in the population
    best_fitness = fitnesses[0][1]
    print("Best fitness: {}".format(best_fitness))
