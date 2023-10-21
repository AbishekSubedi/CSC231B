import GuessingGameObjQuestion as SinglePlayerGuess
import NGuessingGame as NPlayerGuess
import AIGuessingGame as ComputerGuess


class GamesSession:
    """This is a launcher for the games you made in the first part of the semester"""

    def __init__(self):
        self.is_running = True

    def numberGameSubmenu(self):
        """This sub-menu should ask you to pick the vs. one or vs. many guessing game"""
        while True:
            print("-" * 50)
            try:
                print("a - One player\nb - Three player\nc - Five player\nq - back")
                player_option = input("How many players do you want to play with: ")

                if player_option == "a":
                    SinglePlayerGuess.GuessingGame().playGame()
                elif player_option == "b":
                    NPlayerGuess.NGuessingGame(["Gon", "Ned", "Nick"]).playGame()

                elif player_option == "c":
                    NPlayerGuess.NGuessingGame(
                        ["Gon", "Ned", "Nick", "Ashlee", "John"]
                    ).playGame()
                elif player_option == "q":
                    return  # Returns to the main menu
                else:
                    print("Try again! Choose among a-c")
                    print("-" * 50)
            except Exception as e:
                print(f"Errors {e}")
                print("-" * 50)

    def playGames(self):
        """This should contain the primary menu, asking you to choose to guess the Comp's number or have the Comp guess your number"""
        while self.is_running:
            print(
                "Welcome to the game center. You can choose three types of game that you want to play"
            )
            print("-" * 50)
            try:
                print(
                    "1 - Single player game \n2 - Multiple player game \n3 - Computer guess game \n4 - quit or exit"
                )
                game_option = input("Choose the type of game you want to play: ")

                if game_option == "1":
                    SinglePlayerGuess.GuessingGame().playGame()
                    print("-" * 50)
                elif game_option == "2":
                    self.numberGameSubmenu()
                elif game_option == "3":
                    ComputerGuess.AIGuessingGame().playGame()
                    print("-" * 50)
                elif game_option == "4":
                    self.is_running = False  # Marks the end of loop
                    print("Goodbye!")
                else:
                    print("Invalid Option. Choose from 1-4")
                    print("-" * 50)
            except Exception as e:
                print(f"Errors {e}")
                print("Try Again!")
                print("-" * 50)


# Note: this is the propper way to include demo code in your file.
#   As you might have guessed, I didn't know how to do this at the beginning of the semester!
if __name__ == "__main__":
    games = GamesSession()
    games.playGames()
