# This class transform a sbox into polynomial
from .Term import *
from .Polynomial import *

class Sbox(object):
    def __init__(self, valueList, input_dim, output_dim):
        self.values = valueList
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.trueTables = []
        self.__genTrueTables()
        self.polynomials = []
        self.__genPolys()

    def getDimension(self):
        return (self.input_dim, self.output_dim )
        
    def getPolynomilas(self):
        return self.polynomials

    def __genTrueTables(self):
        for i in range(self.output_dim):
            trueTable = []
            for j in range(2 ** self.input_dim):
                trueTable.append(
                    self.values[j] >> (self.output_dim - 1 - i) & 1 )
            self.trueTables.append( trueTable )

    def __genPoly_from_vector(self, vector, dim):
        f = Polynomial('1', dim)
        for i in range(dim):
            if vector >> ( dim - 1 - i ) & 1:
                s = 'x%d' % ( dim - 1 - i )
                f *= Polynomial( s , dim )
            else:
                s = '1+x%d' % ( dim - 1 - i )
                f *= Polynomial( s, dim )
        return f

    def __genPoly_from_trueTable(self, trueTable, in_dim):
        f = Polynomial( '', in_dim )
        for i in range(len(trueTable)):
            if trueTable[i]:
                f += self.__genPoly_from_vector( i, in_dim )
        return f

    def __genPolys(self):
        for i in range(self.output_dim):
            self.polynomials.append( 
                    self.__genPoly_from_trueTable( self.trueTables[i], self.input_dim ) 
                    )


def main():
    sbox = [ 12, 5, 6, 11 , 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2 ]
    s = Sbox(sbox, 4, 4)

    for poly in s.polynomials:
        print ( str(poly) )
    
if __name__ == '__main__':        
    main()
            





