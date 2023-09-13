import random

correctNumber = random.randint(0, 10)

print("Welcome to the Number Guessing Game. \nTo win the game you have to guess the correct number between 0-10 that I'm thinking. \nLet's start the game")
print("You'll get five chances to guess the correct number.")

keepLooping = True
count = 0

while (keepLooping is True):

    userEnteredNumber = int(input("Try to guess the number: "))


    if (userEnteredNumber == correctNumber):
        print("Wow! You guessed the correct number. \nCongrats you won the game! :D")
        keepLooping = False
    elif (userEnteredNumber < correctNumber):
        print("OOPS! Your number is too low :( \nTry Again!")
        count += 1
        print(f"Remaining Chances: {5 - count}")
    else:
        print("OOPS! Your number is too high :( \nTry Again!")
        count += 1
        print(f"Remaining Chances: {5 - count}")

    if (count == 5):
        print("You are out of your chances :( \nYou lost the game.")
        print(f"The correct number is {correctNumber}")
        keepLooping = False
