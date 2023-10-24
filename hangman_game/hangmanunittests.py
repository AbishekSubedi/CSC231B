import hangman as Hangman

def test_getTextPerson():
    game = Hangman.Hangman()
    print("TEST_GETTEXTPERSON")
    for i in range(game.GUESS_LIMIT+1):
        print("game stage " + str(i))
        print(game.getTextPerson(i))
    print("EVALUATE TEST BY EYE")
    print("______________________________________________")
    
    print("TEST_GETTEXTPERSON: INVALID RANGE")
    print("game stage " + str(game.GUESS_LIMIT*2))
    print(game.getTextPerson(game.GUESS_LIMIT*2))
    print("EVALUATE TEST BY EYE")
    print("______________________________________________")

    print("TEST_GETTEXTPERSON: INVALID TYPE")
    print("game stage " + "a")
    print(game.getTextPerson("a"))
    print("EVALUATE TEST BY EYE")
    print("______________________________________________")


def test_getWord():
    game = Hangman.Hangman()
    print("TEST_GETWORD")
    for i in range(5):
        print(game.getWord())
    print("EVALUATE TEST BY EYE")
    print("______________________________________________")
    
def test_allowableGuess():
    game = Hangman.Hangman()
    game.setWord("testword")
    print("TEST_ALLOWABLEGUESS")
    print("Guess 'a' (valid)")
    if(game.allowableGuess("a") == True):
        print("  PASSED")
    else:
        print("X  FAILED")
    print("______________________________________________")
    print("Repeat guess 'a' (invalid repeat)")
    game.updateGame('a')
    if(game.allowableGuess("a") == False):
        print("  PASSED")
    else:
        print("X  FAILED")
    print("______________________________________________")
    print("Guess 'aa' (invalid length)")
    if(game.allowableGuess("aa") == False):
        print("  PASSED")
    else:
        print("X  FAILED")
    print("______________________________________________")

def test_updateGame():
    game = Hangman.Hangman()
    game.setWord("testword")
    print("TEST_UPDATEGAME")
    print("Guess 'a' (not in word)")
    game.updateGame('a')
    if(game.errorCount == 1):
        print("  PASSED (errorcount)")
    else:
        print("X  FAILED (errorcount "+str(game.errorCount)+" vs 1)")
    if("".join(game.workingWord) == "--------"):
        print("  PASSED (workingWord)")
    else:
        print("X  FAILED (workingWord "+"".join(game.workingWord)+" vs --------)")
    if("".join(game.guessedAlready) in ["a", "a"] ):
        print("  PASSED (guessedAlready)")
    else:
        print("X  FAILED (guessedAlready "+"".join(game.guessedAlready)+" vs a))")
    print("______________________________________________")
    print("Guess 't' (in word)")
    game.updateGame('t')
    if(game.errorCount == 1):
        print("  PASSED (errorcount)")
    else:
        print("X  FAILED (errorcount "+str(game.errorCount)+" vs 1)")
    if("".join(game.workingWord) == "t--t----"):
        print("  PASSED (workingWord)")
    else:
        print("X  FAILED (workingWord "+"".join(game.workingWord)+" vs t--t----)")
    if("".join(game.guessedAlready) in ["at", "a"] ):
        print("  PASSED (guessedAlready)")
    else:
        print("X  FAILED (guessedAlready "+"".join(game.guessedAlready)+" vs at or a))")
    print("______________________________________________")
    print("Guess 'z' (not in word)")
    game.updateGame('z')
    if(game.errorCount == 2):
        print("  PASSED (errorcount)")
    else:
        print("X  FAILED (errorcount "+str(game.errorCount)+" vs 2)")
    if("".join(game.workingWord) == "t--t----"):
        print("  PASSED (workingWord)")
    else:
        print("X  FAILED (workingWord "+"".join(game.workingWord)+" vs t--t----)")
    if("".join(game.guessedAlready) in ["atz", "az"] ):
        print("  PASSED (guessedAlready)")
    else:
        print("X  FAILED (guessedAlready "+"".join(game.guessedAlready)+" vs atz or az))")
    print("______________________________________________")
    
def test_displaygame():
    game = Hangman.Hangman()
    game.setWord("testword")
    print("TEST_DISPLAYGAME")
    print("Guess 'a' (not in word)")
    game.updateGame('a')
    game.showInTerminal()
    print("EVALUATE BY EYE: Game with 1 wrong guess (a)")
    print("______________________________________________")
    print("Guess 't' (in word)")
    game.updateGame('t')
    game.showInTerminal()
    print("EVALUATE BY EYE: Game with 1 wrong guess (a) and 1 right guess (t)")
    print("______________________________________________")
    print("Guess 'z' (not in word)")
    game.updateGame('z')
    game.showInTerminal()
    print("EVALUATE BY EYE: Game with 2 wrong guesses (a and z) and 1 right guess (t)")
    print("______________________________________________")
    
def test_getGuessFromTerminal():
    game = Hangman.Hangman()
    print("TEST_GETGUESSFROMTERMINAL")
    print("Validate that 'a' is accepted as a guess")
    game.getGuessFromTerminal()
    print("______________________________________________")
    print("Validate that 'b' is accepted as a guess")
    game.getGuessFromTerminal()
    print("______________________________________________")
    game.updateGame('a')
    print("Validate that 'a' is now rejected as a guess (duplicate), then validate that 'c' is accepted")
    game.getGuessFromTerminal()
    print("______________________________________________")
    print("Validate that 'aa' is rejected as a guess (length), then validate that 'd' is accepted")
    game.getGuessFromTerminal()
    print("______________________________________________")

test_getTextPerson()
print("==============================================")
test_getWord()
print("==============================================")
test_allowableGuess()
print("==============================================")
test_updateGame()
print("==============================================")
test_displaygame()
print("==============================================")
test_displaygame()
print("==============================================")
test_getGuessFromTerminal()
print("==============================================")

game = Hangman.Hangman()
game.playGame()