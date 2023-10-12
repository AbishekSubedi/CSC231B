import AIGuessingGame as AIGame

print("Testing init")
game = AIGame.AIGuessingGame()
if(game.lower_bound == 1 and game.upper_bound == 10):
    print("  Pass")
else:
    print("X Fail")

print("Testing calcGuess")
if game.calcGuess() == 5:
    print("  Pass")
else:
    print("X Fail")
    
game.lower_bound = 4
game.upper_bound = 8

if game.calcGuess() == (4+8)//2:
    print("  Pass")
else:
    print("X Fail")

game.lower_bound = 2
game.upper_bound = 5

if game.calcGuess() == (2+5)//2:
    print("  Pass")
else:
    print("X Fail")
print("Testing updateRange")

game.lower_bound = 1
game.upper_bound = 10
game.updateRange(5,-1)
if game.lower_bound == 6 and game.upper_bound == 10:
    print("  Pass")
else:
    print("X Fail")
game.lower_bound = 1
game.upper_bound = 10
game.updateRange(5,1)

if game.lower_bound == 1 and game.upper_bound == 4:
    print("  Pass")
else:
    print("X Fail")

game.lower_bound = 1
game.upper_bound = 8
game.updateRange(6,1)

if game.lower_bound == 1 and game.upper_bound == 5:
    print("  Pass")
else:
    print("X Fail")

game.lower_bound = 1
game.upper_bound = 8
game.updateRange(6,-1)

if game.lower_bound == 7 and game.upper_bound == 8:
    print("  Pass")
else:
    print("X Fail")

game.lower_bound = 1
game.upper_bound = 10
print("Testing updateRange")
print("__PRESS a__")
if game.getFeedbackFromTerminal(5) == -1 and game.lower_bound == 1 and game.upper_bound == 10:
    print("  Pass")
else:
    print("X Fail")

print("__PRESS b__")
if game.getFeedbackFromTerminal(5) == 0 and game.lower_bound == 1 and game.upper_bound == 10:
    print("  Pass")
else:
    print("X Fail")

print("__PRESS c__")
if game.getFeedbackFromTerminal(5) == 1 and game.lower_bound == 1 and game.upper_bound == 10:
    print("  Pass")
else:
    print("X Fail")

print("Testing game")
game.playGame()
