a="------Simple Calculator------"
print(a.center(50))

# a and b are the variables which take input as a number or float
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

# choice is the variable which takes the input of the operation we want to perform
choice=int(input("Select the operation from 1-4:"))
if (choice==1):
    print(a,"+",b,"=",a+b)
elif(choice==2):
    print(a,"-",b,"=",a-b)
elif(choice==3):
    print(a,"x",b,"=",a*b)
elif(choice==4):
    print(a,"/",b,"=",a/b)
else:
    print("Invalid Input")
exit()