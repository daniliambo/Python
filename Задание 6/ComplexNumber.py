# title Complex number Calculator
# description Complex number Calculator
# code

from math import sqrt
from math import atan2


class ComplexNumber():
    """
    Params:
    real and imag part

    methods:
    +sum # with second number given as 1 + j1
    +sub # -//-
    +mul # -//-
    +mod
    +arg
    +copy
    +to_string
    +comparison

    Return:
    class with different params after
    """

    def __init__(self, a, b):
        self.real = a
        self.imag = b

    def sum(self, second_number):
        return ComplexNumber(second_number.real + self.real, second_number.imag + self.imag)

    def sub(self, second_number):
        return ComplexNumber(second_number.real - self.real, second_number.imag - self.imag)

    def mul(self, second_number):
        return ComplexNumber(self.real * second_number.real - self.imag * second_number.imag, \
                             self.real * second_number.imag + self.imag * second_number.real)

    def module(self):
        return sqrt(self.real ** 2 + self.imag ** 2)

    def pos_argument(self):
        # for positive real values
        return atan2(self.imag, self.real)

    def copy(self):
        return ComplexNumber(self.real, self.imag)

    def comparison(self, second_number):
        return self.real == second_number.real and self.imag == second_number.imag

    def to_string(self, second_number=None):
        if second_number == None:
            return f'{self.real} + {self.imag}j'
        else:
            return f'{second_number.real} + {second_number.imag}j'

    def __compose__(self, second_number=None):
        if second_number == None:
            return self.real + 1j * self.imag
        else:
            return second_number.real + second_number.imag


cn = ComplexNumber(1, 1)
print(cn.sum(1 + 1j))
