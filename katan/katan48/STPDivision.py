import os
class STPDivision(object):
    def __init__(self):
        self._constrs = []
        self._vars = dict()

    def _bin(self, x, length):
        return '0bin' + bin(x)[2:].zfill(length)

    def _or_concate(self, ORS, candidate, length ):
        m = 'ASSERT '
        for x in ORS:
            m += '%s = %s OR ' % (candidate, x)
        m += '%s = %s;'% (candidate, self._bin( (1 << length) - 1, length ) )

        return m

    def _Kcopy(self, a, b0, b1 ):
        s = '%% Kcopy %s -> (%s, %s)\n' % (a, b0, b1)
        s += 'ASSERT '
        s += '~' + b0 + ' | ~'+ b1 + ' = 0bin1;\n' 
        s += 'ASSERT '
        s += a + ' | ' + b0 + ' | ~' + b1 + ' = 0bin1;\n' 
        s += 'ASSERT '
        s += a + ' | ' + '~' +b0 + ' | ' + b1 + ' = 0bin1;\n' 
        s += 'ASSERT '
        s += '~' + a + ' | ' + b0 + ' | ' + b1 + ' = 0bin1;' 

        return s

    def _Lcopy(self, a, b0, b1 ):
        s = 'ASSERT '
        s += a + ' | ' + b0 + ' | ~'+ b1 + ' = 0bin1;\n' 
        s += 'ASSERT '
        s += '~' + a +  ' | ' +  b0 + ' | ' + b1 + ' = 0bin1;\n' 
        s += 'ASSERT '
        s += a + ' | ' + '~' + b0 + ' = 0bin1;' 

        return s

    def _Kand(self, a0, a1, b ):
        s = '%% Kand %s & %s -> %s\n' % (a0, a1, b)
        s += 'ASSERT '
        s += '~' + a1 + ' | ' + b + ' = 0bin1;\n' 
        s += 'ASSERT '
        s += a0 +  ' | ' +  a1 + ' | ~' + b + ' = 0bin1;\n' 
        s += 'ASSERT '
        s += '~' + a0 + ' | ' + b + ' = 0bin1;' 

        return s

    def _Land(self, a0, a1, b ):
        s = 'ASSERT '
        s += a0 + '='  + b + ';\n'
        s += 'ASSERT '
        s += a1 + '='  + b +  ';'

        return s

    def _Kxor(self, a0, a1, b ):
        s = '%% Kxor %s ^ %s -> %s\n' % (a0, a1, b)
        s += 'ASSERT '
        s += '~' + a0 +' | ~' + a1 + '= 0bin1;\n'
        s += 'ASSERT '
        s += a0 + ' | ' + a1 + ' | ~' + b + '= 0bin1;\n'
        s += 'ASSERT '
        s += a0 +' | ~' + a1 + ' | ' + b + '= 0bin1;\n'
        s += 'ASSERT '
        s += '~' + a0 + ' | ' + a1 + ' | ' + b + '= 0bin1;'

        return s

    def _Lxor( self,a0, a1, b ):
        s = 'ASSERT '
        s += a0 +' | ' + a1 + ' | ~' + b + '= 0bin1;\n'
        s += 'ASSERT '
        s += '~' + a1 + ' | ' + b + '= 0bin1;\n'
        s += 'ASSERT '
        s += '~' + a0 + ' | ' + a1 + ' | ' + b + '= 0bin1;\n'
        s += 'ASSERT '
        s += '~' + a0 + ' | ~' + a1 + ' | ~' + b + '= 0bin1;'

        return s

    def _declare(self,  x, num = 1 ):
        return x + ':BITVECTOR(' + str(num) + ');'

    def _declareArray(self,  x, num1, num2 ):
        return x + ': ARRAY BITVECTOR( ' + str(num1) + ') OF BITVECTOR(' + str(num2) + ');'

    def _concate(self, X, res):
        assert X
        model = 'ASSERT '
        for x in X:
            model += '%s@'%x

        model = '%s=%s;' % ( model[0:-1], res)
        return model

    def _equal(self, s1, s2 ):
        return 'ASSERT ' + s1 + '=' + s2 + ';'

    def _addConstr(self, m):
        assert m, 'm must not be None'
        self._constrs.append( m )

if __name__ == '__main__':
    X = [str(x) for x in range(32)]
    m = STPDivision()
    

