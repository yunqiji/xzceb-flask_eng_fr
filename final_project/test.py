import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('hello'),'Bonjour')
        self.assertEqual(english_to_french('you'),'Vous')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('bonjour'),'Hello')
        self.assertEqual(french_to_english('chat'),'Cat')

unittest.main()
