phrase= "This is a funny world!"
print(phrase[:-1])
x=int(input("Enter first Number: "))
y=int(input("Enter second Number: "))
z=input("Enter the operator")
if(z=='+'):
    print(x,z,y)
    print(x+y)
elif(z=='-'):
    print(x,z,y)
    print(x-y)
elif(z=='/'):
    print(x,z,y)
    print(x/y)
elif(z=='^2'):
    print(x,z,"and",y,z)
    print(pow(x,2))
    print(pow(y,2))