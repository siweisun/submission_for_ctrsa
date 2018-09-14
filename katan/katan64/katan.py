import os
from STPDivision import *
import datetime
import sys
import copy

class KATAN(STPDivision):
    Rounds_Irregular = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]

    def __init__(self, model_round,three_round,  L1_len, L2_len, pos1, pos2, inV, outV ):
        super(KATAN, self).__init__()
        self._round = model_round
        self._round_three = three_round
        
        self._L1_len = L1_len
        self._L2_len = L2_len
        self._pos1 = pos1
        self._pos2 = pos2
        self._inV = inV
        self._outV = outV
        self._lastL1 = None
        self._lastL2 = None

    def __KdeclareVariables(self):
        # declare round bit variables
        self._vars['KX_L1'] = [ None for x in range(self._L1_len)]
        self._vars['KX_L2'] = [ None for x in range(self._L2_len)]
        for i in range(self._L1_len):
            varName = 'KX_L1_%d'%i
            self._addConstr( self._declare( varName ) )
            self._vars['KX_L1'][i] = varName 

        for i in range(self._L2_len):
            varName = 'KX_L2_%d'%i
            self._addConstr( self._declare( varName ) )
            self._vars['KX_L2'][i] = varName 

        self._vars['KX_L1_AND'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_L1_AND_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_L1_AND'][i] = varName
        self._vars['KX_L1_XOR1'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_L1_XOR1_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_L1_XOR1'][i] = varName
        self._vars['KX_L1_XOR2'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_L1_XOR2_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_L1_XOR2'][i] = varName
        self._vars['KX_NEW_L2'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_NEW_L2_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_NEW_L2'][i] = varName
        self._vars['KX_L2_AND'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_L2_AND_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_L2_AND'][i] = varName
        self._vars['KX_L2_AND1'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_L2_AND1_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_L2_AND1'][i] = varName

        self._vars['KX_L2_XOR1'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_L2_XOR1_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_L2_XOR1'][i] = varName

        self._vars['KX_L2_XOR2'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_L2_XOR2_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_L2_XOR2'][i] = varName
        self._vars['KX_NEW_L1'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_NEW_L1_%d' % i
            self._addConstr( self._declare(varName ))
 
            self._vars['KX_NEW_L1'][i] = varName
        self._vars['KX_X1_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_X1_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_X1_POST'][i] = varName
        self._vars['KX_X2_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_X2_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_X2_POST'][i] = varName
        self._vars['KX_X3_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_X3_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_X3_POST'][i] = varName
        self._vars['KX_X4_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_X4_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_X4_POST'][i] = varName
        self._vars['KX_Y1_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_Y1_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_Y1_POST'][i] = varName
        self._vars['KX_Y2_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_Y2_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_Y2_POST'][i] = varName
        self._vars['KX_Y3_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_Y3_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_Y3_POST'][i] = varName
        self._vars['KX_Y4_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_Y4_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_Y4_POST'][i] = varName
        self._vars['KX_Y5_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_Y5_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_Y5_POST'][i] = varName


        self._vars['KX_X1_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_X1_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_X1_BRANCH'][i] = varName

        self._vars['KX_X2_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_X2_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_X2_BRANCH'][i] = varName

        self._vars['KX_X3_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_X3_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_X3_BRANCH'][i] = varName

        self._vars['KX_X4_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_X4_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_X4_BRANCH'][i] = varName
        

        self._vars['KX_Y1_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_Y1_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_Y1_BRANCH'][i] = varName

        self._vars['KX_Y2_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_Y2_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_Y2_BRANCH'][i] = varName

        self._vars['KX_Y3_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_Y3_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_Y3_BRANCH'][i] = varName

        self._vars['KX_Y4_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_Y4_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_Y4_BRANCH'][i] = varName
        
        self._vars['KX_Y5_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_Y5_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['KX_Y5_BRANCH'][i] = varName

    def __LdeclareVariables(self):
        # declare round bit variables
        self._vars['LX_L1'] = [ None for x in range(self._L1_len)]
        self._vars['LX_L2'] = [ None for x in range(self._L2_len)]
        for i in range(self._L1_len):
            varName = 'LX_L1_%d'%i
            self._addConstr( self._declare( varName ) )
            self._vars['LX_L1'][i] = varName 

        for i in range(self._L2_len):
            varName = 'LX_L2_%d'%i
            self._addConstr( self._declare( varName ) )
            self._vars['LX_L2'][i] = varName 

        self._vars['LX_L1_AND'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_L1_AND_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_L1_AND'][i] = varName

        self._vars['LX_L1_XOR1'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_L1_XOR1_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_L1_XOR1'][i] = varName
        self._vars['LX_L1_XOR2'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_L1_XOR2_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_L1_XOR2'][i] = varName
        self._vars['LX_NEW_L2'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_NEW_L2_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_NEW_L2'][i] = varName
        self._vars['LX_L2_AND'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_L2_AND_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_L2_AND'][i] = varName
        self._vars['LX_L2_AND1'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_L2_AND1_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_L2_AND1'][i] = varName
        self._vars['LX_L2_XOR1'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_L2_XOR1_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_L2_XOR1'][i] = varName
        self._vars['LX_L2_XOR2'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_L2_XOR2_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_L2_XOR2'][i] = varName
        self._vars['LX_NEW_L1'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_NEW_L1_%d' % i
            self._addConstr( self._declare(varName ))

            self._vars['LX_NEW_L1'][i] = varName
        self._vars['LX_X1_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_X1_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_X1_POST'][i] = varName
        self._vars['LX_X2_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_X2_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_X2_POST'][i] = varName
        self._vars['LX_X3_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_X3_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_X3_POST'][i] = varName
        self._vars['LX_X4_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_X4_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_X4_POST'][i] = varName
        self._vars['LX_Y1_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_Y1_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_Y1_POST'][i] = varName
        self._vars['LX_Y2_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_Y2_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_Y2_POST'][i] = varName
        self._vars['LX_Y3_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_Y3_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_Y3_POST'][i] = varName
        self._vars['LX_Y4_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_Y4_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_Y4_POST'][i] = varName
        self._vars['LX_Y5_POST'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_Y5_POST_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_Y5_POST'][i] = varName

        self._vars['LX_X1_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_X1_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_X1_BRANCH'][i] = varName

        self._vars['LX_X2_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_X2_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_X2_BRANCH'][i] = varName

        self._vars['LX_X3_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_X3_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_X3_BRANCH'][i] = varName

        self._vars['LX_X4_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_X4_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_X4_BRANCH'][i] = varName
        

        self._vars['LX_Y1_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_Y1_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_Y1_BRANCH'][i] = varName

        self._vars['LX_Y2_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_Y2_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_Y2_BRANCH'][i] = varName

        self._vars['LX_Y3_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_Y3_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_Y3_BRANCH'][i] = varName

        self._vars['LX_Y4_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_Y4_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_Y4_BRANCH'][i] = varName
        
        self._vars['LX_Y5_BRANCH'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_Y5_BRANCH_%d' % i
            self._addConstr( self._declare(varName ))
            self._vars['LX_Y5_BRANCH'][i] = varName

    def __declareInter_variables( self ):
        self._vars['KX_CON'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_CON_%d' % i
            self._addConstr( self._declare(varName, self._L1_len + self._L2_len ) )
            self._vars['KX_CON'][i] = varName
        
        self._vars['LX_CON'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'LX_CON_%d' % i
            self._addConstr( self._declare(varName, self._L1_len + self._L2_len ) )
            self._vars['LX_CON'][i] = varName
        
        self._vars['LX_CANDIDATE'] = [ [None for x in range(2) ] for x in range(self._round ) ]
        for i in range(self._round):
            varName = 'LX_CANDIDATE_%d_0' % i
            self._addConstr( self._declare(varName, self._L1_len + self._L2_len) )
            self._vars['LX_CANDIDATE'][i][0] = varName

            varName = 'LX_CANDIDATE_%d_1' % i
            self._addConstr( self._declare(varName, self._L1_len + self._L2_len ) )
            self._vars['LX_CANDIDATE'][i][1] = varName

        self._vars['KX_L1_NEW_START'] = [ [None for x in range(self._L1_len) ] for x in range(self._round)]
        for i in range(self._round):
            for j in range(self._L1_len): 
                varName = 'KX_L1_NEW_START_%d_%d' % (i, j)
                self._addConstr( self._declare(varName ) )
                self._vars['KX_L1_NEW_START'][i][j] = varName


        self._vars['KX_L2_NEW_START'] = [ [None for x in range(self._L2_len) ] for x in range(self._round)]
        for i in range(self._round):
            for j in range(self._L2_len): 
                varName = 'KX_L2_NEW_START_%d_%d' % (i, j)
                self._addConstr( self._declare(varName ) )
                self._vars['KX_L2_NEW_START'][i][j] = varName

        self._vars['KX_CANDIDATE'] = [ None for x in range(self._round)]
        for i in range(self._round):
            varName = 'KX_CANDIDATE_%d' % i
            self._addConstr( self._declare(varName, self._L1_len + self._L2_len ) )
            self._vars['KX_CANDIDATE'][i] = varName

    def __KroundFunc(self, L1, L2, r):
        self._addConstr( self._Kcopy( 
                     L1[self._pos1[1]],
                     self._vars['KX_X1_POST'][r],
                     self._vars['KX_X1_BRANCH'][r] ) )

        self._addConstr( self._Kcopy( 
                     L1[self._pos1[2]],
                     self._vars['KX_X2_POST'][r],
                     self._vars['KX_X2_BRANCH'][r] ) )

        self._addConstr( self._Kcopy( 
                     L1[self._pos1[3]],
                     self._vars['KX_X3_POST'][r],
                     self._vars['KX_X3_BRANCH'][r] ) )

        self._addConstr( self._Kcopy( 
                     L2[self._pos2[1]],
                     self._vars['KX_Y1_POST'][r],
                     self._vars['KX_Y1_BRANCH'][r] ) )

        self._addConstr( self._Kcopy( 
                     L2[self._pos2[2]],
                     self._vars['KX_Y2_POST'][r],
                     self._vars['KX_Y2_BRANCH'][r] ) )

        self._addConstr( self._Kcopy( 
                     L2[self._pos2[3]],
                     self._vars['KX_Y3_POST'][r],
                     self._vars['KX_Y3_BRANCH'][r] ) )

        self._addConstr( self._Kcopy( 
                     L2[self._pos2[4]],
                     self._vars['KX_Y4_POST'][r],
                     self._vars['KX_Y4_BRANCH'][r] ) )

        self._addConstr( self._Kcopy( 
                     L2[self._pos2[5]],
                     self._vars['KX_Y5_POST'][r],
                     self._vars['KX_Y5_BRANCH'][r] ) )

        self._addConstr( self._Kand( 
                     self._vars['KX_X2_BRANCH'][r],
                     self._vars['KX_X3_BRANCH'][r],
        
                     self._vars['KX_L1_AND'][r] ) )

        self._addConstr( self._Kxor( 
                     self._vars['KX_L1_AND'][r], 
                     self._vars['KX_X1_BRANCH'][r],
                     self._vars['KX_L1_XOR1'][r]  ) )

        if KATAN.Rounds_Irregular[r]: 
            self._addConstr( self._Kcopy( 
                             L1[self._pos1[4]],
                             self._vars['KX_X4_POST'][r],
                             self._vars['KX_X4_BRANCH'][r]) )

            self._addConstr( self._Kxor( 
                     self._vars['KX_X4_BRANCH'][r],
                     self._vars['KX_L1_XOR1'][r], 
                     self._vars['KX_L1_XOR2'][r] ) )
        else:
            self._addConstr( self._equal( 
                     self._vars['KX_L1_XOR1'][r], 
                     self._vars['KX_L1_XOR2'][r]) )

        self._addConstr( self._Kxor( 
                     self._vars['KX_L1_XOR2'][r], 
                     L1[self._pos1[0]],
                     self._vars['KX_NEW_L2'][r] ))

        self._addConstr( self._Kand(
                     self._vars['KX_Y2_BRANCH'][r],
                     self._vars['KX_Y3_BRANCH'][r],
                     self._vars[ 'KX_L2_AND'][r] ) )

        self._addConstr( self._Kxor( 
                     self._vars['KX_L2_AND'][r], 
                     self._vars['KX_Y1_BRANCH'][r],
                     self._vars['KX_L2_XOR1'][r]  ) )

        self._addConstr( self._Kand( 
                     self._vars['KX_Y4_BRANCH'][r],
                     self._vars['KX_Y5_BRANCH'][r],
                     self._vars['KX_L2_AND1'][r] ) )

        self._addConstr( self._Kxor( 
                     self._vars['KX_L2_XOR1'][r], 
                     self._vars['KX_L2_AND1'][r], 
                     self._vars['KX_L2_XOR2'][r] ))

        self._addConstr( self._Kxor( 
                     self._vars['KX_L2_XOR2'][r], 
                     L2[self._pos2[0] ],
                     self._vars['KX_NEW_L1'][r] ))

    def __LroundFunc(self, L1, L2, r):
        self._addConstr( self._Lcopy( 
                     L1[self._pos1[1]],
                     self._vars['LX_X1_POST'][r],
                     self._vars['LX_X1_BRANCH'][r] ) )

        self._addConstr( self._Lcopy( 
                     L1[self._pos1[2]],
                     self._vars['LX_X2_POST'][r],
                     self._vars['LX_X2_BRANCH'][r] ) )

        self._addConstr( self._Lcopy( 
                     L1[self._pos1[3]],
                     self._vars['LX_X3_POST'][r],
                     self._vars['LX_X3_BRANCH'][r] ) )

        self._addConstr( self._Lcopy( 
                     L2[self._pos2[1]],
                     self._vars['LX_Y1_POST'][r],
                     self._vars['LX_Y1_BRANCH'][r] ) )

        self._addConstr( self._Lcopy( 
                     L2[self._pos2[2]],
                     self._vars['LX_Y2_POST'][r],
                     self._vars['LX_Y2_BRANCH'][r] ) )

        self._addConstr( self._Lcopy( 
                     L2[self._pos2[3]],
                     self._vars['LX_Y3_POST'][r],
                     self._vars['LX_Y3_BRANCH'][r] ) )

        self._addConstr( self._Lcopy( 
                     L2[self._pos2[4]],
                     self._vars['LX_Y4_POST'][r],
                     self._vars['LX_Y4_BRANCH'][r] ) )

        self._addConstr( self._Lcopy( 
                     L2[self._pos2[5]],
                     self._vars['LX_Y5_POST'][r],
                     self._vars['LX_Y5_BRANCH'][r] ) )

        self._addConstr( self._Land( 
                     self._vars['LX_X2_BRANCH'][r],
                     self._vars['LX_X3_BRANCH'][r],
        
                     self._vars['LX_L1_AND'][r] ) )

        self._addConstr( self._Lxor( 
                     self._vars['LX_L1_AND'][r], 
                     self._vars['LX_X1_BRANCH'][r],
                     self._vars['LX_L1_XOR1'][r]  ) )

        if KATAN.Rounds_Irregular[r]: 
            self._addConstr( self._Lcopy( 
                             L1[self._pos1[4]],
                             self._vars['LX_X4_POST'][r],
                             self._vars['LX_X4_BRANCH'][r]) )

            self._addConstr( self._Lxor( 
                     self._vars['LX_X4_BRANCH'][r],
                     self._vars['LX_L1_XOR1'][r], 
                     self._vars['LX_L1_XOR2'][r] ) )
        else:
            self._addConstr( self._equal( 
                     self._vars['LX_L1_XOR1'][r], 
                     self._vars['LX_L1_XOR2'][r]) )

        self._addConstr( self._Lxor( 
                     self._vars['LX_L1_XOR2'][r], 
                     L1[self._pos1[0]],
                     self._vars['LX_NEW_L2'][r] ))

        self._addConstr( self._Land(
                     self._vars['LX_Y2_BRANCH'][r],
                     self._vars['LX_Y3_BRANCH'][r],
                     self._vars[ 'LX_L2_AND'][r] ) )

        self._addConstr( self._Lxor( 
                     self._vars['LX_L2_AND'][r], 
                     self._vars['LX_Y1_BRANCH'][r],
                     self._vars['LX_L2_XOR1'][r]  ) )

        self._addConstr( self._Land( 
                     self._vars['LX_Y4_BRANCH'][r],
                     self._vars['LX_Y5_BRANCH'][r],
                     self._vars['LX_L2_AND1'][r] ) )

        self._addConstr( self._Lxor( 
                     self._vars['LX_L2_XOR1'][r], 
                     self._vars['LX_L2_AND1'][r], 
                     self._vars['LX_L2_XOR2'][r] ))

        self._addConstr( self._Lxor( 
                     self._vars['LX_L2_XOR2'][r], 
                     L2[self._pos2[0] ],
                     self._vars['LX_NEW_L1'][r] ))

    def __roundFunction(self):
        L1 = copy.deepcopy( self._vars['KX_L1'] )
        L2 = copy.deepcopy( self._vars['KX_L2'] )
        
        LL1 = copy.deepcopy( self._vars['LX_L1'] )
        LL2 = copy.deepcopy( self._vars['LX_L2'] )
        
        
        for r in range(self._round_three):
            self.__KroundFunc(L1,L2,r)
            L1[ self._pos1[1] ] = self._vars['KX_X1_POST'][r]
            L1[ self._pos1[2] ] = self._vars['KX_X2_POST'][r]
            L1[ self._pos1[3] ] = self._vars['KX_X3_POST'][r]
            if KATAN.Rounds_Irregular[r]:
                L1[ self._pos1[4] ] = self._vars['KX_X4_POST'][r]

            L2[ self._pos2[1] ] = self._vars['KX_Y1_POST'][r]
            L2[ self._pos2[2] ] = self._vars['KX_Y2_POST'][r]
            L2[ self._pos2[3] ] = self._vars['KX_Y3_POST'][r]
            L2[ self._pos2[4] ] = self._vars['KX_Y4_POST'][r]
            L2[ self._pos2[5] ] = self._vars['KX_Y5_POST'][r]

            L1 = [self._vars['KX_NEW_L1'][r] ] +  L1[:-1]
            L2 = [self._vars['KX_NEW_L2'][r] ] +  L2[:-1]
            # This is the last K vector
            # next is the L transport
            self.__LroundFunc(LL1, LL2, r)
            
            LL1[ self._pos1[1] ] = self._vars['LX_X1_POST'][r]
            LL1[ self._pos1[2] ] = self._vars['LX_X2_POST'][r]
            LL1[ self._pos1[3] ] = self._vars['LX_X3_POST'][r]
            if KATAN.Rounds_Irregular[r]:
                LL1[ self._pos1[4] ] = self._vars['LX_X4_POST'][r]

            LL2[ self._pos2[1] ] = self._vars['LX_Y1_POST'][r]
            LL2[ self._pos2[2] ] = self._vars['LX_Y2_POST'][r]
            LL2[ self._pos2[3] ] = self._vars['LX_Y3_POST'][r]
            LL2[ self._pos2[4] ] = self._vars['LX_Y4_POST'][r]
            LL2[ self._pos2[5] ] = self._vars['LX_Y5_POST'][r]

            LL1 = [self._vars['LX_NEW_L1'][r] ] +  LL1[:-1]
            LL2 = [self._vars['LX_NEW_L2'][r] ] +  LL2[:-1]
            
            if r < self._round_three - 1:
             	(L1, L2) = self.__supply_K_from_L( L1, L2, LL1, LL2, r ) 
            else: 
                (L1, L2) = self.newstart( L1, L2, LL1, LL2, r )

        for r in range(self._round_three, self._round):
            self.__KroundFunc(L1,L2,r)
            L1[ self._pos1[1] ] = self._vars['KX_X1_POST'][r]
            L1[ self._pos1[2] ] = self._vars['KX_X2_POST'][r]
            L1[ self._pos1[3] ] = self._vars['KX_X3_POST'][r]
            if KATAN.Rounds_Irregular[r]:
                L1[ self._pos1[4] ] = self._vars['KX_X4_POST'][r]

            L2[ self._pos2[1] ] = self._vars['KX_Y1_POST'][r]
            L2[ self._pos2[2] ] = self._vars['KX_Y2_POST'][r]
            L2[ self._pos2[3] ] = self._vars['KX_Y3_POST'][r]
            L2[ self._pos2[4] ] = self._vars['KX_Y4_POST'][r]
            L2[ self._pos2[5] ] = self._vars['KX_Y5_POST'][r]

            L1 = [self._vars['KX_NEW_L1'][r] ] +  L1[:-1]
            L2 = [self._vars['KX_NEW_L2'][r] ] +  L2[:-1]


        self._lastL1 = L1
        self._lastL2 = L2

    def newstart( self, L1,L2,LL1,LL2, r):
        self._constrs.append ( self._concate( L1 + L2, self._vars['KX_CON'][r] ) )
        self._constrs.append ( self._concate( LL1 + LL2, self._vars['LX_CON'][r] ) )
        
        
        # generat the new L1 and L2 
        self._constrs.append( 'ASSERT %s = %s OR %s = %s;'  % (
                                self._vars[ 'KX_CANDIDATE' ][r],
                                self._vars[ 'KX_CON' ][r],
                                self._vars[ 'KX_CANDIDATE' ][r],
                                self._vars[ 'LX_CON'][r] ) )
        # @ them
        self._constrs.append( self._concate( self._vars['KX_L1_NEW_START'][r] + self._vars['KX_L2_NEW_START'][r],
                                             self._vars['KX_CANDIDATE'][r] ) )

        return (self._vars['KX_L1_NEW_START'][r], self._vars['KX_L2_NEW_START'][r] )

    def __supply_K_from_L ( self, L1, L2, LL1, LL2, r ):
        
        self._constrs.append ( self._concate( L1 + L2, self._vars['KX_CON'][r] ) )
        self._constrs.append ( self._concate( LL1 + LL2, self._vars['LX_CON'][r] ) )
        
        self._constrs.append( 'ASSERT %s = IF %s = 0bin0 THEN (%s | 0h%016x) ELSE (0h%012x) ENDIF;' % (
                              self._vars['LX_CANDIDATE'][r][0], 
                              LL1[0],
                              self._vars['LX_CON'][r],
                              1 << (self._L1_len + self._L2_len -1 ),
                              (1 << (self._L1_len + self._L2_len )) - 1 ) )
        
        self._constrs.append( 'ASSERT %s = IF %s = 0bin0 THEN (%s | 0h%016x) ELSE (0h%012x) ENDIF;' % (
                              self._vars['LX_CANDIDATE'][r][1], 
                              LL2[0],
                              self._vars['LX_CON'][r],
                              1 << (self._L2_len - 1 ),
                              (1 << (self._L2_len + self._L1_len)) - 1 ) )
        # generat the new L1 and L2 
        self._constrs.append( 'ASSERT %s = %s OR %s = %s OR %s = %s;' % (
                                self._vars[ 'KX_CANDIDATE' ][r],
                                self._vars[ 'KX_CON' ][r],
                                self._vars[ 'KX_CANDIDATE' ][r],
                                self._vars[ 'LX_CANDIDATE'][r][0],
                                self._vars[ 'KX_CANDIDATE' ][r],
                                self._vars[ 'LX_CANDIDATE'][r][1] ) )
        # @ them
        self._constrs.append( self._concate( self._vars['KX_L1_NEW_START'][r] + self._vars['KX_L2_NEW_START'][r],
                                             self._vars['KX_CANDIDATE'][r] ) )

        return (self._vars['KX_L1_NEW_START'][r], self._vars['KX_L2_NEW_START'][r] )

    def __genInitialConstrs(self ):
        for p in range(self._L1_len):  
            self._constrs.append( self._equal (self._vars['KX_L1'][p], '0bin1' ) )
        for p in range(self._L2_len):  
            self._constrs.append( self._equal (self._vars['KX_L2'][p], '0bin1' ) )

        for p in range(self._L1_len):
            if self._inV[0][p]:
                self._addConstr(
                        self._equal( self._vars['LX_L1'][p], '0bin1')
                        )
            else:
                self._addConstr(
                        self._equal(self._vars['LX_L1'][p], '0bin0' )
                        )

        for p in range(self._L2_len):
            if self._inV[1][p]:
                self._addConstr(
                        self._equal( self._vars['LX_L2'][p], '0bin1')
                        )
            else:
                self._addConstr(
                        self._equal(self._vars['LX_L2'][p], '0bin0' )
                        ) 


        for p in range(self._L1_len):
            if self._outV[0][p]:
                self._addConstr(
                        self._equal( self._lastL1[p], '0bin1')
                        )
            else:
                self._addConstr(
                        self._equal(self._lastL1[p], '0bin0' )
                        )

        for p in range(self._L2_len):
            if self._outV[1][p]:
               self._addConstr(
                        self._equal( self._lastL2[p], '0bin1')
                        )
            else:
                self._addConstr(
                        self._equal(self._lastL2[p], '0bin0' )
                        )

        self._addConstr( 'QUERY FALSE;' )
        self._addConstr( 'COUNTEREXAMPLE;' )
            
    def getModel(self):
        self.__KdeclareVariables()
        self.__LdeclareVariables()
        self.__declareInter_variables()
        self.__roundFunction()
        self.__genInitialConstrs()

        
        return self._constrs

if __name__ == '__main__':
    ROUND = int( sys.argv[1] )
    ROUND_THREE = int( sys.argv[2] )
    L1_len = 25
    L2_len = 39

    pos1 = [24, 15, 20, 11, 9]
    pos2 = [38, 25, 33, 21, 14, 9]

    start = datetime.datetime.now()
    #       0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
    L1 = [1 for x in range(L1_len )]

    L2 = [ 1 for x in range(L2_len )]
    L2[0] = 0

    for i in range(L1_len + L2_len):
        outV_0 = [ 0 for x in range(L1_len)]
        outV_1 = [ 0 for x in range(L2_len)]
        if i < L1_len:
            outV_0 [ i] = 1
        else:
            outV_1 [ i - L1_len ] = 1

        f = open('cvc_%d_%d/%d.cvc' % (L1_len + L2_len, ROUND, i), 'w')
        katan = KATAN(ROUND, ROUND_THREE, L1_len, L2_len, pos1, pos2, (L1,L2), (outV_0, outV_1) )
        f.write('\n'.join(katan.getModel() ) )
        f.close()

    filename = 'result/result%d_%d.res' % ( L1_len + L2_len, ROUND) 
    f = open( filename , 'w')
    f.write( 'KATAN %d \nROUND %d\n' % (L1_len + L2_len, ROUND))
    f.close()
    os.system('bash excuteCVC.sh %d %d %s' %(L1_len + L2_len, ROUND, filename))

    end = datetime.datetime.now()
    f = open( filename , 'a')
    f.write( '%d\n'% (end- start).seconds )
    f.close()
    
    os.system('cat result/result%d_%d.res'%(L1_len + L2_len, ROUND) )

