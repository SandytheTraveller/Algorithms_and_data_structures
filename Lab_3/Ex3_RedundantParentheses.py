# DIFFICULT: Check whether or not a valid expression has redundant parentheses
import sys
sys.path.append("..")
from LinearStructures import Stack


# Function to check redundant parentheses in a valid expression
# It returns True is there are duplicate parentheses False otherwise
def checkRedundancy(expression):

    # set of valid operators
    operators = {"+", "-", "/", "*"}

    # create an empty stack
    st = Stack()

    # TODO

    return False


# Function that prints the result
def isRedundant(expression):
    if checkRedundancy(expression) is True:
        print("The expression has redundant parentheses")
    else:
        print("The expression has no redundant parentheses")


# Test code
if __name__ == '__main__':
    exp = "( (a + b) )"  # Redundant
    isRedundant(exp)

    exp = "( a + (b) / c )"  # Redundant
    isRedundant(exp)

    exp = "( a + ( (b + c) ) )"  # Redundant
    isRedundant(exp)

    exp = "(a + b * (c - d) )"  # Not redundant
    isRedundant(exp)
