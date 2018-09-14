import copy
import sys
sys.path.append( '../..')
from AssertSbox import AssertSbox

class Present_like(object):
    def __init__(self, sboxName, sbox, sboxDim, dim, r, numberOfSbox, permutation, inV, outV):
        self._sbox = AssertSbox( sboxName + 'K', sbox, sboxDim, r, numberOfSbox) # the index is on the sboxName
        self._permutation = permutation
        self._round = r
        self._dim = dim
        self._sboxDim = sboxDim
        self._numberOfSbox = numberOfSbox
        self._constrs = []
        self._inV = inV
        self._outV = outV
        self._vars = dict()
        self._constrs += self._sbox.get_asserts_declares()

    def _addConstr(self, s):
        self._constrs.append( s )

    def _declare(self, x, num= 1):
        return '%s:BITVECTOR(%d);' % (x, num)

    def _concate(self, X, res):
        assert X
        model = 'ASSERT '
        for x in X:
            model += '%s@'%x
        model = '%s=%s;' % ( model[0:-1], res )
        return model

    def _orconcate(self, ORs, Candidate ):
        s = 'ASSERT '
        for i in range(len(ORs)):
            if i < len(ORs)- 1:
                s += '%s = %s OR ' % ( Candidate, ORs[i])
            else:
                s += '%s = %s;' % (Candidate, ORs[i])
        return s

    def _declareVariables(self):
        #declare the round variables
        self._vars['PRESENT_K'] = [ [None for x in range(self._dim) ] for x in range(self._round + 1) ]
        for r in range(self._round + 1):
            for p in range(self._dim):
                varName = 'PRESENT_K_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['PRESENT_K'][r][p] = varName


    def _passSboxLayer(self, inL, outL, r):
        assert len(inL) == len(outL) == self._dim
        for p in range(self._numberOfSbox):
            self._addConstr( self._sbox.build_constrs( 
                inL[self._sboxDim * p : self._sboxDim * (p+ 1) ],
                outL[self._sboxDim * p : self._sboxDim * (p + 1)],
                r, p))


    def _passLinearLayer(self, inL):                                                                                                                                                                                                                                                       
        tmp = copy.deepcopy( inL )
        for index, value in enumerate(self._permutation):
            inL[value] = tmp[index]

    def _genRoundConstrs(self):
        for r in range(self._round):

            self._passSboxLayer(self._vars['PRESENT_K'][r], self._vars['PRESENT_K'][r+1], r)
            self._passLinearLayer(self._vars['PRESENT_K'][r + 1])
    
    def _genInitialConstrs(self):
        for i in range(self._dim ):
            if i in self._inV:
                self._addConstr( 'ASSERT %s = 0bin1;' % self._vars['PRESENT_K'][0][i] ) 
            else:
                self._addConstr( 'ASSERT %s = 0bin0;' % self._vars['PRESENT_K'][0][i] )

        for i in range(self._dim ):
            if i in self._outV:
                self._addConstr( 'ASSERT %s = 0bin1;' % self._vars['PRESENT_K'][self._round][i] ) 
            else:
                self._addConstr( 'ASSERT %s = 0bin0;' % self._vars['PRESENT_K'][self._round][i] )

        self._addConstr( 'QUERY FALSE;')
    
    def getConstrs(self):
        self._declareVariables()
        self._genRoundConstrs()
        self._genInitialConstrs()
        return self._constrs


def main():
    sbox = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]
    perm = [  0, 16, 32, 48,  1, 17, 33, 49,  2, 18, 34, 50,  3, 19, 35, 51, 
              4, 20, 36, 52,  5, 21, 37, 53,  6, 22, 38, 54,  7, 23, 39, 55, 
              8, 24, 40, 56,  9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59,
             12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]
    inV = [ x for x in range(15)]
    outV = [ int(sys.argv[2] )]
    ROUND = int(sys.argv[1] )
    #def __init__(self, sboxName, sbox, sboxDim, dim, r, numberOfSbox, permutation, inV, outV):
    present = Present_like('PRESENT_SBOX', sbox, 4, 64, ROUND, 16, perm, inV, outV )
    print( '\n'.join( present.getConstrs() ) )

if __name__ == '__main__':
    main()

            

    


    

        
        


