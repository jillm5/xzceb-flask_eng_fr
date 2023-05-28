import unittest
from translator import *

class TestTranslator(unittest.TestCase):

    # Each test case is defined as a method starting with "test_"
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('How are you'), 'Comment vous êtes')  # Assertion to check if the result is as expected

        self.assertEqual(englishToFrench('good'), 'Bon')  # Assertion to check if the result is as expected

        self.assertNotEqual(englishToFrench('None'), '') #Test None

        self.assertNotEqual(englishToFrench(0), 0) #Test empty string


    def frenchToEnglish(self):

        self.assertEqual(frenchToEnglish('Salut'), 'Hello')  # Assertion to check if the result is as expected
   
        self.assertEqual(frenchToEnglish('bon'), 'good')  # Assertion to check if the result is as expected
   
        self.assertNotEqual(frenchToEnglish('None'), '') #Test None

        self.assertNotEqual(frenchToEnglish(0), 0) #Test empty string

    def test_hello_bonjour(self):
        frenchText = englishToFrench('Hello')
        self.assertEqual(frenchText, 'Bonjour')  # Assertion to check if the result is as expected

    def test_bonjour_hello(self):
        englishText = frenchToEnglish('Bonjour')
        print(englishText)
        self.assertEqual(englishText, 'Hello')  # Assertion to check if the result is as expected
   

# Run the tests
if __name__ == '__main__':
    unittest.main()