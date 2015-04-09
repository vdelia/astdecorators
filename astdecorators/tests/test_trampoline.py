import unittest
from astdecorators.trampoline import trampolined

def factorial(x, acc=1):
    if x == 0:
        return acc
    return factorial(x-1, acc=acc*x)

def fib(n):
    def fib_help(a, b, n):
        return fib_help(b, a+b, n-1) if n > 0 else a
    return fib_help(0, 1, n)

class TestTailRecElimination(unittest.TestCase):

    def test_factorial(self):
        self.assertRaises(RuntimeError, lambda: factorial(1000))

        tfactorial = trampolined(factorial)
        self.assertEqual(3628800,tfactorial(10))

        tfactorial(1000)

    def test_fib(self):
        tfib = trampolined(fib)
        self.assertRaises(RuntimeError, lambda: fib(1000))
        self.assertEqual(55, tfib(10))

        tfib(10000)

