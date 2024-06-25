def fibonacciDP(n):
    # initialize the list with the first 2 values of the sequence
    f = [0, 1]

    for i in range(2, n + 1):
        # store and reuse each partial result
        # thus, the results of the previous steps are reused multiple times
        f.append(f[i - 1] + f[i - 2])

    return f[n] # return the n-th Fibonacci number

n = 10
print(fibonacciDP(n))