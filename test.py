#!/usr/bin/python3
import unittest
from add import add

class TestSum(unittest.TestCase):
    def test_1(self):
        result1 = add(10, 5)
        self.assertEqual(result1, 15)
    def test_2(self):
        result2 = add(20, 0)
        self.assertEqual(result2, 20)
    def test_3(self):
        result3 = add(15, 10)
        self.assertEqual(result3, 25)


if __name__ == '__main__':
    unittest.main()
