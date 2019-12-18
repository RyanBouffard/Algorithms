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

def hillClimb(clauses, guess):
    ''' Finds a new "guess" that is better than the input "guess".  Each possible
    "new guess" is made by flipping one variable in "guess" from True to False (or
    vice versa).
    Returns False if it can't find a better guess.  '''

    # assume the minimum is the current guess
    minValue = [(Clause.countTrue(clauses, guess), guess)]

    # if the current guess solves the problem, don't try any others
    if Clause.countTrue(clauses, guess) == len(clauses):
        return guess

    foundBetter = False
    for i in range(0, len(guess)):
        newGuess = guess.copy()

        # the next statement flips the True/False value at index i
        newGuess[i] = True if guess[i] == False else False
        count = Clause.countTrue(clauses, newGuess) # see how good the new guess is

        if count == len(clauses): # perfect.   No need to try anything else.
            return newGuess

        if count > minValue[0][0]: # better than the best so far
            minValue = [(count, newGuess)]
            foundBetter = True
        elif count == minValue[0][0] and foundBetter: # equal to the best so far
            minValue.append((count, newGuess))

    if not foundBetter:
        return False

    # pick one at random
    index = random.randint(0, len(minValue) - 1)
    return minValue[index][1]


def simulatedAnnealing(sol,score):

    old_score = score
    if old_score == m:
        return sol,old_score

    temperature = 1.0
    temperature_min = 0
    alpha = 0.9
    # i= 0
    print("old_score:",old_score,"/",m)
    print(sol, old_score)
    # solution = randomGuess
    i = 0
    while i <= 100 and temperature > temperature_min:
        new_sol = hillClimb(allClauses, sol)
        if new_sol == False:
            # print("found it")
            break
        new_score = Clause.countTrue(allClauses, new_sol)
        if new_score == m:
            # print("Answer:",new_sol)
            break
        # print(new_score)
        ap = acceptance_probability(old_score, new_score, temperature)
        if ap < random.random():
            sol = new_sol
            old_score = new_score
        print(new_sol,new_score)
        print(temperature , temperature_min)
        i += 1
        temperature = temperature * alpha

    return sol,new_score


def acceptance_probability(old_score, new_score, temperature):
    accept_prob = 2.71828**((old_score - new_score ) / temperature)
    # print("old_score:", old_score, "new_score:", new_score, "temperature", temperature)
    # print("accept_prob:",accept_prob)
    return accept_prob



n = 10
assignments = n * [True]
randomAssignment(assignments)
m = 10*n
allClauses = []
for i in range(m):
    allClauses.append(Clause.randomClauseThatIsSatisfiable(n, assignments))

randomGuess = [True if random.randint(1, 2) == 1 else False for _ in range(n)]
old_score = Clause.countTrue(allClauses, randomGuess)
a = simulatedAnnealing(randomGuess,old_score)
print("final guess/score:",a)
print("began with this guess/score:",randomGuess,old_score)