inputString = input("Enter String :")
def checkPalindrome(inputString):
    b = len(inputString)
    if (inputString[0:b] == inputString[::-1]):
        print("True")
    else:
        print("False")

checkPalindrome(inputString)

