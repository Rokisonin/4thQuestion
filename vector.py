from abc import ABC, abstractmethod
import math

class VectorBase(ABC):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def magnitude(self):
        pass

class Vector(VectorBase):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    @staticmethod
    def is_zero_vector(vector):
        return vector.x == 0 and vector.y == 0

    class MetaInfo:
        author = "Sehiro"
        version = "1.0"
