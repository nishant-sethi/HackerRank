def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def hasUpper(inputString):
    return any(char.isupper() for char in inputString)

def hasLower(inputString):
    return any(char.islower() for char in inputString)

def hasAlphabet(inputString):
    return any(char.isalpha() for char in inputString)

def hasAlphaNumeric(inputString):
    return any(char.isalnum() for char in inputString)

if __name__ == '__main__':
    s = raw_input()
    print hasAlphaNumeric(s)
    print hasAlphabet(s)
    print hasNumbers(s)
    print hasLower(s)
    print hasUpper(s)