import random

secret_number = random.randint(1 , 10)

while True:
    guess = int(input("guess the number between 1 to 10: "))

    if(guess < secret_number):
        print("too low")

    elif(guess > secret_number):
        print("too high")

    else:
        print("correct guess")
        break