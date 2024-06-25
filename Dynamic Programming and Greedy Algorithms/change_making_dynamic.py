"""
Solution:
1. Start computing the minimum change for one cent and store it
2. Repeat adding one cent at a time up to the amount of change we require
"""

def minChangeDP(availableCoins, change):
    minCoins = [0]*(change + 1)
    coinsUsed = [0]*(change + 1)

    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1

        for j in [c for c in availableCoins if c <= cents]:
            # store and re-use sub-problems results
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j

        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    return minCoins[change], coinsUsed


if __name__ == '__main__':
    coins = [1, 5, 10, 12, 20]
    change = 11
    print(minChangeDP(coins, change))