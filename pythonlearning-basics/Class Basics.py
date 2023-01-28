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
        print("Hello Mr. " + self.name + ". You are " + str(self.age) + " years old")

# p1 = Person(input("Who are we talking to?"),30)
p1 = Person("Jim",32)
# p1.myFunc()
print(p1)

#If we need to define a class without any definition, we can use 'pass' statement to avoid any compiling errors.
class Person1:
    pass

class Student(Person):
  # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
  def __init__(self, name, age):
    #In order to keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    Person.__init__(self, name, age)

x = Student("Mike Tosti", 42)
x.myFunc()
# We can also use the super function to inherit all objects and methods of the parent class.
class Student2(Person):
  def __init__(self, name, age, year):
    super().__init__(name, age)
    self.joiningyear = year
x2 = Student2("Manoj", 42, 2018)
x2.myFunc()
print(x2.joiningyear)