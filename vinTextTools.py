from deep_translator import GoogleTranslator

def translateText(textToTranslate, inputLanguage="ja", outputLanguage="en"):
    return GoogleTranslator(source=inputLanguage, target=outputLanguage).translate(textToTranslate)
