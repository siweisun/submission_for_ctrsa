class Vector(object):
    def __init__(self, dim, value):
        assert 0 <= value <= (1 << dim)
        self.dimension = dim
        self.value = value
        self.coveringVectors = []

    def __le__(self, other):
        assert self.dimension == other.dimension
        return self.Value & other.value == self.value

    def __lt__(self, other):
        assert self.dimension == other.dimension
        return self.value < other.value

    def __ge__(self, other):
        assert self.dimension == other.dimension
        return self.Value & other.value == other.value

    def __genCoveringVectors(self):
        for vec in range(0, 1 << self.dimension):
            if vec & self.value == self.value:
                self.coveringVectors.append( Vector(self.dimension, vec) )

    def getValue(self):
        return self.value
    
    def __hash__(self):
        return hash((self.dimension, self.value))
    
    def __eq__(self, other):
        return self.dimension == other.dimension and self.value == other.value

    def toList(self):
        vectorList = list()
        for i in range(self.dimension):
            vectorList.append( self.value >> (self.dimension - 1 - i) & 1 )
        return vectorList

    def __str__(self):
        return str(self.value)

    def getCoveringVectors(self):
        self.__genCoveringVectors()
        return self.coveringVectors

    def __add__(self, other):
        return Vector(self.dimension + other.dimension, ( self.value << other.dimension ) | other.value )

def main():
    a = Vector(4, 2)
    b = Vector(4, 3)
    print( str(a + b ) ) 
    print ( ( a + b ).toList() )

if __name__ == '__main__':
    main()
  


