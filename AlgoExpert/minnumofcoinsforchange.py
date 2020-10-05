# Given a target amount, n, and different denominations of coins available,
# find the minimum number of coins (of types in any amount defined in denom array)
# to get target amount of money

# Complexity Time O(d * n) | Space O(n)
# where d is # of denominations, and n is target amount
def minNumberOfCoinsForChange(n, denoms):
    # iterate through the array of denominations, finding the minimum number of coins
    # for coins up to that point in the array, to make each amount between 0 and
    # n.  Dynamically solve for minimum number of coins at each position
    numOfCoins = [float("inf") for amount in range(n + 1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(n + 1):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])
    return numOfCoins[-1] if numOfCoins[-1] != float("inf") else -1
