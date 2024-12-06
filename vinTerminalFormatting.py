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
def specialPrint(String, Attribute, endingCharacter = "\n"): # to use multiple attributes at once, join them into a single string, using +
    global Reset
    print(f"{Attribute}{String}{Reset}", end=endingCharacter)

def specialInput(String, AttributeForPrint, AttributeForInput): # to use multiple attributes at once, join them into a single string, using +
    global Reset
    ###
    print(f"{AttributeForPrint}{String}{Reset}{AttributeForInput}", end="")
    userInput = input()
    print(Reset, end="")
    ###
    return userInput
