friends = ['Test1', 'Test2', 'Test3']
print(friends[1:])

# Doing operations on Strings
lucky_numbers = [1, 2, 3, 6, 7, 8, 4, 3, 77, 54, 43, 23]
friends = ['Test1', 'Test2', 'Test3']
friends.extend(lucky_numbers)
print(friends)
friends.insert(3, "Test4")  # first argument is the index and other is the value\
print(friends)
friends.remove("Test3")
print(friends)
friends.pop()
print(friends)
friends.pop()
print(friends)
x = friends.index(77)
print(x)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
newlucky = lucky_numbers.copy()
print(newlucky)
lucky_numbers.sort()
print(lucky_numbers)
friends.clear()
print(friends)
