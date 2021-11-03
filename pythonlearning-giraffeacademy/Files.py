# import calendar
# mh= calendar.month(2021, 10)
# print(mh)

# C:\Users\vhmir\PycharmProjects\pythonProject
# C:\Users\vhmir\OneDrive\Documents\Emp.txt

employee_file = open('C:/Users/vhmir/OneDrive/Documents/Emp1.txt', "r+")
# print(employee_file.read())
try:
    print(employee_file.read())
except:
    print("Unknown Error")
employee_file.write("\n" + "Toby - Human Resource")
print(employee_file.read())
employee_file.close()

def get_file_ext(filename):
    return  filename[filename.index(".") + 1:]

print(get_file_ext("vakas.dat"))





