class Person:
    def __init__(self,fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    def __init__(self, fname, lname):
      # Person.__init__(self, fname, lname)
        # Use the super() Function  suPython also has a super() function that will make the child class inherit all the methods and properties from its parent:
      # super().__init__(fname, lname)

x = Student("Johny", "Depp")
x.printname()