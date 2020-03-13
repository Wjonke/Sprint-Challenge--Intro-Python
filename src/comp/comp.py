# The following list comprehension exercises will make use of the 
# defined Human class.

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]
a = []
# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
for i in humans :
    if i.name[0] == "D" :
        a.append(i.name)

print("Starts with D:")

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print(humans[0].name)
b = []
for i in humans :
    if i.name[-1] == "e" :
        b.append(i.name)
print("Ends with e:")
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
letters = ['C','D','E','F','G']
c = [i.name for i in humans if (i.name[0] in letters)]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for i in humans :
    new_age = int(i.age) + 10
    d.append(new_age)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for i in humans:
    new_list = f"{i.name}-{i.age}"
    e.append(new_list)
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(i.name, i.age) for i in humans if 27 <= i.age <= 32]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
for i in humans:
    new_list = f"{i.name.upper(), i.age + 5}"
    g.append(new_list)
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
for i in humans:
    new_list = math.sqrt(i.age)
    h.append(new_list)
print(h)
