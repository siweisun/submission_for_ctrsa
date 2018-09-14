from .Term import *   

class Polynomial(object):
    ZERO_TERM = ConstTerm(0)
    ONE_TERM = ConstTerm(1)
    def __init__(self, poly_str, dimension ):
        self.__terms = set()
        self.__polyStr = poly_str.replace(' ', '').replace('\n', '')
        self.__dimension = dimension
        self.__parse()

    def __parse(self):
        if not self.__polyStr:
            return 
        if self.__polyStr == '0' or self.__polyStr == '1':
            self.__terms.add( ConstTerm(int(self.__polyStr) ) )
            return 
        terms = self.__polyStr.split('+')
        for term in terms:
            if term == '0' or term == '1':
                self.__terms.add( ConstTerm( int(term) )  )
            else:
                t = Term(term[0], self.__dimension)
                self.__terms.add( t.parseTerm( term, self.__dimension ) )

    def getTerms(self):
        return self.__terms

    def deleteTerm(self, term):
        self.__terms.remove( term )
        
    def addTerm(self, term):
        self.__terms.add( term )

    def getDimension( self ):
        return self.__dimension


    def __genPoly_from_trueTable(self):
        pass

    def __add__(self, other):
        assert self.__dimension == other.getDimension()
        dim = self.__dimension

        f = Polynomial('', dim)

        for x in other.getTerms():
            if x not in f.getTerms():
                f.addTerm(x)
            else:
                f.deleteTerm(x)

        for x in self.__terms:
            if x not in f.getTerms():
                f.addTerm(x)
            else:
                f.deleteTerm(x)
        return f
    
    def __mul__(self, other):
        assert self.__dimension == other.getDimension()
        dim = self.__dimension

        if Polynomial.ZERO_TERM in self.__terms or \
           Polynomial.ZERO_TERM in other.getTerms():
            return Polynomial('0', dim )

        f = Polynomial('', dim)

        for term_1 in self.__terms:
            for term_2 in other.__terms:
                newTerm = term_1 * term_2
                if newTerm in f.getTerms():
                    f.deleteTerm( newTerm )
                else:
                    f.addTerm( newTerm )
        return f

    def __str__(self):
        s = ''
        for term in self.__terms:
            s += str( term ) + ' + '
        return s[0:-2]

    def isContain(self, term):
        return term in self.__terms

    def containTermSet(self, vecSet, number_of_bit):
        for vec in vecSet:
            vecValue = vec.value
            if vecValue == 0:
                t = ConstTerm(vecValue)
            #print ('number_of_bit', number_of_bit)
            else:
                t = Term('x', number_of_bit, vecValue)
            if self.isContain(t):
                return True
        else:
            return False
        

def main():
    term = Term('x', 8, term_str = 'x3x2x1')
    term_cover = Term('x', 8, term_str='x3x2x1x7')
    p = Polynomial('x3x2x1 + 1', 8)
    print (p.isContain(term))

if __name__ == '__main__':
        main()


