# -*- coding: utf-8 -*-
"""
Created on Wednesday February 19, 2020
@author: Davis Henckel (henckeld)
@author: Justin Phillips (phillij6)
@author: Clifford Reiselt (reiseltc)
"""

import sys
from math import trunc
from unittest import TestCase
from UnitTestAndCode.calculator import Calculator
import random
import math

'''Globals'''

max = sys.maxsize
min = -sys.maxsize - 1
maxFloat = sys.float_info.max
minFloat = -sys.float_info.max - 1

'''Functions to define boundaries'''


# Returning true means number is too large
def tooLargeInt(num):
    if num > max:
        return True
    return False


# Returning true means number is too large
def tooLargeFloat(num):
    if num > maxFloat:
        return True
    return False


# Returning true means number is too small
def tooSmallInt(num):
    if num < min:
        return True
    return False


# Returning true means number is too small
def tooSmallFloat(num):
    if num < minFloat:
        return True
    return False


'''Start of Unit tests'''


class test_calc(TestCase):

    def test_out(self):
        pass

    def test_multiply(self):
        calc = Calculator(4)
        '''Basic functionality'''
        self.assertEqual(calc.multiply(2, 5), 10)  # demonstrating associativity
        self.assertEqual(calc.multiply(5, 2), 10)  # demonstrating associativity
        self.assertEqual(calc.multiply(max, 0), 0)  # 0 * anything is 0
        self.assertEqual(calc.multiply(max, 1), max)  # 1 * anything is itself
        self.assertEqual(calc.multiply(min, 1), min)  # 1 * anything is itself
        self.assertEqual(calc.multiply(-1, 1), -1)  # neg * pos = neg
        self.assertEqual(calc.multiply(-1, -1), 1)  # neg * neg = pos
        self.assertEqual(calc.multiply(1, 1), 1)  # pos * pos = pos
        '''Testing max and min int multiplication'''
        result = tooLargeInt(calc.multiply(max, 2))
        self.assertTrue(result)
        result = tooSmallInt(calc.multiply(min, 2))
        self.assertTrue(result)
        '''Testing max and min float multiplication'''
        result = tooLargeFloat(calc.multiply(maxFloat, 2))
        self.assertTrue(result)
        result = tooSmallFloat(calc.multiply(minFloat, 2))
        self.assertTrue(result)
        '''Random Testing'''
        for i in range(1, 500):  # run the test 500 times (for ints)
            KRandNum = random.randint(trunc(min / 5), trunc(max / 5))
            JRandNum = random.randint(1, 5)
            result = calc.multiply(KRandNum, JRandNum)
            smallTest = tooSmallInt(result)
            self.assertFalse(smallTest)
            largeTest = tooLargeInt(result)
            self.assertFalse(largeTest)
            self.assertEqual(KRandNum * JRandNum, result)
        for i in range(1, 500):  # run the test 500 times (for floats)
            KRandNum = random.uniform(minFloat / 5, maxFloat / 5)
            JRandNum = random.uniform(1, 5)
            result = calc.multiply(KRandNum, JRandNum)
            smallTest = tooSmallFloat(result)
            self.assertFalse(smallTest)
            largeTest = tooLargeFloat(result)
            self.assertFalse(largeTest)
            self.assertEqual(KRandNum * JRandNum, result)

    def test_divide(self):
        random.seed()
        maxInt = sys.maxsize
        min = -sys.maxsize - 1
        maxfloat = sys.float_info.max
        minfloat = -sys.float_info.max -1
        print("max: %d min: %d" %(maxInt, min))
        print("maxfloat: %d" % maxfloat)
        print("maxfloat: %d" % minfloat)
        calc = Calculator(4)
        #numerator = 4
        numerator = random.randint(min, maxInt)
        denominator = random.randint(min, maxInt)
        print("numer: %d" % numerator)
        print("demom: %d" % denominator)
        #denominator = 3
        self.assertTrue(numerator != 0)
        self.assertTrue(denominator != 0)
        output = calc.divide(numerator, denominator)
        conFloat = float(output)
        testOut = calc.out(numerator/denominator)
        print("output: %s" % output)
        self.assertTrue(conFloat < maxInt)
        self.assertTrue(conFloat > min)
        #self.assertTrue(conFloat < maxfloat)
        #self.assertTrue(conFloat > minfloat)
        self.assertEqual(output, testOut)
        # test floats
        numerator = random.uniform(min, maxInt)
        denominator = random.uniform(min, maxInt)
        print("numer: %.8f" % numerator)
        print("demom: %.8f" % denominator)
        output = calc.divide(numerator, denominator)
        conFloat = float(output)
        testOut = calc.out(numerator / denominator)
        print("output: %s" % output)
        self.assertTrue(conFloat < maxfloat)
        self.assertTrue(conFloat > minfloat)
        self.assertEqual(output, testOut)
    #   assert False

    def test_sqrt(self):
        pass

    def test_square(self):
        calc = Calculator(4)
        self.assertEqual(calc.square(1), 1)  # 1 squared = 1
        self.assertEqual(calc.square(0), 0)  # 0 squared = 0
        '''Testing Integers'''
        squareRtOfMaxI = trunc(math.sqrt(max))  # sqrt of max int
        squareRtOfMinI = (-1) * squareRtOfMaxI
        num1 = calc.square(squareRtOfMaxI)
        result = tooLargeInt(num1)  # largest int that doesn't return error
        self.assertFalse(result)
        result = tooLargeInt(calc.square(num1 + 1))  # number should return error
        self.assertTrue(result)
        '''Testing Floats'''
        squareRtOfMaxF = math.sqrt(maxFloat)
        squareRtOfMinF = (-1) * squareRtOfMaxF
        num1 = calc.square(squareRtOfMaxF)
        result = tooLargeFloat(result)  # largest float that doesn't return error
        self.assertFalse(result)
        result = tooLargeFloat(calc.square(num1 + 1))  # should return error
        self.assertTrue(result)
        '''Random Testing'''
        for i in range(1, 500):  # testing ints
            num = random.randint(0, trunc(math.sqrt(max)))
            otherNum = calc.square(num)
            result = tooLargeInt(otherNum)
            self.assertFalse(result)
            result = tooLargeFloat(result)
            self.assertFalse(result)
        for i in range(1, 500):  # testing floats
            num = random.uniform(0, math.sqrt(maxFloat - 0.001))
            otherNum = calc.square(num)
            result = tooLargeFloat(otherNum)
            self.assertFalse(result)

    def test_abs(self):
        max = sys.maxsize
        min = -sys.maxsize - 1
        maxfloat = sys.float_info.max
        minfloat = -sys.float_info.max - 1
        calc = Calculator(4)
        test = random.randint(min, max)
        input = calc.abs(test)
        testout = abs(test)
        self.assertTrue(input < max)
        self.assertTrue(input > min)
        self.assertTrue(input < maxfloat)
        self.assertTrue(input > minfloat)
        self.assertEqual(testout, input)    

    def test_sin(self):
        calc = Calculator(4)
        '''Boundary Testing'''
        self.assertEqual(calc.sin(0), 0)
        self.assertEqual(calc.sin(90), 1)
        self.assertEqual(calc.sin(180), 0)
        self.assertEqual(calc.sin(270), -1)
        self.assertEqual(calc.sin(360), calc.sin(0))
        self.assertAlmostEqual(calc.sin(max), 0, delta=1)
        self.assertAlmostEqual(calc.sin(maxFloat), 0, delta=1)
        self.assertAlmostEqual(calc.sin(min), 0, delta=1)
        self.assertAlmostEqual(calc.sin(minFloat), 0, delta=1)
        '''Random Testing'''
        for i in range(1,500):
            num = random.randint(min, max)
            numFloat = random.uniform(-2147483648, maxFloat)
            self.assertAlmostEqual(calc.sin(num), 0, delta=1)
            self.assertAlmostEqual(calc.sin(numFloat), 0, delta=1)
            
    def test_cos(self):
        pass


    def test_reciprocal(self):
        max = sys.maxsize
        min = -sys.maxsize - 1
        maxfloat = sys.float_info.max
        minfloat = -sys.float_info.max - 1
        calc = Calculator(4)
        test =  random.randint(min, max)
        input = calc.reciprocal(test)
        testout = calc.out(1/test)
        conFloat = float(input)
        testFloat = float(testout)
        self.assertTrue(conFloat < max)
        self.assertTrue(conFloat > minfloat)
        self.assertTrue(conFloat < maxfloat)
        self.assertTrue(conFloat > min)
        self.assertEqual(testFloat, conFloat)

    def test_factorial(self):
        pass


