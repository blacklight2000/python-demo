import unittest
from fibonacci import *

class FibonacciTest(unittest.TestCase):

    def testCase1(self):
        self.assertEqual(6765, Case1.fibonacci(20), "Case1 unit test")

    def testCase2(self):
        self.assertEqual(6765, Case2.fibonacci(20), "Case2 unit test")



if __name__ == '__main__':
    unittest.main()

