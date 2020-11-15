import unittest

from to_be_tested import func1, func2, func3, func4

class Test(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(func1(), True)

    def test_func2(self):
        self.assertEqual(func2(10, 20), 30)

    def test_func3(self):
        self.assertEqual(func3(20, 10), 10)

    def test_func4(self):
        self.assertEqual(func4(20, 10), 200)