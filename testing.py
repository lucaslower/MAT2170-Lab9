"""
MAT 2170: Lab 9
Provides some testing of the required functions
"""

from EIUunittest import *
from lab9Functions import *


def testSmallestPrimeFactor():
    print("smallestPrimeFactor...")
    assertEquals(None, smallestPrimeFactor(1))
    assertEquals(2, smallestPrimeFactor(2))
    assertEquals(3, smallestPrimeFactor(3))
    assertEquals(2, smallestPrimeFactor(4))
    assertEquals(5, smallestPrimeFactor(5))
    assertEquals(2, smallestPrimeFactor(6))
    assertEquals(7, smallestPrimeFactor(7))
    assertEquals(2, smallestPrimeFactor(8))
    assertEquals(3, smallestPrimeFactor(9))
    assertEquals(2, smallestPrimeFactor(10))
    assertEquals(11, smallestPrimeFactor(11))
    assertEquals(2, smallestPrimeFactor(12))
    assertEquals(13, smallestPrimeFactor(13))
    assertEquals(2, smallestPrimeFactor(14))
    assertEquals(3, smallestPrimeFactor(15))
    assertEquals(2, smallestPrimeFactor(16))
    assertEquals(17, smallestPrimeFactor(17))
    assertEquals(2, smallestPrimeFactor(18))
    assertEquals(19, smallestPrimeFactor(19))
    assertEquals(2, smallestPrimeFactor(20))
    assertEquals(9871247, smallestPrimeFactor(9871247))
    print("passed!")
    print()


def testPrimeFactors():
    print("primeFactors...")
    assertEquals([], primeFactors(1))
    assertEquals([2], primeFactors(2))
    assertEquals([3], primeFactors(3))
    assertEquals([2, 2], primeFactors(4))
    assertEquals([5], primeFactors(5))
    assertEquals([2, 3], primeFactors(6))
    assertEquals([7], primeFactors(7))
    assertEquals([2, 2, 2], primeFactors(8))
    assertEquals([3, 3], primeFactors(9))
    assertEquals([2, 5], primeFactors(10))
    assertEquals([11], primeFactors(11))
    assertEquals([2, 2, 3], primeFactors(12))
    assertEquals([13], primeFactors(13))
    assertEquals([2, 7], primeFactors(14))
    assertEquals([3, 5], primeFactors(15))
    assertEquals([2, 2, 2, 2], primeFactors(16))
    assertEquals([17], primeFactors(17))
    assertEquals([2, 3, 3], primeFactors(18))
    assertEquals([19], primeFactors(19))
    assertEquals([2, 2, 5], primeFactors(20))
    assertEquals([2, 3, 3, 5, 3607, 3803], primeFactors(1234567890))
    assertEquals([2, 3, 3, 5, 17, 17, 379721], primeFactors(9876543210))
    print("passed!")
    print()


def testSumOfSquares():
    print("sumOfSquares...")
    assertEquals(1, sumOfSquares(1))
    assertEquals(5, sumOfSquares(2))
    assertEquals(14, sumOfSquares(3))
    assertEquals(30, sumOfSquares(4))
    assertEquals(55, sumOfSquares(5))
    assertEquals(2870, sumOfSquares(20))
    assertEquals(41791750, sumOfSquares(500))
    print("passed!")
    print()


def testDigitSequence():
    print("digitSequence...")
    assertEquals([1, 2, 3], digitSequence(123, 10))
    assertEquals([1, 7, 3], digitSequence(123, 8))
    assertEquals([1, 1, 1, 1, 0, 1, 1], digitSequence(123, 2))
    assertEquals([1, 0, 0, 0, 0, 0, 0], digitSequence(2**6, 2))
    print("passed!")
    print()


def testFreq():
    print("freq...")
    assertEquals(0, freq([], 10))
    assertEquals(3, freq([10, 10, 20, 20, 10], 10))
    assertEquals(2, freq([10, 10, 20, 20, 10], 20))
    assertEquals(0, freq([10, 10, 20, 20, 10], 30))
    assertEquals(3, freq(["cat", "dog", "dog", "cat", "cat"], "cat"))
    assertEquals(2, freq(["cat", "dog", "dog", "cat", "cat"], "dog"))
    print("passed!")
    print()


def testReplaceMatching():
    print("replaceMatching...")
    assertEquals([], replaceMatching([], "cat", "frog"))
    assertEquals(['frog', 'dog', 'dog', 'dog', 'frog'],
                 replaceMatching(["cat", "dog", "dog", "dog", "cat"], "cat", "frog"))
    assertEquals(['cat', 'frog', 'frog', 'frog', 'cat'],
                 replaceMatching(["cat", "dog", "dog", "dog", "cat"], "dog", "frog"))
    assertEquals(['cat', 'dog', 'dog', 'dog', 'cat'],
                 replaceMatching(["cat", "dog", "dog", "dog", "cat"], "frog", "toad"))
    print("passed!")
    print()


if __name__ == "__main__":
    print("Beginning automated tests...")
    testSmallestPrimeFactor()
    testPrimeFactors()
    testSumOfSquares()
    testDigitSequence()
    testFreq()
    testReplaceMatching()
