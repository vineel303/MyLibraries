from deep_translator import GoogleTranslator

# VARIABLES
listOfAlphabets_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listOfNumbers_asStr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# FUNCTIONS
def translateJapanese(textToTranslate, inputLanguage="ja", outputLanguage="en"):
    return ( GoogleTranslator(source=inputLanguage, target=outputLanguage).translate(textToTranslate) )
def translateAnyLanguage(textToTranslate, inputLanguage="auto", outputLanguage="en"):
    return ( GoogleTranslator(source=inputLanguage, target=outputLanguage).translate(textToTranslate) )
