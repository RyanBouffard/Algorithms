

class Term:
    ''' A term is a symbol (a string) that may be negated. '''

    def __init__(self, theTerm):
        ''' The parameter, theTerm, is a string symbol.  It may be preceded
        by a ~ meaning that the term is negated. '''
        if theTerm[0] == '~':
            self.term = theTerm[1:]
            self.neg = True
        else:
            self.term = theTerm
            self.neg = False

    def isTrue(self, assignments):
        ''' assignments is a list of
        truth values for each symbol from
        the list '0', '1', '2', ...'''
        index = int(self.term)
        value = assignments[index]
        if self.neg:
            return not value
        else:
            return value

    def __str__(self):
        if self.neg:
            return '~' + self.term
        else:
            return self.term
