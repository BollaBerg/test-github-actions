import unittest

from to_be_tested import func1, func2, func3

class Test(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(func1(), True)