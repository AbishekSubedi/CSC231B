import GuessingGameObjQuestion as GuessingGameObj
import time


class NGuessingGame:
    """This is a number guessing game. When an instance is created, two numbers between 1 and 10 are chosen, and the user can be asked to guess the number."""

    def __init__(self, player_names):
        """When an instance is created, it creates two single-number guessing games and associates a name with each."""
        # Note: this is coded without a list, and is therefore bad. The objective of this and the next game is to ease you into the use of lists.
        self.players_games = []
        self.player_names = []

        for name in player_names:
            self.players_games.append(GuessingGameObj.GuessingGame())
            self.player_names.append(name)

    def getRules(self):
        """Returns a string describing what the player should do, suitable to be printed to prompt them to guess a number between 1 and 10."""
        return "Guess a number between 1 and 10. Try to solve all games at once! \nYou will get 5 chances to make the correct guess!!!"

    def allGamesDone(self):
        """Returns True if both games are finished, and False otherwise"""
        return all(game.checkGameDone() for game in self.players_games)

    def checkCorrectGuess(self, player_name, guess):
        """For each game, checks if the guess is correct for that game and marks that game complete if so."""
        if player_name in self.player_names:
            player_index = self.player_names.index(player_name)
            player_game = self.players_games[player_index]
            if not player_game.checkGameDone() and guess == player_game.num:
                player_game.markGameDone()
                return True
        return False

    ###################################################################################
    ## Functions above this point shouldn't assume anything about how i/o is handled!
    ##############################################################################

    def printGuessFeedback(self, player_name, guess):
        """Prints feedback about the guess to the terminal (std i/o). Does not print feedback from games that have been finished. Uses the names associated with each game so that the user can tell the "speakers" appart."""
        if player_name in self.player_names:
            player_index = self.player_names.index(player_name)
            player_game = self.players_games[player_index]
            if not player_game.checkGameDone():
                result = player_game.checkGuess(guess)
                if result == -1:
                    print(f"Too Low!!! says {player_name}")
                elif result == 1:
                    print(f"Too High!!! says {player_name}")
                else:
                    print(f"You got the right guess for {player_name}")
                    player_game.markGameDone()

    def playGame(self):
        """Instructs the current game instance to play itself with the user via the terminal (std i/o)."""
        print(self.getRules())

        total_guess = 5

        while not self.allGamesDone() and total_guess > 0:
            try:
                user_guess = int(input("what's your guess? "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue  # Restart the loop if the input is not a valid integer.

            for player_name in self.player_names:
                self.printGuessFeedback(player_name, user_guess)

            # Check if all games are done
            if self.allGamesDone():
                print("Congratulations! You Won the Game!!!")
                print("You guessed the correct number for all players.")
            else:
                total_guess -= 1
                print("-" * 50)
                print(f"Remaining Guesses = {total_guess}")

            if total_guess == 0:
                print("Maximum guess limit reached. The games is over.")


if __name__ == "__main__":
    num_players = int(
        input("How many players do you want to play with simultaneously??? ")
    )
    player_names = [
        input(f"Give the name for the player {i + 1}: ") for i in range(num_players)
    ]

    game = NGuessingGame(player_names)
    game.playGame()
