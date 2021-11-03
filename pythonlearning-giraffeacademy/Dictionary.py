dictionary={
    "Jan": "January",
     "Feb": "February",
    "Mar": "March"
}
print(dictionary.get("Mar", "The month you entered is not valid"))

secret_word = "giraffe"
guess = ""
counter = 0
while guess != secret_word and counter < 3:
    guess  = input("Enter guess: ")
    counter +=1
if counter <= 3:
    print("You win")
else:
    print("You lost all attempts")