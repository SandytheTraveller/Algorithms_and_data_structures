def fibonacciDP_optimized(n):
    # space optimized method
    f2 = 0
    f1 = 1

    if n == 0:
        return f2
    elif n == 1:
        return f1

    for i in range(2, n + 1):
        # store and reuse only the previous two number of the sequence
        f = f1 + f2
        f2 = f1
        f1 = f

    return f1

n = 10
print(fibonacciDP_optimized(n))