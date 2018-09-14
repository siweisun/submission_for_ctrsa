from BOOLFUNC import GenInt
import BOOLFUNC.Vector as vc

class AssertSbox(object):
    def __init__(self, sboxName, sbox, dim, r, number_of_sbox):
        self.__round = r
        self.__numberOfSbox = number_of_sbox
        self.__genInt = GenInt.GenInt(sbox, dim, dim)
        self.__sboxName = sboxName
        self.__sboxNames = self.__genSboxName()
        self.__dim = dim
        self.__declares = []
        self.__asserts = []

    def __genSboxName(self):
        sboxNames = []
        for r in range(self.__round):
            sboxNameOneRound = []
            for p in range(self.__numberOfSbox):
                sboxNameOneRound.append( '%s_%d_%d'%(self.__sboxName, r, p ) )
            sboxNames.append( sboxNameOneRound )
        return sboxNames

    def build_constrs(self, inVec, outVec, r, p):
        assert len(inVec) == self.__dim and len(outVec) == self.__dim
        s = 'ASSERT %s = %s[%s];' % (
                '@'.join(outVec),
                self.__sboxNames[r][p], 
                '@'.join(inVec)
                )

        return s
   
    def __bin(self, num, length):
        return '0bin' + bin(num)[2:].zfill(length)

    def __declareSbox(self, r, p):
        trails = self.__genInt.getTrails()

        s = '%s:ARRAY BITVECTOR(%d) OF BITVECTOR(%d);' % (
                self.__sboxNames[r][p], 
                self.__dim, 
                self.__dim
                )
        self.__declares.append(s)

        for i in range(2 ** self.__dim):
            s = '%s_%d:BITVECTOR(%d);' % (self.__sboxNames[r][p], i, self.__dim)
            self.__declares.append(s)
            L = []

            x = vc.Vector(self.__dim, i)
            for y in trails[x]:
                    L.append( '%s_%d = %s' % (
                        self.__sboxNames[r][p], 
                        x.getValue(), 
                        self.__bin(y.getValue(), self.__dim)
                        ) )
            self.__declares.append( 'ASSERT %s;' % ' OR '.join(L))

            s = 'ASSERT %s[%s] = %s_%d;'%(
                    self.__sboxNames[r][p], 
                    self.__bin(i, self.__dim),
                    self.__sboxNames[r][p], 
                    i
                    )
            self.__asserts.append(s)
        
    def get_asserts_declares(self):
        for r in range(self.__round):
            for p in range(self.__numberOfSbox):
                self.__declareSbox(r, p)
        return self.__declares + self.__asserts

def main():
    sbox = [ 0x6, 0x5, 0xC, 0xA, 0x1, 0xE, 0x7, 0x9, 0xB, 0x0, 0x3, 0xD, 0x8, 0xF, 0x4, 0x2 ]

    a = AssertSbox('sbox', sbox, 4, 2, 16)

    print( '\n'.join(a.get_asserts_declares()))

    inVec  = ['x0', 'x1', 'x2', 'x3']
    outVec = ['y0', 'y1', 'y2', 'y3']
    print( a.build_constrs(inVec, outVec, 1, 15) )

if __name__ == '__main__':
    main()
    
            
            
        


            


