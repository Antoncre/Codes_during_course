from unittest import TestCase
from code import multiply

class Test(TestCase):
    def test_mul_norm(self):
        ar = 20
        arg = 20
        expoected = 400
        self.assertEqual(multiply(ar, arg), expoected)

    def test_mul_on_minus(self):
        ar = 20
        arg = -3
        expected = -60
        self.assertAlmostEqual(multiply(ar, arg), expected, delta=0.00002)

    def test_mul_with_zero(self):
        ar = 12
        arg = 0
        self.assertEqual(multiply(ar, arg), arg)

    def test_error(self):
        with self.assertRaises(TypeError):
            multiply("sun", 'shine')

    def test_many_values(self):
        values = (1, 15, -5.0)
        expected = -75
        self.assertEqual(multiply(*values), expected)
