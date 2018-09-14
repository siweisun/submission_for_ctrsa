import os
import datetime
from STPDivision import *
import sys
K = 0
L = 1

K_OR_L = int ( sys.argv[4] )

class Simon(STPDivision):
    def __init__(self, model_round, bits,rotateNum1, rotateNum2, rotateNum3, inV, outV  ):
        super(Simon, self).__init__()
        self._round = model_round
        self._bits = bits
        self._inV = inV
        self._outV = outV
        self._const1 = rotateNum1
        self._const2 = rotateNum2
        self._const3 = rotateNum3

    def __KdeclareVariables(self):
        # declare round bit variables
        self._vars['KX'] = [ [None for x in range(self._bits)] 
                for x in range(self._round + 1) ]

        for r in range(self._round + 1):
            for p in range(self._bits):
                varName = 'KX_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['KX'][r][p] = varName 

        # declare intermediate variables
        # X -> (A, D)
        # D -> (B, E)
        # E -> (C, Y)
        self._vars['KA'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['KB'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['KC'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['KD'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['KE'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['KF'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['KG'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]

        for r in range(self._round):
            for p in range(self._bits // 2):
                varName = 'KA_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['KA'][r][p] = varName

                varName = 'KB_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['KB'][r][p] = varName
    
                varName = 'KC_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['KC'][r][p] = varName

                varName = 'KD_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['KD'][r][p] = varName

                varName = 'KE_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['KE'][r][p] = varName

                varName = 'KF_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['KF'][r][p] = varName

                varName = 'KG_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['KG'][r][p] = varName

    def __LdeclareVariables(self):
        # declare round bit variables
        self._vars['LX'] = [ [None for x in range(self._bits)] 
                for x in range(self._round + 1) ]

        for r in range(self._round + 1):
            for p in range(self._bits):
                varName = 'LX_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['LX'][r][p] = varName 

        # declare intermediate variables
        # X -> (A, D)
        # D -> (B, E)
        # E -> (C, Y)
        self._vars['LA'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['LB'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['LC'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['LD'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['LE'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['LF'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]
        self._vars['LG'] = [ [None for x in range(self._bits // 2)] 
                for x in range(self._round) ]

        for r in range(self._round):
            for p in range(self._bits // 2):
                varName = 'LA_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['LA'][r][p] = varName

                varName = 'LB_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['LB'][r][p] = varName
    
                varName = 'LC_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['LC'][r][p] = varName

                varName = 'LD_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['LD'][r][p] = varName

                varName = 'LE_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['LE'][r][p] = varName

                varName = 'LF_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['LF'][r][p] = varName

                varName = 'LG_%d_%d' % (r, p)
                self._addConstr( self._declare( varName ) )
                self._vars['LG'][r][p] = varName

    def __KgenCopyConstrs(self):
        for r in range(self._round):
            for p in range(self._bits // 2):
                self._addConstr(
                        self._Kcopy( self._vars['KX'][r][p], 
                               self._vars['KA'][r][p], 
                               self._vars['KD'][r][p]  ) 
                        )
            
                self._addConstr(
                        self._Kcopy( self._vars['KD'][r][p], 
                               self._vars['KB'][r][p], 
                               self._vars['KE'][r][p]  ) 
                        )

                self._addConstr(
                        self._Kcopy( self._vars['KE'][r][p], 
                               self._vars['KC'][r][p], 
                               self._vars['KX_RES'][r][p + self._bits//2]  ) 
                        )

    def __LgenCopyConstrs(self):
        for r in range(self._round):
            for p in range(self._bits // 2):
                self._addConstr(
                        self._Lcopy( self._vars['LX'][r][p], 
                               self._vars['LA'][r][p], 
                               self._vars['LD'][r][p]  ) 
                        )
            
                self._addConstr(
                        self._Lcopy( self._vars['LD'][r][p], 
                               self._vars['LB'][r][p], 
                               self._vars['LE'][r][p]  ) 
                        )

                self._addConstr(
                        self._Lcopy( self._vars['LE'][r][p], 
                               self._vars['LC'][r][p], 
                               self._vars['LX'][r +1][p + self._bits//2]  ) 
                        )

    def __KgenAndConstrs( self ):
        for r in range(self._round):
            for p in range(self._bits // 2):
                self._addConstr(
                        self._Kand( self._vars['KA'][r][(p + self._const1) % (self._bits // 2)],
                            self._vars['KB'][r][(p + self._const2) % (self._bits // 2)], 
                            self._vars['KF'][r][p] )
                        )

    def __LgenAndConstrs( self ):
        for r in range(self._round):
            for p in range(self._bits // 2):
                self._addConstr(
                        self._Land( self._vars['LA'][r][(p + self._const1) % (self._bits // 2)],
                            self._vars['LB'][r][(p + self._const2) % (self._bits // 2)], 
                            self._vars['LF'][r][p] )
                        )

    def __KgenXorConstrs(self):
        for r in range(self._round):
            for p in range(self._bits // 2):
                self._addConstr( 
                        self._Kxor( self._vars['KF'][r][p],
                            self._vars['KC'][r][(p + self._const3) % (self._bits // 2)], 
                            self._vars['KG'][r][p] )
                        )

                self._addConstr( 
                        self._Kxor( self._vars['KG'][r][p], 
                            self._vars['KX'][r][p + self._bits // 2], 
                            self._vars['KX_RES'][r][p] )
                        )
                
    def __LgenXorConstrs(self):
        for r in range(self._round):
            for p in range(self._bits // 2):
                self._addConstr( 
                        self._Lxor( self._vars['LF'][r][p],
                            self._vars['LC'][r][(p + self._const3) % (self._bits // 2)], 
                            self._vars['LG'][r][p] )
                        )

                self._addConstr( 
                        self._Lxor( self._vars['LG'][r][p], 
                            self._vars['LX'][r][p + self._bits // 2], 
                            self._vars['LX'][r + 1][p] )
                        )
        

    def __supply_K_from_L_one_round(self, 
                                KX_RESS,
                                KX_con, 
                                LX, 
                                LX_con, 
                                LX_ORS, 
                                candidate,
                                KX_new,  
                                KX
                                     ):
        self._addConstr( self._concate(KX_RESS, KX_con) )
        self._addConstr( self._concate(LX, LX_con) )

        for i in range(self._bits // 2):     
            self._addConstr( 'ASSERT %s = IF %s=0bin0 THEN (%s | %s) ELSE %s ENDIF;' % (
                LX_ORS[i],
                LX[i],
                LX_con, 
                self._bin( 1 << (self._bits - 1 - i), self._bits ),
                self._bin( (1 << self._bits) - 1,  self._bits )
                ))

        self._addConstr( self._or_concate( [KX_con] + LX_ORS, KX_new, self._bits ) )

        #m = 'ASSERT %s = IF %s[%d:%d] = %s THEN %s ELSE %s ENDIF;' % (
        #            KX_new, 
        #            LX_con, 
        #            self._bits - 1, 
        #            self._bits//2,  
        #            self._bin( ( (1 << (self._bits // 2) ) - 1), self._bits//2) ,
        #            KX_con,
        #            candidate
        #            )
        #self._addConstr( m )
        #self._addConstr( 'ASSERT %s = %s OR %s = %s;'% ( KX_new, KX_con, KX_new, LX_con ) )

        self._addConstr( self._concate(KX, KX_new ) )

    def __supply_K_from_L(self):
        for r in range(self._round):
            self.__supply_K_from_L_one_round(
                                self._vars['KX_RES'][r],
                                self._vars['KX_con'][r],
                                self._vars['LX'][r+1], 
                                self._vars['LX_con'][r],
                                self._vars['LX_ORS'][r],
                                self._vars['candidate'][r],
                                self._vars['KX_new'][r],
                                self._vars['KX'][r+1]
                    )
                          
    def __inter_declareVariables(self):
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

    def __genInitialConstrs(self ):
        for p in range(self._bits):
            self._addConstr(
                        self._equal(self._vars['KX'][0][p], '0bin1' )
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

        if K_OR_L == K:
            for p in range(self._bits):
                if self._outV[p]:
                    self._addConstr(
                          self._equal( self._vars['KX'][self._round][p], '0bin1')
                          )
                else:
                    self._addConstr(
                          self._equal( self._vars['KX'][self._round][p], '0bin0' )
                          )
        if K_OR_L == L:
            for p in range(self._bits):
                if self._outV[p]:
                    self._addConstr(
                          self._equal( self._vars['LX'][self._round][p], '0bin1')
                          )
                else:
                    self._addConstr(
                          self._equal( self._vars['LX'][self._round][p], '0bin0' )
                          )

        self._addConstr( 'QUERY FALSE;' )
            
    def getModel(self):
        self.__KdeclareVariables()
        self.__LdeclareVariables()
        self.__inter_declareVariables()

        self.__KgenCopyConstrs()
        self.__LgenCopyConstrs()

        self.__KgenAndConstrs()
        self.__LgenAndConstrs()

        self.__KgenXorConstrs()
        self.__LgenXorConstrs()

        self.__supply_K_from_L()

        self.__genInitialConstrs()
        
        return self._constrs

if __name__ == '__main__':
    BITLENGTH = int( sys.argv[1] )
    ROUND = int( sys.argv[2] )
    BIT1 = 1
    BIT2 = 8
    BIT3 = 2
    
    start = datetime.datetime.now()
    # 0 for constant and 1 for active bits of plaintexts
    inV = [ 1 for x in range(BITLENGTH)]
    inV[0] = 0
    # the output bit to check
    outV = [ 0 for x in range(BITLENGTH) ]
    outV[int(sys.argv[3]) ] = 1

    simon = Simon(ROUND, BITLENGTH,BIT1,BIT2,BIT3, inV, outV)


    # print the model for SIMON_BITLENGTH in a cvc language
    print('\n'.join(simon.getModel() ) )


