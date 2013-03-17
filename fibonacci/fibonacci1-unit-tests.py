import unittest
from fibonacci1 import *

class FibonacciTest(unittest.TestCase):
    msg = "Input to fibonacci sequence must be a non-negative integer"

    def testCase1(self):
        self.assertEqual(6765, Case1.fibonacci(20), "Case1 unit test")

    def testCase2(self):
        self.assertEqual(6765, Case2.fibonacci(20), "Case2 unit test")

    def testCase1NegativeInteger_Input_Validation(self):
        self.assertTrue(self.msg, Case1.fibonacci(-1))

    def testCase1_PositiveRealNumber_Input_Validation(self):
        self.assertTrue(self.msg, Case1.fibonacci(0.5))

    def testCase1_NegativeRealNumber_Input_Validation(self):
        self.assertTrue(self.msg, Case1.fibonacci(-0.5))

    def testCase1_CharacterString_Input_Validation(self):
        self.assertTrue(self.msg, Case1.fibonacci("kk"))

    def testCase2_NegativeInteger_Input_Validation(self):
        self.assertTrue(self.msg, Case1.fibonacci(-1))

    def testCase2_PositiveRealNumber_Input_Validation(self):
        self.assertTrue(self.msg, Case1.fibonacci(0.5))

    def testCase2_NegativeRealNumber_InputValidation(self):
        self.assertTrue(self.msg, Case1.fibonacci(-0.5))

    def testCase2_CharacterString_Input_Validation(self):
        self.assertTrue(self.msg, Case1.fibonacci("kk"))


if __name__ == '__main__':
    unittest.main()

