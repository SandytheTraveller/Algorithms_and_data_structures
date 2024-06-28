# Compute the Pascal's Triangle using recursion
#
#         1           n = 0
#       1   1         n = 1
#     1   2   1       n = 2
#   1   3   3   1     n = 3
# 1   4   6   4   1   n = 4
# ...
#
# You can print the triangle like this:
#
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# ...
#
# NOTE: You can use iterative loop(s) inside recursion


def pascal(n):
    if n == 0:
        return [1]

    previous = pascal(n - 1)
    current = [1]
    for i in range(1, len(previous)):
        current.append(previous[i - 1] + previous[i])
    current.append(1)
    return current


if __name__ == "__main__":
    n = 4
    for i in range(n+1):
        print(pascal(i))

