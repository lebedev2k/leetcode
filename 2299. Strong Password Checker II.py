def strongPasswordCheckerII(password: str) -> bool:
    isCorrectLength = len(password)>=8
    isHasLowerCaseLetter = set(password) & set([chr(i)  for i in range(ord('a'), ord('z')+1)])
    isHasUpperCaseLetter = set(password) & set([chr(i)  for i in range(ord('A'), ord('Z')+1)])
    isHasDigitCaseLetter = set(password) & set([chr(i)  for i in range(ord('0'), ord('9')+1)])
    isHasSpecialLetter = set(password) & set("!@#$%^&*()-+")
    isNotContainAdjustentDoubleLetters = True
    previousChar = ''
    for c in password:
        if c==previousChar:
            isNotContainAdjustentDoubleLetters = False
            break
        previousChar = c

    return (isCorrectLength and isHasLowerCaseLetter and isHasUpperCaseLetter and isHasDigitCaseLetter and isHasSpecialLetter and isNotContainAdjustentDoubleLetters)==True


assert strongPasswordCheckerII("IloveLe3tcode!") == True
assert strongPasswordCheckerII("Me+You--IsMyDream") == False
assert strongPasswordCheckerII("1aB!") == False