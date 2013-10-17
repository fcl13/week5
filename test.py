import unittest

class Test(unittest.TestCase):

    def test(self):
        self.assertAlmostEqual(1.125, 1.12, delta=0.006)

    def test2(self):
        self.assertAlmostEqual(1.125, 1.12, delta=0.004)

