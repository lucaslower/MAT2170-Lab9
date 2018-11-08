"""
MAT 2170: Lab 9
Demonstration of graphics functions from lab9Functions.py module

Submitted by:
"""

import turtle
import lab9Functions


def demoSquare():
    # Create a turtle named bob
    bob = turtle.Turtle()

    # Set the turtle speed
    bob.speed(0)

    # Draw some squares anchored at (0,0)
    lab9Functions.drawNestedSquares(bob, 10, 400, 30)

    # Keep the turtle's screen open until the user clicks on it
    window = turtle.Screen()
    window.exitonclick()


def demoSquareVersion2():
    # Create a turtle named bob
    bob = turtle.Turtle()

    # Set the turtle speed
    bob.speed(0)

    # Draw some squares anchored at (0,0), reducing size by 90%
    lab9Functions.drawNestedSquaresVersion2(bob, 10, 400, 0.9)

    # Keep the turtle's screen open until the user clicks on it
    window = turtle.Screen()
    window.exitonclick()

      
def demoSquareVersion3():
    # Create a turtle named bob
    bob = turtle.Turtle()

    # Set the turtle speed
    bob.speed(0)

    # Draw some squares anchored at (0,0), reducing size by 90%
    # with a 10 degree turn after each square
    lab9Functions.drawNestedSquaresVersion3(bob, 10, 400, 0.9, 10)

    # Keep the turtle's screen open until the user clicks on it
    window = turtle.Screen()
    window.exitonclick()
    

if __name__ == "__main__":
    print("Beginning graphics demos...\n")

    # Demo Squares
    demoSquare()
    demoSquareVersion2()
    demoSquareVersion3()

    print("All demos complete!")
