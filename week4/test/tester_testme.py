import testme
from unittest import TestCase
import string


class testchar(TestCase):
    def test_input_char(self):
        tc = testme.inputChar()
        letters = string.ascii_letters
        if (tc.isalpha() == True):
            #print(tc)
            self.assertTrue(tc.isalpha() == True)
        else:
            temp = " "
            for temp in tc:
                if tc in string.punctuation:
                    temp = tc
                    self.assertEqual(tc, temp)


class teststring(TestCase):
    def test_input_string(self):
        ts = testme.inputString()
        count = 0
        for x in ts:
            if x.isalpha() == True or x == '\0':
                count += 1
                print(x)
            else:
                print("Invalid input")
                break
        self.assertEqual(count, 6)