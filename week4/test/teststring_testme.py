import testme
from unittest import TestCase
import string

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



        #self.assertTrue(ts.isalpha() == True)

