""" Validating the 'triples' module """
from triples import triple
import unittest


class TripleTestCase(unittest.TestCase):
    '''Test Cases for triples.py module'''

    def test_is_6_the_triple_of_2(self):
        """ 2x3 == 6 """
        self.assertTrue(triple(2) == 6)

    def test_is_12_the_triple_of_4(self):
        """ 4x3 == 12 """
        self.assertTrue(triple(4) == 12)

    def test_is_15_the_triple_of_5(self):
        """ 5x3 == 15 """
        self.assertTrue(triple(5) == 15)

if __name__ == '__main__':
    unittest.main()
