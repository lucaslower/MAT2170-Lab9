"""
MAT 2170: Lab 9
Demonstration of non-graphics functions from lab9Functions.py module

Submitted by:
"""

import turtle
import lab9Functions


def pause():
    """
    Pause the output, waiting for a key from the user
    """
    input("Press the enter key to continue...")
    print()
    

def demoSumOfSquares(lower, upper):
    """
    Outputs the result of the sumOfSquares function for a range of values

    Arguments:
        lower: lower limit of the desired range
        upper: upper limit of the desired range

    Returns:
        None
    """
    print("sum of squares")
    for n in range(lower, upper + 1):
        print(n, lab9Functions.sumOfSquares(n))
    print()


def demoSmallestPrimeFactor(lower, upper):
    """
    Outputs the result of the smallestPrimeFactor function for a range of values

    Arguments:
        lower: lower limit of the desired range
        upper: upper limit of the desired range

    Returns:
        None
    """
    print("smallest prime factor:")
    for n in range(lower, upper + 1):
        print("Smallest prime factor of ", n, "is: ",
              lab9Functions.smallestPrimeFactor(n))
    print()


def demoPrimeFactors(lower, upper):
    """
    Outputs the result of the primeFactors function for a range of values

    Arguments:
        lower: lower limit of the desired range
        upper: upper limit of the desired range

    Returns:
        None
    """
    print("prime factors")
    for n in range(lower, upper + 1):
        print(n, lab9Functions.primeFactors(n))
    print()


def demoDigitSequence(lower, upper, base):
    """
    Outputs the result of the digitSequence function for a range of values

    Arguments:
        lower: lower limit of the desired range
        upper: upper limit of the desired range
        base:  desired base, assumed to be a whole number between 2 and 10

    Returns:
        None
    """
    print("Digit sequence, base = ", base)
    for n in range(lower, upper + 1):
        print(n, lab9Functions.digitSequence(n, base))
    print()


def demoFreq():
    """
    Outputs the result of the freq function for some typical inputs

    Arguments:
        None

    Returns:
        None
    """
    myList = [20, 10, 10, 20, 10, 30, "mat2170"]
    unique = set(myList)

    # Find the frequency of each distinct element in MyList
    for x in unique:
        print("Frequency of ", x, " in ", myList, "is: ",
              lab9Functions.freq(myList, x))

    # Find the frequency of an element not in the list
    x = 5
    print("Frequency of ", x, " in ", myList, "is: ",
              lab9Functions.freq(myList, x))
    print()


def demoReplaceMatching():
    """
    Outputs the result of the replace function for some typical inputs

    Arguments:
        None

    Returns:
        None
    """
    myList = [20, 10, 10, 20, 10, 30, "mat2170"]
    replacements = [[20, 77], [10, 88], [30, 99],
                    ["mat2170", "mat1441"], [40, 55]]

    # Find the frequency of each distinct element in MyList
    for pair in replacements:
        this = pair[0]
        that = pair[1]
        result = lab9Functions.replaceMatching(myList, pair[0], pair[1])
        print("original:    ", myList, pair[0], "-->", pair[1])
        print("replacement: ", result)
        print()
    print()

    
if __name__ == "__main__":
    print("Beginning demos...\n")

    # Sum of squares
    demoSumOfSquares(1, 10)
    pause()

    # Prime factors and factorization
    demoSmallestPrimeFactor(1, 30)
    pause()
    demoPrimeFactors(1, 30)
    pause()

    # Digit sequences in various bases
    demoDigitSequence(1, 30, 2)
    demoDigitSequence(100, 127, 2)
    demoDigitSequence(1, 30, 5)
    demoDigitSequence(1234, 1245, 10)
    pause()

    # Frequency
    demoFreq()
    pause()

    # Replace
    demoReplaceMatching()

    print("All demos complete!")
