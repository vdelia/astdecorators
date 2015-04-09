import unittest
from astdecorators.trampoline import trampolined

def factorial(x, acc=1):
    if x == 0:
        return acc
    return factorial(x-1, acc=acc*x)

class TestTailRecElimination(unittest.TestCase):

    def test_factorial(self):
        self.assertRaises(RuntimeError, lambda: factorial(1000))

        tfactorial = trampolined(factorial)
        self.assertEqual(3628800,tfactorial(10))

        try:
            tfactorial(1000)
        except:
            self.assertFalse(True, "no max recursion depth exceeded")

