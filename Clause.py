import random
from Term import *

class Clause:
    ''' A Clause is the conjunction (OR) of 3 terms. '''

    def __init__(self, t1, t2, t3):
        ''' Store the three terms in a list. '''
        self.terms = [t1, t2, t3]

    def isTrue(self, assignments):
        ''' The clause is True if any of its terms are True.
        False, otherwise. '''
        if self.terms[0].isTrue(assignments):
            return True
        elif self.terms[1].isTrue(assignments):
            return True
        else:
            return self.terms[2].isTrue(assignments)


    def __str__(self):
        s = ""
        for t in self.terms:
            s += str(t) + " "
        return s

    def randomClause(n):
        ''' Generate a random clause of 3 unique symbols (possibly negated).
         n is the number of variables.   '''
        if n < 3:
            raise Exception("Too few variables.")


        ''' Make a random clause with different terms with the names
        '0', '1', '2', ..., '(n-1)' '''
        listOfTerms = []
        while len(listOfTerms) < 3:
            t = str(random.randint(0, n-1))
            if t not in listOfTerms:
                listOfTerms.append(t)

        ''' negate the terms with a probability of 0.5'''
        for i in range(len(listOfTerms)):
            if random.randint(1,2) == 1:
                listOfTerms[i] = '~' + listOfTerms[i]

        ''' now, make the clause '''
        theClause = Clause(Term(listOfTerms[0]), Term(listOfTerms[1]), Term(listOfTerms[2]))
        return theClause


    def randomClauseThatIsSatisfiable(n, assignments):
        ''' Generate a clause from n symbols that is true
        given the list of associated truth values in assignments.  '''
        done = False
        while not done:
            theClause = Clause.randomClause(n)
            if theClause.isTrue(assignments):
                done = True

        return theClause


    def allClausesTrue(clauses, assignments):
        ''' Returns true if all of the clauses evaluate to True
        given the set of truth assignments.
        False, otherwise.  '''
        for clause in clauses:
            if not clause.isTrue(assignments):
                return False
        return True

    def countTrue(clauses, assignment):
        ''' Return a count of how many clauses are True given the
        truth assignments.  '''
        count = 0
        for clause in clauses:
            if clause.isTrue(assignment):
                count += 1
        return count
