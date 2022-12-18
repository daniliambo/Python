# title Unittests Complex number Calculator
# description Unittests Complex number Calculator
# code

from math import sqrt
from ComplexNumber import ComplexNumber as CN
import unittest


class TestComplexNumber(unittest.TestCase):

    def setUp(self) -> None:
        self.complex_number = CN(1, 1)
        self.second_number = CN(1, 1)

    def test_mod(self):
        self.assertEqual(self.complex_number.module(),
                         sqrt(self.complex_number.real ** 2 + self.complex_number.imag ** 2))

    def test_sum(self):
        sum_result = self.complex_number.sum(self.second_number.__compose__())
        self.assertEqual(sum_result.real, self.complex_number.real + self.second_number.real)
        self.assertEqual(sum_result.imag, self.complex_number.imag + self.second_number.imag)

    def test_mul(self):
        mul_result = self.complex_number.mul(self.second_number)
        self.assertEqual(mul_result.real,
                         self.complex_number.real * self.second_number.real - self.complex_number.imag * self.second_number.imag)
        self.assertEqual(mul_result.imag,
                         self.complex_number.real * self.second_number.imag + self.complex_number.imag * self.second_number.real)

    def test_subtraction(self):
        sub_result = self.complex_number.sub(self.second_number)
        self.assertEqual(sub_result.real, self.complex_number.real - self.second_number.real)
        self.assertEqual(sub_result.imag, self.complex_number.imag - self.second_number.imag)

    def test_comparison(self):
        # self.assertEqual(self.complex_number, self.second_number) # wrong
        self.assertEqual(self.complex_number.imag, self.second_number.imag)
        self.assertEqual(self.complex_number.real, self.second_number.real)


if __name__ == '__main__':
    unittest.main()
