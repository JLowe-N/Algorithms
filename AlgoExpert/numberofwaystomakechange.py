# Given an array of distinct positive integers representing coin dominations and
# a single non-negative integer n: Write a function that returns the number of ways
# to make change for that target amount using the given coin denominations.

# Complexity - Time O(n x d) | Space O(n) - where n is target amt, d is # of denominations
def numberOfWaysToMakeChange(n, denoms):
    # Initialize an array of amounts from 0 to n
    # Iterate through for each denomination, incrementing number of ways to make
    # change.  Final element, will represent total ways to make change for target amount
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]
