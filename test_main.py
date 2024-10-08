# test_main.py
import unittest
from main import add, mult

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(10, 5), 15)

    def test_add(self):
        self.assertEqual(mult(2, 3), 6)
        self.assertEqual(mult(-1, 1), -1)
        self.assertEqual(mult(10, 5), 50)

if __name__ == "__main__":
    unittest.main()
