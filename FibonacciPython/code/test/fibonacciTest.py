import unittest

from code.fibonacci import Fibonacci


class test_fibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_should_fibonacci_number_of_months_one_and_pairs_produced_three_return_one(self):
        self.assertEqual(1, self.fibonacci.compute(1, 3))

    def test_should_fibonacci_number_of_months_two_and_pairs_produced_three_return_one(self):
        self.assertEqual(1, self.fibonacci.compute(2, 3))

    def test_should_fibonacci_number_of_months_three_and_pairs_produced_three_return_4(self):
        self.assertEqual(4, self.fibonacci.compute(3, 3))

    def test_should_fibonacci_number_of_months_four_and_pairs_produced_three_return_seven(self):
        self.assertEqual(7, self.fibonacci.compute(4, 3))

    def test_should_fibonacci_number_of_months_five_and_pairs_produced_three_return_nineteen(self):
        self.assertEqual(19, self.fibonacci.compute(5, 3))

    def test_should_fibonacci_number_of_months_six_and_pairs_produced_three_return_forty(self):
        self.assertEqual(40, self.fibonacci.compute(6, 3))

    def test_should_fibonacci_number_of_months_seven_and_pairs_produced_three_return_ninetyseven(self):
        self.assertEqual(97, self.fibonacci.compute(7, 3))


if __name__ == '__main__':
    unittest.main()
