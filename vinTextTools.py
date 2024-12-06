from deep_translator import GoogleTranslator

def translateJapanese(textToTranslate, inputLanguage="ja", outputLanguage="en"):
    return ( GoogleTranslator(source=inputLanguage, target=outputLanguage).translate(textToTranslate) )
def translateAnyLanguage(textToTranslate, inputLanguage="auto", outputLanguage="en"):
    return ( GoogleTranslator(source=inputLanguage, target=outputLanguage).translate(textToTranslate) )
