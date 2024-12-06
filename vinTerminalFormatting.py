# VARIABLES
#reset
Reset = "\033[0m"

#bold and dim
Bold = "\033[1m"
Dim = "\033[2m"

#colours
Red = "\033[31m"
Green = "\033[32m"
Blue = "\033[34m"
Yellow = "\033[33m"
Magenta = "\033[35m"
Cyan = "\033[36m"

# FUNCTIONS
def printSpecial(stringToPrint="", stringAttribute="", endingCharacter="\n"): # to use multiple attributes at once, join them into a single string, using +
    global Reset
    print(f"{stringAttribute}{stringToPrint}{Reset}", end=endingCharacter)

def inputSpecial(stringToPrint="", AttributeForPrint="", AttributeForInput=""): # to use multiple attributes at once, join them into a single string, using +
    global Reset
    ###
    print(f"{AttributeForPrint}{stringToPrint}{Reset}{AttributeForInput}", end="")
    userInput = input()
    print(Reset, end="")
    ###
    return userInput
