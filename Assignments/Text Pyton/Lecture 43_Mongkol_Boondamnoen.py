CorrectNumber = 17
UserGuess = 0
while UserGuess != CorrectNumber :
    UserGuess = int(input("Please guess a number : "))
    if UserGuess > CorrectNumber :
        print("Too Large")
    elif UserGuess < CorrectNumber :
        print("Too Small")
    elif UserGuess == CorrectNumber :
        print("Correct !!!")