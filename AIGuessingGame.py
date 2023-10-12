class AIGuessingGame:
    """This is an AI number guessing game. When an instance is created, it sets up a range from 1 and 10, and attempts to guess the user's number within that range via binary search."""

    def __init__(self, lower_bound=1, upper_bound=10):
        """When an instance is created, it sets up a range of uncertanty from 1 to 10."""
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def getRules(self):
        """Returns a string describing what the player should do, suitable to be printed to prompt them to pick a number between 1 and 10."""
        return f"Welcome to the AI Guessing. \nTo Play the game you have to guess a number between {self.lower_bound} and {self.upper_bound}. \nThe game is over when your number is guessed correctly. \nEnjoy!!!"

    def calcGuess(self):
        """Returns the best guess within the range (the best guess is the one that eliminates the most possibilities if incorrect)."""
        best_guess = (self.lower_bound + self.upper_bound) // 2
        return best_guess

    def updateRange(self, guess, feedback):
        """Updates the range of uncertanty or marks the game complete based on the provided guess and feedback code (1, 0, or -1)."""
        if feedback == 1:
            self.upper_bound = guess - 1
        elif feedback == -1:
            self.lower_bound = guess + 1

    ##No I/O above this point!

    def getFeedbackFromTerminal(self, guess):
        """Uses the terminal to get feedback from the user about the provided guess. Returns 1 if the guess is greater than the user's number, -1 if it is smaller, and 0 if it is the same."""

        # user_number = int(input("Enter your number to be guessed by me :)"))

        print(
            f"Is {guess} your number????"
        )  # This line is incomplete! How do you ask the user about the guess?

        print(
            "a - Too low!\nb - You got it!\nc - Too high!"
        )  # This line is finished, you don't need to change it.

        # Note: this function is incomplete, finish it!
        # What is the user expecting to do now?
        # What do you need to do after that?
        user_input = input("Choose among the three option: \n")

        if user_input == "a":
            return -1
        elif user_input == "b":
            return 0
        elif user_input == "c":
            return 1

    def playGame(self):
        """Instructs the current game instance to play itself with the user via the terminal (std i/o)."""


if __name__ == "__main__":
    game = AIGuessingGame()
    game.playGame()
