# Define Class and name the class
class number:
    x = 5
    y = 2
    m = x * y
    z = 9
# Create an Object p1
p1 = number()
print(p1.m)


# All classes have a function called __init__(), which is always executed when the class is being initiated.
#
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return  f"{self.name}(-{self.age}-)"
    def myFunc(self):
        print("Hello Mr. " + self.name)

# p1 = Person(input("Who are we talking to?"),30)
p1 = Person("Jim",32)
p1.myFunc()
# print(p1)

class Person1:
    pass

