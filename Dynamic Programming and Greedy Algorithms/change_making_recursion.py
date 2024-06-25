def minChangeRecursive(availableCoins, change):
    minCoins = change
    if change in availableCoins: # base case
        return 1
    else:
        for i in [c for c in availableCoins if c <= change]:
            numCoins = 1 + minChangeRecursive(availableCoins, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

if __name__ == '__main__':
    coins = [1, 5, 10, 12, 20]
    change = 36
    print(minChangeRecursive(coins, change))