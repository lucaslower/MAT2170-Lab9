"""
MAT 2170: Lab 9
Support functions for Lab 9, which emphasizes recursion as a design technique.

Submitted by:
"""

import math


def sumOfSquares(n):
    """
    Computes the sum of the first n squares.
    
    Arguments:
        n: the number of desired terms in the sum, where n >= 0
        
    Returns:
        The sum 1**2 + 2**2 + 3**2 + ... + n**2.
    """
    # base case
    if n == 1:
        return 1
    # recursive case
    return (n**2)+sumOfSquares(n-1)


def smallestPrimeFactor(n):
    """
    Finds the smallest prime divisor of a given positive integer.

    Arguments:
        n: an integer n with n > 0

    Returns:
        The smallest prime divisor p of n.  If n = 1, the return value
        is None since n has no prime divisors.  For every value n > 1,
        there is a smallest prime number p which evenly divides n.

    Notes:
        This function should use a loop, not recursion.
    """
    # loop through every number up to n/2
    if n == 1:
        return None
    for i in range(2,n):
        # check if it is a divisor
        if n % i == 0:
            # check if it is a prime
            prime = True
            for ii in range(2,i):
                if i % ii == 0:
                    prime = False
                    break
            if prime:
                return i
    return n


def primeFactors(n):
    """
    Computes a list of all prime factors of a given positive integer.

    Arguments:
        n: an integer n with n > 0

    Returns:
        A list of all prime factors of n, in sorted order, from smallest
        to largest.  Duplicate factors should appear. For example,
        primeFactors(24) = [2, 2, 2, 3].
    """
    if n == 1:
        return []
    else:
        smallest = smallestPrimeFactor(n)
        list = primeFactors(n//smallest)
        list.insert(0, smallest)
        return list


def digitSequence(n, base):
    """
    Produce a list of all the digits of a given integer, in a desired base

    Arguments:
        n: the number to be inspected, assumed to be a non-negative integer
        base: the desired base, a whole number between 2 and 10

    Returns:
        a list of the digits of n, in the given base
    """
    if n == 0:
        return []
    else:
        seq_list = digitSequence(n//base, base)
        seq_list.append(n%base)
        return seq_list

    
def freq(myList, value):
    """
    Determine how many times a given value appears in a list

    Arguments:
        myList: a list of values
        value:  a specific value, which may or may not appear in this list

    Returns:
        the number of times value appears in myList
    """
    if len(myList) != 0:
        times = freq(myList[:-1], value)
        if myList[-1] == value:
            return times+1
        else:
            return times
    return 0


def replaceMatching(myList, alpha, beta):
    """
    Returns a copy of a list, performing substitutions for matching values
    
    Arguments:
        myList: a list of values
        alpha:  a value to be replaced
        beta:   what to replace it with
        
    Returns:
        A copy of the given list, with every occurrence of alpha replaced with
        beta.
    """
    if alpha in myList:
        replace = myList.index(alpha)
        myList[replace] = beta
        myList = replaceMatching(myList, alpha, beta)
        return myList
    return myList
    

def drawSquare(myTurtle, sideLength):
    """
    Causes a turtle to draw a square of a specified size.

    After drawing the square, the turtle returns to its original position,
    facing in its original heading, as shown below. Note the relationship
    of the square to the turtle's initial position.

             +-------+
             |       |
             |   >   |
             |       |
             +-------+

    Arguments:
        myTurtle: the turtle which is to do the drawing
        sideLength: the length of each side of the desired square

    Returns:
        None
    """

    # move to bottom right corner
    myTurtle.penup()
    for repetition in range(2):
        myTurtle.forward(sideLength/2)
        myTurtle.right(90)
    myTurtle.pendown()

    # draw the four sides
    for i in range(4):
        # Draw a side of the square
        myTurtle.forward(sideLength)

        # Turn to make a right angle, preparing for the next side
        myTurtle.right(90)

    # return to initial point, with initial heading
    myTurtle.penup()
    for repetition in range(2):
        myTurtle.forward(sideLength/2)
        myTurtle.right(90)

    myTurtle.pendown()


def drawNestedSquares(myTurtle, n, size, decrement):
    """
    Draw a collection of decreasing squares centered on a point
    
    Arguments:
        myTurtle: the turtle which does the drawing
        n: the number of desired squares
        size: the side length of the outermost square
        decrement: the difference in side lengths between adjacent squares
        
    Returns:
        None
    """
    drawSquare(myTurtle, size)
    if n != 1:
        drawNestedSquares(myTurtle, n-1, size-decrement, decrement)


def drawNestedSquaresVersion2(myTurtle, n, size, scaleFactor):
    """
    Draw a collection of decreasing squares centered on a point

    Arguments:
        myTurtle: the turtle which does the drawing
        n: the number of desired squares
        size: the side length of the outermost square
        scaleFactor: a fraction between 0 and 1 indicating how much to
                     reduce the side length from one square to the next

    Returns:
        None
    """
    pass   # THIS FUNCTION IS INCOMPLETE

    
def drawNestedSquaresVersion3(myTurtle, n, size, scaleFactor, turnAngle):
    """
    Draw a collection of decreasing squares centered on a point

    Arguments:
        myTurtle: the turtle which does the drawing
        n: the number of desired squares
        size: the side length of the outermost square
        scaleFactor: a fraction between 0 and 1 indicating how much to
                     reduce the side length from one square to the next
        turnAngle: amount, in degrees, to rotate from one square to the next

    Returns:
        None
    """
    pass   # THIS FUNCTION IS INCOMPLETE
