import unittest

from jenkinspy.Numbers import Math

class NumbersTest(unittest.TestCase):
    
    def test_if_addition_works(self):
        num = Math()
        result = num.add(2, 2)
        self.assertEqual(result, 4)

    def test_if_sub_works(self):
        num = Math()
        result = num.sub(10, 5)
        self.assertEqual(result, 5)

    def test_if_mult_works(self):
        num = Math()
        result = num.mult(15, 2)
        self.assertEqual(result, 30)


if __name__ == '__main__':
    unittest.main()
