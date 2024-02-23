import unittest
from simplemath import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleMath.addition(2, 3), 5)
        self.assertEqual(SimpleMath.addition(-1, 1), 0)
        self.assertEqual(SimpleMath.addition(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
