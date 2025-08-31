# simple calculation app
num1 = int(input("ENter the first number: "))
num2 = int(input("Enter the second number: "))
opt = input("Enter the operator: ")

if opt == '+':
    print("the adition is ", num1 + num2)
elif opt == '-':
    print("the subtraction is ", num1 - num2)

elif opt == '*':
    print("the multiplication is ", num1 * num2)  
elif opt == '/':
    print("the division is ", num1 / num2)  
else:
    print("invalid operator")    





