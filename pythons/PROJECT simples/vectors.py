"""
this is just some simple vectors stuff that i will use for the thorough understanding of the
oop object creation and the more advanced thingy on the
"""


class Vector2D:
    """
    the vector class that needs to be implemented.
    it needs two other
    """
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __str__(self):
        return str(tuple(self))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

if __name__ == '__main__':
    v = Vector2D(3, 5)
    v2 = Vector2D(5, 11)
    ex, wy = v
    print(ex, wy)
    print(v)

    print(hash(v))
    print(hash(v2))
