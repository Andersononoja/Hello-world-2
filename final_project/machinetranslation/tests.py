import unittest
from translator import english_to_french
from translator import french_to_english
class TestMyModule(unittest.TestCase):
    def test_english_to_french1(self):
        self.assertNotEqual(english_to_french("None"), "")
    def test_english_to_french7(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestMyModule1(unittest.TestCase):
    def test_french_to_english3(self):
        self.assertNotEqual(french_to_english("None"), "")
    def test_french_to_english5(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
unittest.main()