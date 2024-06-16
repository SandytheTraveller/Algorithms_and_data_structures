from deque import Deque


def palindrome_checker(s):
    charDeque = Deque()

    for ch in s:
        charDeque.addRear(ch)

    while charDeque.size() > 1:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            return False

    return True

word = 'homie'
print(palindrome_checker(word))