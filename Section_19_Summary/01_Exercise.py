"""
Exercise No. 01

The people list is given. Sort the objects in the people list ascending by age. Then print the name and age to the
console as shown below.

Expected result:

    Alice -> 19
    Tom -> 25
    Mike -> 27
    John -> 29
"""


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [
    People("John", 29),
    People("Mike", 27),
    People("Tom", 25),
    People("Alice", 19)
]

# Solution 1
people.sort(key=lambda people: people.age)
for person in people:
    print(f"{person.name} -> {person.age}")
