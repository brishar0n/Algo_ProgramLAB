total_bill = eval(input("Please enter your total bill "))
number_of_people = eval(input("How many people are splitting the bill? "))
percentage_tip = eval(input("How much tip in % would you like to give? "))

billpercent = total_bill * (percentage_tip / 100)
totalamount = total_bill + billpercent
tipPerPerson = billpercent / number_of_people
totalperPerson = totalamount / number_of_people

print(f"Tip per person $ {tipPerPerson:.2f}")
print(f"Bill per person $ {totalperPerson:.2f}")

#_________

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

#__________

seconds_insert = eval(input("Insert a number of seconds"))

hour = seconds_insert // 3600
minute = seconds_insert // 60
second = seconds_insert % 60 

print(f"Result: {hour}:{minute}:{second}")