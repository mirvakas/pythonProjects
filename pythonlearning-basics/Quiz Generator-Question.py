from Question import Student

# from Question import Question

Student1 = Student("Vakas", "29", "Male", "7.8")
Student2 = Student("Rob", "34", "Male", "3.2")

print(Student2.is_pass())

# Program 2 to make a 3 question quiz and storing it to a file;
# employee_file = open('C:/Users/vhmir/OneDrive/Documents/Questions.txt', "r+")
# question_prompt = [
#     "What color are apples?\n (a) Red\n (b) Green\n (c) Orange\n (d) Yellow\n\n",
#     "What color are bananas?\n (a) Red\n (b) Green\n (c) Orange\n (d) Yellow\n\n",
#     "What color are oranges?\n (a) Red\n (b) Green\n (c) Orange\n (d) Yellow\n\n"
# ]
# questions = [
#     Question(question_prompt[0],"a"),
#     Question(question_prompt[1],"d"),
#     Question(question_prompt[2],"c")
# ]
#
# def run_test (questions):
#     score=0
#     for question in questions:
#         if question == questions[0]:
#             employee_file.write(question.prompt)
#         else:
#             employee_file.write("\n" + question.prompt)
#         answer = input(question.prompt)
#         employee_file.write("User's answer: (" + answer + ")\n")
#         if answer  == question.answer:
#             score+=1
#     if score == 3:
#         message = "\nUser scored 100%. Congratulations."
#         print("\nYou've scored 100%. Congratulations.")
#         employee_file.write(message)
#     else:
#         message = "The Score is: " + str(score) + " out of " + str(len(questions)) + " questions."
#         print("The Score is: " + str(score) + " out of " + str(len(questions)) + " questions.")
#         employee_file.write(message)
#
# run_test(questions)
# input("Press any button to exit!")
