x=int(input("Enter first Number: "))
z=input("Enter the operator")
y=int(input("Enter second Number: "))

if(z=='+'):
    #print(x,z,y)
    print(x+y)
elif(z=='-'):
    #print(x,z,y)
    print(x-y)
elif(z=='/'):
    #print(x,z,y)
    print(x/y)
elif(z=='^2'):
    #print(x,z,"and",y,z)
    print(pow(x,2))
    print(pow(y,2))
else:
    print("Invalid Operator")