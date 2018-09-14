import datetime
from STPDivision import *
from ModularAdd import *
from L_ModularAdd import *

class Speck(STPDivision):
    def __init__(self, model_round, bits, num1, num2, inV, outV ):
        super(Speck, self).__init__()
        self._round = model_round
        self._bits = bits
        self._bit1 = num1
        self._bit2 = num2
        self._inV = inV
        self._outV = outV
        ModularAdd.clearTags()
        L_ModularAdd.clearTags()

    def _KdeclareVariables(self):
        self._vars['KX'] = [ [None for x in range(self._bits)] 
                for x in range(self._round + 1)]
        for r in range(self._round + 1):
            for p in range(self._bits):
                varName = 'KX_%d_%d' % (r, p)
                self._addConstr( self._declare(varName ) )
                self._vars['KX'][r][p] = varName

        self._vars['KA'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round)]
        for r in range(self._round):
            for p in range(self._bits // 2):
                varName = 'KA_%d_%d' % (r, p)
                self._addConstr( self._declare(varName ) )
                self._vars['KA'][r][p] = varName
    
        self._vars['KB'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round)]
        for r in range(self._round):
            for p in range(self._bits // 2):
                varName = 'KB_%d_%d' % (r, p)
                self._addConstr( self._declare(varName ) )
                self._vars['KB'][r][p] = varName

        self._vars['KC'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round)]
        for r in range(self._round):
            for p in range(self._bits // 2):
                varName = 'KC_%d_%d' % (r, p)
                self._addConstr( self._declare(varName ) )
                self._vars['KC'][r][p] = varName

        self._vars['KD'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round)]
        for r in range(self._round):
            for p in range(self._bits // 2):
                varName = 'KD_%d_%d' % (r, p)
                self._addConstr( self._declare(varName ) )
                self._vars['KD'][r][p] = varName

    def _LdeclareVariables(self):
        self._vars['LX'] = [ [None for x in range(self._bits)] 
                for x in range(self._round + 1)]
        for r in range(self._round + 1):
            for p in range(self._bits):
                varName = 'LX_%d_%d' % (r, p)
                self._addConstr( self._declare(varName ) )
                self._vars['LX'][r][p] = varName

        self._vars['LA'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round)]
        for r in range(self._round):
            for p in range(self._bits // 2):
                varName = 'LA_%d_%d' % (r, p)
                self._addConstr( self._declare(varName ) )
                self._vars['LA'][r][p] = varName
    
        self._vars['LB'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round)]
        for r in range(self._round):
            for p in range(self._bits // 2):
                varName = 'LB_%d_%d' % (r, p)
                self._addConstr( self._declare(varName ) )
                self._vars['LB'][r][p] = varName

        self._vars['LC'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round)]
        for r in range(self._round):
            for p in range(self._bits // 2):
                varName = 'LC_%d_%d' % (r, p)
                self._addConstr( self._declare(varName ) )
                self._vars['LC'][r][p] = varName

        self._vars['LD'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round)]
        for r in range(self._round):
            for p in range(self._bits // 2):
                varName = 'LD_%d_%d' % (r, p)
                self._addConstr( self._declare(varName ) )
                self._vars['LD'][r][p] = varName

    def _inter_declareVariables(self):
        #declare res of one round
        self._vars['KX_RES'] = [ [None for x in range(self._bits)] 
                for x in range(self._round) ]

        for r in range(self._round):
            for p in range(self._bits):
                varName = 'KX_RES_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['KX_RES'][r][p] = varName 

        #declare concation of X
        self._vars['KX_con'] = [  None for x in range(self._round) ]

        for r in range(self._round):
                varName = 'KX_con_%d' % (r)
                self._addConstr( self._declare( varName, self._bits ) )
                self._vars['KX_con'][r] = varName 

        #declare concation of L
        self._vars['LX_con'] = [  None for x in range(self._round) ]

        for r in range(self._round):
                varName = 'LX_con_%d' % (r)
                self._addConstr( self._declare( varName, self._bits ) )
                self._vars['LX_con'][r] = varName 

        #declare LX_ORS
        self._vars['LX_ORS'] = [  [None for x in range(self._bits//2) ]
                for x in range(self._round) ]

        for r in range(self._round):
            for p in range(self._bits//2):
                varName = 'LX_ORS_%d_%d' % (r, p)
                self._addConstr( self._declare( varName, self._bits ) )
                self._vars['LX_ORS'][r][p] = varName 

        #decalre candidates
        self._vars['candidate'] = [ None for x in range(self._round) ]

        for r in range(self._round):
                varName = 'candidate_%d' % (r)
                self._addConstr( self._declare( varName, self._bits ) )
                self._vars['candidate'][r] = varName 

        #decalre candidates
        self._vars['KX_new'] = [ None for x in range(self._round) ]

        for r in range(self._round):
                varName = 'KX_new_%d' % (r)
                self._addConstr( self._declare( varName, self._bits ) )
                self._vars['KX_new'][r] = varName 


    def __supply_K_from_L_one_round(self, 
                                KX_RES,
                                KX_con, 
                                LX, 
                                LX_con, 
                                LX_ORS, 
                                candidate,
                                KX_new,  
                                KX
                                     ):
        self._addConstr( self._concate(KX_RES, KX_con) )
        self._addConstr( self._concate(LX, LX_con) )

        for i in range(self._bits // 2):     
            self._addConstr( 'ASSERT %s = IF %s=0bin0 THEN (%s | %s) ELSE %s ENDIF;' % (
                LX_ORS[i],
                LX[i],
                LX_con, 
                self._bin( 1 << (self._bits - 1 - i), self._bits ),
                self._bin( (1 << self._bits) - 1,  self._bits )
                ))

        self._addConstr( self._or_concate( [KX_con] + LX_ORS, candidate, self._bits ) )

        m = 'ASSERT %s = IF %s[%d:%d] = %s THEN %s ELSE %s ENDIF;' % (
                    KX_new, 
                    LX_con, 
                    self._bits - 1, 
                    self._bits//2,  
                    self._bin( ( (1 << (self._bits // 2) ) - 1), self._bits//2) ,
                    KX_con,
                    candidate
                    )
        self._addConstr( m )

        self._addConstr( self._concate(KX, KX_new ) )

    def _supply_K_from_L(self):
        for r in range(self._round):
            self.__supply_K_from_L_one_round(
                                self._vars['KX_RES'][r],
                                self._vars['KX_con'][r],
                                self._vars['LA'][r] + self._vars['LC'][r], 
                                self._vars['LX_con'][r],
                                self._vars['LX_ORS'][r],
                                self._vars['candidate'][r],
                                self._vars['KX_new'][r],
                                self._vars['KA'][r] + self._vars['KC'][r]
                    )
                          
    def _declareTempVars(self, tmpVars):
        for var in tmpVars:
            self._addConstr( self._declare(var) )

    def _KgenRoundModel(self, KX, KX_RES, KA, KB, KC, KD, KX_NEXT, r):
        #the right branch splits 
        for p in range( self._bits // 2 ):
            self._addConstr( self._Kcopy(KX[p + self._bits // 2], KB[p], KX_RES[p + self._bits//2]))

        #ModularAdd, Care the input after left shift
        #shift
        TMP = KX[:self._bits//2]
        TMP = TMP[self._bits//2 - self._bit1 : ] + TMP[:self._bits// 2 - self._bit1]

        ma = ModularAdd(self._bits//2, TMP, KB, KX_RES[0:self._bits//2], 'Mod_%d'%r)
        self._declareTempVars(ma.getTempVariables() )
        self._constrs += ma.getEquations()

        # A split -> D KX_NEXT
        for p in range( self._bits // 2 ):
            self._addConstr( self._Kcopy(KA[p], KD[p], KX_NEXT[p]) )

        # KC right shift
        TMP2 = KC[self._bit2:] + KC[0:self._bit2]
        for p in range(self._bits//2):
            self._addConstr( self._Kxor(KD[p], TMP2[p], KX_NEXT[self._bits//2 + p]))

    def _KgenModel(self): 
        for r in range(self._round):
            self._KgenRoundModel(self._vars['KX'][r], 
                                 self._vars['KX_RES'][r],
                                 self._vars['KA'][r], 
                                 self._vars['KB'][r], 
                                 self._vars['KC'][r], 
                                 self._vars['KD'][r], 
                                 self._vars['KX'][r + 1],
                                 r)
            
    def _LgenRoundModel(self, LX, LA, LB, LC, LD, LX_NEXT, r):
        #the right branch splits 
        for p in range( self._bits // 2 ):
            self._addConstr( self._Lcopy(LX[p + self._bits // 2], LB[p], LC[p]))

        #ModularAdd, Care the input after left shift
        #shift
        TMP = LX[:self._bits//2]
        TMP = TMP[self._bits // 2 - self._bit1:] + TMP[:self._bits // 2 - self._bit1]
        #@TMP = LX[:self._bits//2][self._bits//2 - self._bit1:] + LX[:self._bits//2][0:self._bits//2 - self._bit1]
        ma = L_ModularAdd(self._bits//2, TMP, LB, LA, 'Mod_%d'%r)
        self._declareTempVars(ma.getTempVariables() )
        self._constrs += ma.getEquations()

        # A split -> D KX_NEXT
        for p in range( self._bits // 2 ):
            self._addConstr( self._Lcopy(LA[p], LD[p], LX_NEXT[p]) )

        # KC right shift
        TMP2 = LC[self._bit2:] + LC[0:self._bit2]
        for p in range(self._bits//2):
            self._addConstr( self._Lxor( LD[p], TMP2[p], LX_NEXT[self._bits//2 + p]))

    def _LgenModel(self): 
        for r in range(self._round):
            self._LgenRoundModel(self._vars['LX'][r], 
                                 self._vars['LA'][r], 
                                 self._vars['LB'][r], 
                                 self._vars['LC'][r], 
                                 self._vars['LD'][r], 
                                 self._vars['LX'][r + 1],
                                 r)
    def _genInitialConstr(self):
        for p in range(self._bits):
            self._addConstr(
                    self._equal( self._vars['KX'][0][p], '0bin1')
                    )

        for p in range(self._bits):
            if self._inV[p]:
                self._addConstr(
                        self._equal( self._vars['LX'][0][p], '0bin1')
                        )
            else:
                self._addConstr(
                        self._equal(self._vars['LX'][0][p], '0bin0' )
                        )

        for p in range(self._bits):
            if self._outV[p]:
                self._addConstr(
                          self._equal( self._vars['KX'][self._round][p], '0bin1')
                          )
            else:
                self._addConstr(
                          self._equal( self._vars['KX'][self._round][p], '0bin0' )
                          )

        self._addConstr( 'QUERY FALSE;' )
        #self._addConstr( 'COUNTEREXAMPLE;' )

    def getModel(self):
        self._KdeclareVariables()
        self._LdeclareVariables()
        self._inter_declareVariables()
        self._KgenModel()
        self._LgenModel()
        self._supply_K_from_L()
        self._genInitialConstr()

        return self._constrs

def main():
    BITLENGTH = 32
    ROUND = 6
    BIT1 = 7
    BIT2 = 2  

    start = datetime.datetime.now()

    #       0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
    for i in range(BITLENGTH):
        #inV = [0] + [ 1 for x in range(BITLENGTH - 1)]
        inV = [1 for x in range(BITLENGTH)]
        inV[i] = 0

        for j in range(BITLENGTH):
            outV = [ 0 for x in range(BITLENGTH)]
            outV[j] = 1


            f = open('cvc_%d/%d_%d.cvc' % (BITLENGTH, i, j), 'w')

            speck = Speck(ROUND, BITLENGTH, BIT1, BIT2, inV, outV)

            f.write('\n'.join(speck.getModel() ) )

            f.close()

    filename = 'result%d_%d.res' % (BITLENGTH, ROUND) 
    f = open( filename , 'w')
    f.write( 'SPECK %d \nROUND %d\n' % (BITLENGTH, ROUND))
    f.close()

    os.system('bash excuteCVC.sh %d %s' %(BITLENGTH, filename))

    end = datetime.datetime.now()
    f = open( filename , 'a')
    f.write( '%d'% (end- start).seconds )
    f.close()

if __name__ == '__main__':
    main()
                



