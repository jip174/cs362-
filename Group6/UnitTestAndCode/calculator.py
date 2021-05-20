# -*- coding: utf-8 -*-
"""
Created on Wednesday February 19, 2020
@author: Davis Henckel (henckeld)
@author: Justin Phillips (phillij6)
@author: Clifford Reiselt (reiseltc)
"""

import math


class Calculator:
    def __init__(self, precision):
        self.precision = precision

    def out(self, value):
        return "%g" % round(value, self.precision)

    def multiply(self, lhs, rhs):
        num = lhs * rhs
        return num

    def divide(self, numerator, denominator):
        return self.out(numerator / denominator)

    def sqrt(self, number):
        return self.out(math.sqrt(number))

    def square(self, number):
        num = number * number
        return num

    def reciprocal(self, number):
        return self.out(1 / number)

    def factorial(self, number):
        return self.out(math.factorial(number))

    def abs(self, number):
        return abs(number)

    def sin(self, number):
        if number % 360 == 180:
            num = 0
        elif number % 360 == 270:
            num = -1
        elif number % 360 == 0:
            num = 0
        else:
            num = math.sin(math.radians(number))
        return num

    def cos(self, number):
        return self.out(math.cos(math.degrees(number)))
