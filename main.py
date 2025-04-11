from vector import Vector

v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = v1 + v2

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Vector 3 (v1 + v2):", v3)
print("Magnitude of Vector 3:", v3.magnitude())
print("Is v3 a zero vector?", Vector.is_zero_vector(v3))
print("Vector Class Info: Author =", Vector.MetaInfo.author, ", Version =", Vector.MetaInfo.version)
