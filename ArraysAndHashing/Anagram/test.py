from main import Anagram
import unittest

class TestStringMethods(unittest.TestCase):

    def test_nagaram(self):
        self.assertTrue(Anagram.anagram("anagram", "nagaram"))

    def test_rat(self):
        self.assertFalse(Anagram.anagram("car", "rat"))

if __name__ == "__main__":
    unittest.main()
