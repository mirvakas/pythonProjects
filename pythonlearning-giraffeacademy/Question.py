class Student:

    def __init__(self, name, age, sex, grade):
        self.name = name
        self.age = age
        self.sex = sex
        self.grade = grade

    def is_pass(self):
        if float(self.grade) >= 3.5:
            return True
        else:
            return False


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
