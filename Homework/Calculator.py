# Create a calculator program using functions, loops, if and else. Basically everything u have learnt so far. 
# Push ur answer to a repo and WA or Discord the link to Ko Alvin.
# DUE DATE: 22/10/2022 11.59 PM

def add(num1, num2):
    return num1 +num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

calculate_again = "Yes"
while calculate_again == "Yes":
    choice = eval((input("Enter choice (1 - addition, 2 - subtraction, 3 - multiplication, 4 - division): ")))
    num1 = eval(input("Enter first number: "))
    num2 = eval(input("Enter second number: "))
    if choice == 1:
        add(num1,num2)
        print(add(num1,num2))
    elif choice == 2:
        subtract(num1,num2)
        print(subtract(num1,num2))
    elif choice == 3:
        multiply(num1,num2)
        print(multiply(num1,num2))
    elif choice == 4:
        divide(num1,num2)
        print(divide(num1,num2))
    else:
        print("You can only put a number from 1 to 4")
        eval(input("Re-enter your operation of choice (1 - addition, 2 - subtraction, 3 - multiplication, 4 - division): "))
    calculate_again = input("Would you like to calculate again? Yes/No ")

