import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + ' ') for _ in range(length))

def fitness(target, candidate):
    return sum(1 for a, b in zip(target, candidate) if a == b)

def evolve_population(target, population_size, mutation_rate):
    population = [generate_random_string(len(target)) for _ in range(population_size)]
    
    generation = 1
    while True:
        sorted_population = sorted(population, key=lambda x: -fitness(target, x))
        best_candidate = sorted_population[0]
        
        print(f"Generation {generation}: {best_candidate} (Fitness: {fitness(target, best_candidate)})")
        
        if best_candidate == target:
            print(f"Found the target string '{target}' in {generation} generations!")
            break
        
        new_population = []
        for _ in range(population_size):
            parent1 = random.choice(sorted_population)
            parent2 = random.choice(sorted_population)
            midpoint = random.randint(0, len(target))
            child = parent1[:midpoint] + parent2[midpoint:]
            
            for i in range(len(child)):
                if random.random() < mutation_rate:
                    child = child[:i] + random.choice(string.ascii_letters + ' ') + child[i+1:]
            
            new_population.append(child)
        
        population = new_population
        generation += 1

if __name__ == "__main__":
    target_string = "Hello, World!"
    population_size = 100
    mutation_rate = 0.01
    evolve_population(target_string, population_size, mutation_rate)