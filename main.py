from vector import Vector

# Create two vectors using the constructor
v1 = Vector(3, 4)
v2 = Vector(1, 2)

# Add the vectors using overloaded + operator (__add__)
v3 = v1 + v2

# Print the string representation of each vector
print("Vector 1:", v1)  # Output: Vector(3, 4)
print("Vector 2:", v2)  # Output: Vector(1, 2)
print("Vector 3 (v1 + v2):", v3)  # Output: Vector(4, 6)

# Display magnitude of the result vector
print("Magnitude of Vector 3:", v3.magnitude())  # sqrt(4² + 6²) = ~7.21

# Use static method to check if the vector is a zero vector
print("Is v3 a zero vector?", Vector.is_zero_vector(v3))  # Output: False

# Access nested MetaInfo class for author/version
print("Vector Class Info: Author =", Vector.MetaInfo.author, ", Version =", Vector.MetaInfo.version)
