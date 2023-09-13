import random

class GuessingGame:
    """This is a number guessing game. When an instance is created, it picks a number between 1 and 10, and the user can be asked to guess the number."""
    def __init__(self):
        """When an instance is created, it picks a number between 1 and 10."""
        #note: This is a syntax error. Complete the following statement!
        self.num = random.randint(1, 10)
        self.done = False

    def getRules(self):
        """Returns a string describing what the player should do, suitable to be printed to prompt them to guess a number between 1 and 10."""
        #note: This returns an empty string. Finish the function!
        return "Welcome to the battelship game. You have to guess the location of the battelship which are hidden between 1 - 10."

    def checkGameDone(self):
        """Returns a boolean value, True if the game is over, False otherwise."""
        return self.done


    def markGameDone(self):
        """Marks the game as being over."""
        self.done = True

    def checkGuess(self, guess):
        """Returns 1 if the guess is greater than the chosen number, -1 if it is smaller, and 0 if it is the same."""
        if guess < self.num:
            return -1
        elif guess > self.num:
            return 1
        else:
            return 0

    def playGame(self):
        """Instructs the current game instance to play itself with the user via the terminal (std i/o)."""
        print(self.getRules())

        while not self.checkGameDone():
            user_guess = int(input("Enter the cordinate for the battelship: "))
            result = self.checkGuess(user_guess)

            if result == -1:
                print("Your guess is lower then the coordinates :(")
            elif result == 1:
                print("Your guess is higher then the coordinates :(")
            else:
                print("You guessed the correct cordinates. Congrats you won the game :D")
                self.markGameDone()


if __name__ == "__main__":
    game = GuessingGame()
    game.playGame()
