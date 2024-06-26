# DIFFICULT: Check whether or not a valid expression has redundant parentheses
import sys
sys.path.append("..")
from stack import Stack


# Function to check redundant parentheses in a valid expression
# It returns True is there are duplicate parentheses False otherwise
def checkRedundancy(expression):
    # set of valid operators
    operators = {"+", "-", "/", "*"}

    # create an empty stack
    st = Stack()

    # Iterate through the given expression
    for ch in expression:

        # if current character is a close parenthesis ')'
        if ch == ')':
            top_elem = st.pop()

            # set a flag redundant to True
            redundant = True

            # Pop the top element of the stack until an open parenthesis
            while top_elem != '(':
                # check if we have an operator in the expression
                if top_elem in operators:
                    redundant = False
                top_elem = st.pop()

            # If no operator is present the parentheses are redundant
            if redundant:
                return True

        else:
            st.push(ch)  # push open parenthesis '(', operators and operands to stack

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
