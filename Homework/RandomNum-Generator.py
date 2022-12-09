import random

x = random.randint(1,100)
print("I'm thinking of a number from 1 to 100, what is it?")
guess = int(input())

while True:
    if guess < x:
        print("Yikes, your guess is too small.")
        guess = int(input("Try again."))

    if guess > x:
        print("Yikes, your guess is too big.")
        guess = int(input("Try again."))

    if guess == x:
        print("Wow! You guessed it! Great job!")
        break
