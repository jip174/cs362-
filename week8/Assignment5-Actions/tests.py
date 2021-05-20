#tests.py
import unittest
import task
import sys
from math import pi
import random
from datetime import date

class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_radius(self):
        max = sys.maxsize
        min = -sys.maxsize -1
        random.seed()
        input = random.randint(min, max)
        area = task.circleRadius(input)
        test = pi * input**2
        self.assertEqual(test, area)

    def test_fl(self):
        max = sys.maxsize
        min = -sys.maxsize - 1
        random.seed()
        list = []
        for i in range(10):
            list.append(random.randint(min, max))
        listlength = len(list)
        print(listlength)
        endvalue = list[listlength-1]
        print(endvalue)
        newlist = task.firstlastlist(list)
        print(list)
        print(newlist)
        print("start: %s end: %s" % (newlist[0], newlist[1]))
        self.assertEqual(newlist[0], list[0])
        self.assertEqual(endvalue, newlist[1])
        self.assertEqual(len(newlist), 2)


    def test_datediff(self):
        d1 = date(2014, 7, 17)
        d2 = date(2013, 7, 17)
        datediff = task.twodates(d1, d2)
        print("You are: %d  days old" % datediff)
        self.assertTrue(datediff > -1)


if __name__ == '__main__':
    unittest.main()