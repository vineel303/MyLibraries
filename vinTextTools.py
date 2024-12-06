from deep_translator import GoogleTranslator

def translateText(text, inputLanguage="auto", outputLanguage="en"):
    return GoogleTranslator(source=inputLanguage, target=outputLanguage).translate(text)
