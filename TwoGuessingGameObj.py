import GuessingGameObjQuestion as GuessingGameObj
import time

class TwoGuessingGame:
    """This is a number guessing game. When an instance is created, two numbers between 1 and 10 are chosen, and the user can be asked to guess the number."""
    def __init__(self):
        """When an instance is created, it creates two single-number guessing games and associates a name with each."""
        #Note: this is coded without a list, and is therefore bad. The objective of this and the next game is to ease you into the use of lists.
        self.game1 = GuessingGameObj.GuessingGame()
        self.game2 = GuessingGameObj.GuessingGame()

        self.name1 = "Alexia"
        self.name2 = "Lucy"

    def getRules(self):
        """Returns a string describing what the player should do, suitable to be printed to prompt them to guess a number between 1 and 10."""
        return "Guess a number between 1 and 10. Try to solve both games at once! \nYou will get 5 chances to make the correct guess!!!"

    def allGamesDone(self):
        """Returns True if both games are finished, and False otherwise"""
        return self.game1.checkGameDone() and self.game2.checkGameDone()

    def checkCorrectGuess(self, guess):
        """For each game, checks if the guess is correct for that game and marks that game complete if so."""
        if not self.game1.checkGameDone() and guess == self.game1.num:
            self.game1.markGameDone()
            return True
        if not self.game2.checkGameDone() and guess == self.game2.num:
            self.game2.markGameDone()
            return True
        return False
        
        # if guess == self.game1:
        #     return self.game1.markGameDone()
        # elif guess == self.game2:
        #     return self.game2.markGameDone()
###################################################################################
## Functions above this point shouldn't assume anything about how i/o is handled!
##############################################################################

    def printGuessFeedback(self, guess):
        """Prints feedback about the guess to the terminal (std i/o). Does not print feedback from games that have been finished. Uses the names associated with each game so that the user can tell the "speakers" appart."""
        if not self.game1.checkGameDone():
            result1 = self.game1.checkGuess(guess)
            if result1 == -1:
                print(f"Too Low!!! says {self.name1}")
            elif result1 == 1:
                print(f"Too High!!! says {self.name1}")
        
        if not self.game2.checkGameDone():
            result2 = self.game2.checkGuess(guess)
            if result2 == -1:
                print(f"Too Low!!! says {self.name2}")
            elif result2 == 1:
                print(f"Too High!!! says {self.name2}")

    def playGame(self):
        """Instructs the current game instance to play itself with the user via the terminal (std i/o)."""
        print(self.getRules())

        count_game_cycle = 0

        while not self.allGamesDone():
            user_guess = int(input("What's your guess? "))
            if self.checkCorrectGuess(user_guess):
                name = self.name1 if self.game1.checkGameDone() else self.name2
                print(f"You got the right number for {name}")
            self.printGuessFeedback(user_guess)

            total_guess = 5
            count_game_cycle += 1
            remaining_guess = total_guess - count_game_cycle
            print(f"Remaining Guesses = {remaining_guess}")

            if count_game_cycle == 5:
                self.game1.markGameDone()
                self.game2.markGameDone()
                print(f"Sorry you lost the game. \nYou used all your guess.\nSo the correct number for {self.name1} is {self.game1.num} and \nthe correct number for {self.name2} is {self.game2.num}")


if __name__ == "__main__":
    game = TwoGuessingGame()
    game.playGame()
