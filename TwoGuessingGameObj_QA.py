import TwoGuessingGameObj as TGG

def init_game():
    game = TGG.TwoGuessingGame()
    game.game1.num = 4
    game.game2.num = 6
    return game

print("----------------------------------------------------------------------")
print("Testing __init__")
game = init_game()
print("__init__ succeeded")

print("----------------------------------------------------------------------")
print("Testing getRules")
print("Rules should appear here: ", game.getRules())

print("----------------------------------------------------------------------")
print("Testing allGamesDone")
if(game.allGamesDone() == False):
    print("  Passed")
else:
    print("X FAILED")
game.game1.markGameDone()
if(game.allGamesDone() == False):
    print("  Passed")
else:
    print("X FAILED")
game = init_game()
game.game2.markGameDone()
if(game.allGamesDone() == False):
    print("  Passed")
else:
    print("X FAILED")
game.game1.markGameDone()
if(game.allGamesDone() == True):
    print("  Passed")
else:
    print("X FAILED")

print("----------------------------------------------------------------------")
print("Testing printGuessFeedback")
game = init_game()
print("Testing both too low (2 responses)")
game.printGuessFeedback(2)
game.checkCorrectGuess(2)
print("Testing both too high (2 responses)")
game.printGuessFeedback(9)
game.checkCorrectGuess(9)
print("Testing between")
game.printGuessFeedback(5)
game.checkCorrectGuess(5)
print("Testing first correct (2 responses)")
game.printGuessFeedback(4)
print("Testing second correct (2 responses)")
game.printGuessFeedback(6)

print("----------------------------------------------------------------------")
print("Testing printGuessFeedback, first game finished")
game = init_game()
game.checkCorrectGuess(4)
print("Testing too low (1 response)")
game.printGuessFeedback(4)
print("Testing too high (1 response)")
game.printGuessFeedback(8)
print("Testing correct (1 response)")
game.printGuessFeedback(6)
print("----------------------------------------------------------------------")
print("Testing printGuessFeedback, second game finished")
game = init_game()
game.game2.markGameDone()
game.checkCorrectGuess(6)
print("Testing too low (1 response)")
game.printGuessFeedback(3)
print("Testing too high (1 response)")
game.printGuessFeedback(6)
print("Testing correct (1 response)")
game.printGuessFeedback(4)
