def fibonnaci(n):
    if n <= 1:
        return n
    return fibonnaci(n - 1) + fibonnaci(n - 2)


n = 10
sequence = [fibonnaci(i) for i in range(n + 1)]
print(sequence)