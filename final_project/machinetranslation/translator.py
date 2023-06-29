'''Module provides functions to translate from english-to-french and french-to-english'''

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''This function returns french text from english text input''' 
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''This function returns english text from french text input''' 
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
