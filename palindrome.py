def checkPalindrome(inputString):
    b = len(inputString)
    if (inputString[0:b] == inputString[::-1]):
        return True
    else:
        return False
