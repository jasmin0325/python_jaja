import random

def number_baseball():
    # Generate a random 3-digit number
    target = str(random.randint(100, 999))
    print("Welcome to Number Baseball! I'm thinking of a 3-digit number.")
    print("Try to guess the number and I'll tell you how many digits are correct.")
    print("You have 10 tries to guess the number.")
    for i in range(10):
        guess = input("Enter your guess: ")
        if guess == target:
            print("Congratulations! You guessed the number in {} tries!".format(i+1))
            return
        else:
            correct_digits = 0
            for j in range(3):
                if guess[j] == target[j]:
                    correct_digits += 1
            print("{} digits are correct.".format(correct_digits))
    print("Sorry, you didn't guess the number. The correct number was {}.".format(target))

number_baseball()
