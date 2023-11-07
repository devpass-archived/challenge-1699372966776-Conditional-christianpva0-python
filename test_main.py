import unittest
from main import maximum

class TestMain(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(3, 5), 5)
        self.assertEqual(maximum(7, 2), 7)

if __name__ == '__main__':
    unittest.main()
