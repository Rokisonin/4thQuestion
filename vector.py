from abc import ABC, abstractmethod
import math

# Abstract base class defining vector behavior blueprint
class VectorBase(ABC):
    @abstractmethod
    def __add__(self, other):
        # Enforces that any subclass must implement vector addition
        pass

    @abstractmethod
    def magnitude(self):
        # Enforces magnitude calculation implementation
        pass

# Vector class implementing VectorBase and overloading +
class Vector(VectorBase):
    def __init__(self, x, y):
        # Encapsulated private coordinates
        self.__x = x
        self.__y = y

    # Getter for x (read-only access)
    @property
    def x(self):
        return self.__x

    # Getter for y
    @property
    def y(self):
        return self.__y

    # Operator overloading: enables `v1 + v2`
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        # Returns a new Vector with summed components
        return Vector(self.x + other.x, self.y + other.y)

    # Check equality of two vectors
    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    # Readable string representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Debug-friendly representation
    def __repr__(self):
        return str(self)

    # Calculate vector magnitude using Pythagorean theorem
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Static method to check if a vector is zero (0, 0)
    @staticmethod
    def is_zero_vector(vector):
        return vector.x == 0 and vector.y == 0

    # Nested class to store metadata about the Vector class
    class MetaInfo:
        author = "Sehiro"
        version = "1.0"
