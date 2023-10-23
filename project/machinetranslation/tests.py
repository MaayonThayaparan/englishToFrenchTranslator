import unittest

from translator import english_to_french, french_to_english

class testEnglishtoFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('hello'),'bonjour')
        self.assertEqual(english_to_french('goodbye'),'au revoir')
        self.assertNotEqual(english_to_french('goodbye'),'goodbye','adiós')
        

class testFrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('bonjour'),'hello')
        self.assertEqual(french_to_english('au revoir'),'goodbye')
        self.assertNotEqual(french_to_english('au revoir'),'au revoir','adiós')

unittest.main()
        