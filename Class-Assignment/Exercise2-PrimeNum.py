number = eval(input("Enter a number: "))
if number > 1:
    for i in range(2, int(number/2)):
        if (number % 1) == 0:
            print(number, "is not a prime number")
            break

    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")
