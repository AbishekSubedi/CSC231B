import random


class Hangman:
    def __init__(self):
        """Set up the hangman game by getting the word to guess and initializing the game's state"""
        self.setWord(self.getWord())
        self.gameWon = False
        self.gameLost = False
        self.errorCount = 0
        self.GUESS_LIMIT = 6

    def setWord(self, word):
        """Sets the given word as the word to guess, updating the working word and the list of already guessed letters as well."""
        self.wordToGuess = word  # .lower()
        self.workingWord = ["-"] * len(self.wordToGuess)
        self.guessedAlready = []

    # The functions above this point are "given," you don't need to modify them.

    def getWord(self):
        """Returns a word to be guessed. Currently just returns HelloWorld."""
        return random.choice(open("usa.txt", "r").readlines()).split()

    def getTextPerson(self, stage):
        """Returns a single string, suitable to be printed, depicting the person at the given stage of the game."""
        if stage == 0:
            return ""
        elif stage == 1:
            return """
                     |--------
                     |       O
                     |
                     |
                     |
                     ==============
        """
        elif stage == 2:
            return "\O"
        elif stage == 3:
            return "\O/"
        elif stage == 4:
            return "\O/\n |"
        elif stage == 5:
            return "\O/\n |\n/"
        elif stage == 6:
            return "\O/\n |\n/ \\"

    def allowableGuess(self, guess):
        """Returns true if guess is a single letter string that does not appear in guessedAlready. Assumes guess is a string."""
        if len(guess) != 1 or not guess.isalpha():
            return False
        else:
            return guess not in self.guessedAlready

    def updateGame(self, guess):
        """Updates the game's state in response to the provided guess. Updates workingWord, guessedAlready, errorCount, and whether the game is won or lost."""
        if self.allowableGuess(guess):
            self.guessedAlready.append(guess)
            if guess in self.wordToGuess:
                for i in range(len(self.wordToGuess)):
                    if self.wordToGuess[i] == guess:
                        self.workingWord[i] = guess
                if "-" not in self.workingWord:
                    self.gameWon = True
            else:
                self.errorCount += 1
                if self.errorCount == self.GUESS_LIMIT:
                    self.gameLost = True

    ###Functions below this point assume that the game is being played on the terminal, and can use print and input.
    def showInTerminal(self):
        """Prints the current state of the game to the terminal (the ASCII graphic of the person, the working state of the word, and the letters guessed so far)."""

    def getGuessFromTerminal(self):
        """Gets the next guess from the user.
        Returns the user's guess if and only if the guess is allowable
        Repeats untill the user enters an allowable guess.
        """

    def playGame(self):
        """Instructs the game to play itself with the user in the terminal."""


if __name__ == "__main__":
    game = Hangman()
    game.playGame()
