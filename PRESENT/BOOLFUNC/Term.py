class Term(object):
    def __init__(self, represent_char, number_of_bit, term_value = None, term_str=None) :
        self.represent_char = represent_char
        self.number_of_bit = number_of_bit
        if term_value:
            assert  0 < term_value < (1 << number_of_bit), \
               'term_value %x out of limits of mumber_of_bit %d' % (term_value, number_of_bit)
            self.term_value = term_value
        else:
            self.term_value= None
        
        if term_str:
            self.term_value = 0
            self.__parseTerm(term_str)


    def __eq__(self, other):
        return self.represent_char == other.represent_char and \
               self.number_of_bit == other.number_of_bit and \
               self.term_value == other.term_value

    def __hash__(self):
        return hash( (self.represent_char, self.number_of_bit, self.term_value) )

    def __ge__(self, other):
        return self.term_value & other.term_value == other.term_value

    def __le__(self, other):
        return self.term_value & other.term_value == self.term_value

    def __str__(self):
        if not self.term_value:
            return 'None'
        represent = list()
        for bit_index in range( self.number_of_bit ):
            bit_pos = self.number_of_bit -1 -bit_index 
            if self.term_value >> bit_pos & 1:
                represent.append( self.represent_char + str(bit_pos) )
        return ''.join( represent )
    
    def __mul__(self, other):
        if isinstance(other, ConstTerm):
            return self
        elif isinstance(other, Term):
            return Term( self.represent_char, self.number_of_bit, self.term_value | other.term_value)

    def __parseTerm(self, strTerm):
        numbers = strTerm.split( self.represent_char )
        for num in numbers:
            if num:
                self.term_value ^= (1 << int(num))

    def parseTerm(self, strTerm, number_of_bit):
        #Todo check the strTerm is right 
        represent_char = strTerm[0]
        value = 0
        numbers = strTerm.split( represent_char )
        for num in numbers:
            if num:
                value ^= (1 << int(num))

        return Term( represent_char, number_of_bit, value )
    
class ConstTerm(object):
    def __init__(self, value):
        assert value == 0 or value == 1, \
                'ConstTerm has only two values, 0 or 1 NOT %d'% value
        self.value = value

    def __hash__(self):
        return hash( (self.value ))

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    def __mul__(self, other):
        if isinstance(other, ConstTerm):
            if self.value == 1 and other.value ==1:
                return ConstTerm(1)
            else:
                return ConstTerm(0)

        elif isinstance(other, Term):
            return other


def main():
    term = Term('x', 8, term_str = 'x3x2x1')
    term_cover = Term('x', 8, term_str='x3x2x1x7')
    p = Polynomial('x3x2x1 + 1', 8)
    print (p.isContain(term))

if __name__ == '__main__':
        main()


