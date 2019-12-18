import random, time

from Term import *
from Clause import *


def randomAssignment(assignments):
    ''' Randomly assign True or False to each element in the list
    assignments.  '''
    for i in range(len(assignments)):
        if random.randint(1,2) == 1:
            assignments[i] = False
        else:
            assignments[i] = True


def GeneticAlgorithm(fitnessWanted):
    population_size = 100
    generation = 1

    found = False
    population = []

    i=0
    while i < population_size:
        randomGuess = [True if random.randint(1, 2) == 1 else False for _ in range(n)]
        fitness = Clause.countTrue(allClauses, randomGuess)
        solution = randomGuess,fitness
        population.append(solution)
        i +=1



    while not found:
        population = sorted(population, key=lambda tup: tup[1], reverse=True)

        # print("generation:",generation)
        # for x in population:
        #     print(x)

        if population[0][1] == fitnessWanted:
            # print("got it, generation:",generation)
            found = True
            return generation
        # break
        # print("best", population[len(population) - 1])
        # if generation == 200:
        #     return population[len(population) - 1]

        new_generation = []
        # least_fit = (population[0:5])
        # most_fit = (population[(len(population)-5):len(population)])
        # for x in least_fit:
        #     print("least fit:",x)
        # for x in most_fit:
        #     print("most fit:",x)
        # break
        bestFit = population[:(len(population) // 2)]
        for _ in range(population_size // 2):
            parent1 = random.choice(bestFit)
            parent2 = random.choice(bestFit)
            child = mate(parent1, parent2)
            new_generation.append(child)
        # for _ in range(len(least_fit)):
        #     parent1 = random.choice(least_fit)
        #     parent2 = random.choice(most_fit)
        #     child = mate(parent1,parent2)
        #     new_generation.append(child)

        population = bestFit.copy()
        population = population + new_generation
        # population = sorted(population, key=lambda tup: tup[1])

        generation += 1
        # print("generation",generation,"\t","most fit:",population[len(population) - 1][1],"\t","fitness wanted:",fitnessWanted)

        # break
    return generation


def mate(parent1, parent2):
    child_solution = []
    # print("parent1",parent1)
    # print("LENGTH OF PARENT 1:",len(parent1[0]))
    for i in range(len(parent1[0])):
        # print(i)
        mutation_prob = random.random()
        if mutation_prob < 0.45:
            child_solution.append(parent1[0][i])

        elif mutation_prob < 0.9:
            child_solution.append(parent2[0][i])

        elif mutation_prob >= 0.9:
            choice = random.randint(1, 2)
            if choice == 1:
                child_solution.append(True)
            else:
                child_solution.append(False)

    # print("CHILD SOLUTION:",child_solution)
    fitness = Clause.countTrue(allClauses, child_solution)
    final_child_solution = child_solution, fitness
    return final_child_solution


numExperi = 10
print("\n\n""n\t","generationSum/numExperi")
for n in range(60,101,1):
    generationSum = 0
    for i in range(numExperi):
        assignments = n * [True]
        randomAssignment(assignments)
        m = 10*n
        allClauses = []
        for i in range(m):
            allClauses.append(Clause.randomClauseThatIsSatisfiable(n, assignments))
        result = GeneticAlgorithm(m)
        generationSum += result

# print("\n\nresult:",result)
    print(n,"\t",generationSum / numExperi)

