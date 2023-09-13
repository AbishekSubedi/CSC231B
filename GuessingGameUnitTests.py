import GuessingGameObjQuestion as GGOQ

####Test creation
print("TEST_init")
game = GGOQ.GuessingGame()
print("Passed")
####Test num
print("TEST_num")
number = game.num
print("The chosen number was: " + str(number))
print("Passed")
#### Test getrules
print("TEST_getRules")
print("Rules should appear here: "+game.getRules())
#### Set number to known value
game.num = 5
#### Test incorrect guess
print("TEST_xGameDone")
print(" Not Done")
correct = game.checkGameDone()
if(correct == False):
    print("   PASSED")
else:
    print("X  FAILED")
game.markGameDone()
correct = game.checkGameDone()
print(" Done")
if(correct == True):
    print("   PASSED")
else:
    print("X  FAILED")
#### Test incorrect guess
print("TEST_checkGuess")
print(" Incorrect guesses")
correct = game.checkGuess(4)
if(isinstance(correct, int) and correct < 0):
    print("   PASSED")
else:
    print("X  FAILED")
correct = game.checkGuess(7)
if(isinstance(correct, int) and correct  > 0):
    print("   PASSED")
else:
    print("X  FAILED")
#### Test correct guess
print(" Correct guesses")
correct = game.checkGuess(5)
if(isinstance(correct, int) and correct == 0):
    print("   PASSED")
else:
    print("X  FAILED")
