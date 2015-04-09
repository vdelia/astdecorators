import unittest
from astdecorators.trampoline import trampolined

def factorial(x, acc=1):
    assert x >= 0
    if x == 0:
        return acc
    return factorial(x-1, acc=acc*x)

class TestTailRecElimination(unittest.TestCase):

    def test_factorial(self):
        self.assertRaises(RuntimeError, lambda: factorial(1000))

        decorated = trampolined(factorial)

