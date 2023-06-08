
import unittest
from final_project.machinetranslation.translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        
        self.assertEqual(english_to_french('Quality'), 'Qualité')
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
       
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Qualite'), 'Hello')

unittest.main()