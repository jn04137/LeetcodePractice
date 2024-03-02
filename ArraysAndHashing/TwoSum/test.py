from TwoSum import two_sum
import unittest

class TestStringMethods(unittest.TestCase):

    def test_one(self):
        self.assertEqual(two_sum([2,7,11,15], 9), [0, 1])
    
    def test_two(self):
        self.assertEqual(two_sum([3,2,4], 6), [1, 2])
    
    def test_three(self):
        self.assertEqual(two_sum([3,3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()
