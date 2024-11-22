import unittest
from app import arith, geom  # Replace `your_module` with the name of your script

class TestSequences(unittest.TestCase):

    def test_arith_basic(self):
        # Test a basic arithmetic sequence
        self.assertEqual(arith(1, 2, 5), [1, 3, 5, 7, 9])

    def test_arith_negative_diff(self):
        # Test with a negative difference
        self.assertEqual(arith(10, -2, 5), [10, 8, 6, 4, 2])

    def test_arith_single_term(self):
        # Test with a single term
        self.assertEqual(arith(5, 3, 1), [5])

    def test_geom_basic(self):
        # Test a basic geometric sequence
        self.assertEqual(geom(1, 2, 5), [1, 2, 4, 8, 16])

    def test_geom_fraction_ratio(self):
        # Test with a fractional ratio
        self.assertEqual(geom(8, 0.5, 4), [8, 4, 2, 1])

    def test_geom_single_term(self):
        # Test with a single term
        self.assertEqual(geom(5, 3, 1), [5])

    def test_geom_zero_ratio(self):
        # Test with a ratio of 0
        self.assertEqual(geom(10, 0, 4), [10, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()