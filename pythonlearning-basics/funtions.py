def cube_v(x):
    return x * x * x


print(cube_v(int(input("Enter the number you want Cube of:"))))


def text_ctrl(x, y, z):
    print("This is a good person:" + x + ". You can see his age as:" + str(y) + ". Last arugment is:" + str(z))


text_ctrl("Mike", 22, "Great Man")

x = int(input("Enter the number"))
print(pow(x, 2))


# writing raise to the power function

def raise_to_power(base_num, power):
    result = 1
    for index in range(power):
        result = result * base_num
    return result


print(raise_to_power(3, 3))
