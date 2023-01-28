
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have an iter() method which is used to get an iterator:
mytuple = ("raisins","walnuts", "almonds")
print(len(mytuple))
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit) + "\n")
# Even strings are iterable objects, and can return an iterator:
string = "Pussy Cat "
x=iter(string)
y=len(string)
counter =0
while counter < y:
    print(next(x))
    counter +=1
for b in string:
    print(b)
# Even Tuples are iterable objects, and can return an iterator:
tuple = ("apple","samsung", "nokia")
for x in tuple:
    # The for loop actually creates an iterator object and executes the next() method for each loop.
    print(x)

# Creating an Iterator: To create an object/class as an iterator, we have to implement the methods __iter__() and __next__()
class mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
mynum = iter(mynumbers())
print(next(mynum))
print(next(mynum))
print(next(mynum))
print(next(mynum))

# StopIteration
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration to go on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:

class MyNumbers:
   def __iter__(self):
       self.a = 1
       return self
   def __next__(self):
       if self.a <= 20:
           x = self.a
           self.a += 1
           return x
       else:
           raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)