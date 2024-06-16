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

    for word in input_string:
        for ch in word:
            st.push(ch)
        for _ in range(0, st.size()):
            revString += st.pop()
        st = Stack()


    # return the reversed string
    return revString


# Test Code
if __name__ == "__main__":
    myString = "Algorithm and Data Structures"
    print(reverserWords(myString))