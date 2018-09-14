from STPDivision import *

class ModularAdd(STPDivision):
    tags = set()
    def clearTags():
        ModularAdd.tags.clear()

    def __init__(self, dim, a, b, d, tag):
        super(ModularAdd, self).__init__()

        # tag is only used once
        assert isinstance(tag, str)
        assert tag not in ModularAdd.tags

        ModularAdd.tags.add(tag)
        self._tag = tag

        #TODO if a b d is not lists, write a function and transfer them to lists
        assert dim == len(a) and dim == len(b) and dim == len(d)
        self._dim = dim
        self._addend_1 = a
        self._addend_2 = b
        self._result = d
        
        self._equations = []
        self._tempVariables = []

        self._Kmodadd()

    def getTempVariables(self):
        return self._tempVariables

    def getEquations(self):
        return self._equations

    def _addEquation(self, s):
        self._equations.append(s)

    def _Kcopy3( self, x, y, z, zz):
        tmp = self._getTempVar(y + z) 
        self._addEquation( self._Kcopy( tmp, y, z))
        self._addEquation( self._Kcopy( x, tmp, zz ) )

    def _Kxor3(self, x, y, z, r):
        tmp = self._getTempVar(x + y )
        self._addEquation( self._Kxor( x, y, tmp) )
        self._addEquation( self._Kxor( tmp, z, r) )

    def _Kmodadd(self):
        n = self._dim
        a = self._addend_1
        b = self._addend_2 
        d = self._result

        self._addEquation('%Modular Add')
        v, g, m, r, q, w = 'Kv', 'Kg', 'Km', 'Kr', 'Kq', 'Kw'
        self._addEquation( self._Kcopy( a[n-1], self._getTempVar(a[n-1], 0), self._getTempVar(a[n-1], 1)  ) )
        self._addEquation( self._Kcopy( b[n-1], self._getTempVar(b[n-1], 0), self._getTempVar(b[n-1], 1)  ) )
        self._addEquation( self._Kxor( self._getTempVar(a[n-1], 0), self._getTempVar(b[n-1], 0), d[n-1] ) )
        self._addEquation( self._Kand( self._getTempVar(a[n-1], 1), self._getTempVar(b[n-1], 1), self._getTempVar(v, 0) ) )
        self._addEquation( self._Kcopy( self._getTempVar(v, 0), self._getTempVar(g, 0), self._getTempVar(r, 0) ) )
        self._Kcopy3( a[n-2], self._getTempVar( a[n-2], 0 ), self._getTempVar(a[n-2], 1), self._getTempVar(a[n-2], 2 ) )
        self._Kcopy3( b[n-2], self._getTempVar( b[n-2], 0 ), self._getTempVar(b[n-2], 1), self._getTempVar(b[n-2], 2 ) )

        for i in range(2, n-1):
            self._Kxor3( self._getTempVar( a[n-i], 0 ), self._getTempVar( b[n-i], 0) , self._getTempVar(g, i - 2), d[n-i] ) 
            self._addEquation( self._Kand( self._getTempVar( a[n-i], 1), self._getTempVar( b[n-i], 1), self._getTempVar( v, i - 1) ))
            self._addEquation( self._Kxor(self._getTempVar(a[n-i], 2), self._getTempVar(b[n-i], 2), self._getTempVar(m, i-2) ) )
            self._addEquation( self._Kand(self._getTempVar(m, i-2), self._getTempVar(r, i-2), self._getTempVar(q, i-2) ) )
            self._addEquation( self._Kxor(self._getTempVar(v, i-1), self._getTempVar(q, i-2), self._getTempVar(w, i-2) ) )
            self._addEquation( self._Kcopy( self._getTempVar(w, i-2), self._getTempVar(g, i-1), self._getTempVar(r, i-1) ) )
            self._Kcopy3( a[n-i-1], self._getTempVar(a[n-i-1], 0), self._getTempVar(a[n-i-1], 1), self._getTempVar(a[n-i-1], 2) )
            self._Kcopy3( b[n-i-1], self._getTempVar(b[n-i-1], 0), self._getTempVar(b[n-i-1], 1), self._getTempVar(b[n-i-1], 2) )

        self._Kxor3( self._getTempVar(a[1], 0), self._getTempVar(b[1], 0), self._getTempVar(g, n-3), d[1] )
        self._addEquation( self._Kand( self._getTempVar(a[1], 1), self._getTempVar(b[1], 1 ), self._getTempVar(v, n-2) ))
        self._addEquation( self._Kxor( self._getTempVar(a[1], 2), self._getTempVar(b[1], 2 ), self._getTempVar(m, n-3) ) )
        self._addEquation( self._Kand( self._getTempVar(m, n-3), self._getTempVar( r, n-3 ), self._getTempVar(q, n-3) ) ) 
        self._addEquation( self._Kxor( self._getTempVar(v, n-2), self._getTempVar( q, n-3 ), self._getTempVar(w, n-3) ) ) 
        self._Kxor3( a[0], b[0], self._getTempVar(w, n-3), d[0] )

    def _getVarName(self, name, index):
        return 'K_%s_%s_%s'%(self._tag, name, str(index))
    
    def _getTempVar(self, name, index = 0 ):
        var = self._getVarName(name, index)
        if var in self._tempVariables:
            return var
        else:
            self._tempVariables.append( var )
            return var
    

def main():
    m = ModularAdd(4, ['x0','x1','x2','x3'], ['y0','y1','y2','y3'], ['z0','z1','z2','z3'], 'test' )
    print ( '\n'.join(m.getEquations() )) 
    print ( '\n'.join(m.getTempVariables() )) 


if __name__ == '__main__':
    main()
