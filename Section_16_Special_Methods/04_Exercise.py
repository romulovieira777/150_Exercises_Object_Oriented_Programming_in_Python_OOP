"""
Exercise No. 04

An implementation of the Vector class is given. Implement __str__() special method to display an informal representation
of a Vector instance as show below:

    [IN]: v1 = Vector(1, 2)
    [IN]: print(v1)

    [OUT]: (1, 2)

Create a vector from the R^3 space with coordinates: (-3, 4, 2) and assign it to the variable v1.

In response, print the variable v1 to the console.

Expected result:

    (-3, 4, 2)
"""


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"

    def __str__(self):
        return str(self.components)


v1 = Vector(-3, 4, 2)
print(v1)
