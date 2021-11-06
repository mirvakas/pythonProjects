# secret_word = "giraffe"
# guess = ""
# counter = 0
# while guess != secret_word and counter < 3:
#     guess  = input("Enter guess: ")
#     counter +=1
# if counter <= 3:
#     print("You win")
# else:
#     print("You lost all attempts")

# learning while loop:
# for letter in "Giraffe Academy":
#     print(letter)
#
# friends = ['List1','List2','List3','List4','List5','List6','List7']
# # for index in friends:
#     print(index)
# for index in range(100):
#     print(index)
# print(range(1,100))
#
# for index in range(len(friends)):
#     print(index)
#     print(friends[index])
#
# for index in range(5):
#     if index == 0:
#         print("1st Iteration of the loop.")
#     elif index == 1:
#         print("2nd Iteration of the loop")
#     else:
#         print(str((index+1)) + " Iteration of the loop.")

# Nested Loops:
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[2][2])

for row in number_grid:
    for col in row:
        print(col)
