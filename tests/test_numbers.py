import unittest
from app.Numbers import Numbers

class NumbersTest(unittest.TestCase):
    
    def test_if_addition_works(self):
        num = Numbers()
        result = num.add(2,2)
        self.assertEqual(result,4)

    def test_if_sub_works(self):
        num = Numbers()
        result = num.sub(10,5)
        self.assertEqual(result,5)


if __name__ == '__main__':
    unittest.main()
