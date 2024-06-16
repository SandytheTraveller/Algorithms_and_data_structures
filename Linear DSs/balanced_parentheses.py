# check if a string contains a balanced number of parentheses

from stack import Stack

openers = ['[', '{', '(']
closers = [']', '}', ')']

# the match is done by comparing the indexes of the two lists
# corresponding to the current open and close elements


def matches(opener, closer):
    return openers.index(opener) == closers.index(closer)

def balanced_parentheses(seq):
    s = Stack()
    for symbol in seq:
        # if the current symbol is an opening parenthesis, it is pushed into the stack
        if symbol in openers:
            s.push(symbol)
        else:
            if s.isEmpty():
                return False
            else:
                # if the current symbol is a closing parenthesis, check if the element
                # on top of the stack is an opening of the correct type
                if symbol in closers:
                    top = s.pop()
                    if not matches(top, symbol):
                        return False
    if s.isEmpty():
        return True


t = "( [ ] { } )"
print(balanced_parentheses(t))