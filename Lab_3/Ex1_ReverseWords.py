# Reverse each word in a string using a Stack
# Words must stay in the same initial position
# E.g., "Algorithm and Data Structures" will become "mhtiroglA dna ataD serutcurtS"
import sys
sys.path.append("..")
from stack import Stack


# Reverse each word of a string maintaining their position
def reverserWords(input_string):
    revString = ""
    st = Stack()

    words = input_string.split()

    for word in words: # algorithms
        for ch in word:
            st.push(ch)
        while not st.isEmpty():
            revString = revString + st.pop()
        revString += ' '
    return revString

    # return the reversed string
    return revString


# Test Code
if __name__ == "__main__":
    myString = "Algorithms and Data Structures"
    print(reverserWords(myString))