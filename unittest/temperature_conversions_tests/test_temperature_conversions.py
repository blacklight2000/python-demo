""" Validate temperature conversion function """


from temperature_conversions import convert
import unittest

class TemperatureConversionsTestCase(unittest.TestCase):
    ''' TDD temperature conversions F to C and C to F. Default rounding is 0 '''

    def test_is_212f_equal_to_212f(self):
        """ 212F == 212 F """
        self.assertTrue(convert(212, "F", "F") ==  212)

    def test_convert_100c_to_100c(self):
        """ 100C == 100C """
        self.assertEqual(convert(100, "C", "C"), 100)

    def test_convert_212f_to_100c(self):
        """ 212F == 100C """
        self.assertEqual(convert(212, "F", "C"), 100)

    def test_convert_100c_to_212f(self):
        """ 100C == 212F """
        self.assertEqual(convert(100, "C", "F"), 212)

    def test_convert_32f_to_0c(self):
        """ 32F == 0C """
        self.assertEqual(convert(32, "F", "C"), 0)

    def test_convert_0c_to_32f(self):
        """ 0C == 32F """
        self.assertEqual(convert(0, "C", "F"), 32)

    def test_convert_76c_to_169_0f(self):
        """ 76C == 169F """
        self.assertTrue(convert(76, "C", "F"), 169.0)

    def test_convert_76c_to_168_8f(self):
        """ 76C == 168.8F """
        self.assertTrue(convert(76, "C", "F", 1), 168.8)


if __name__ == '__main__':
    unittest.main()
