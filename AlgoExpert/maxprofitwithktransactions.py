'''
Given an array of positive integers representing prices of a single stock on
various days (each index in the array represents a different day), as well as
an integer k representing number of allowed (non-overlapping) transaction periods
where you can buy-sell a single unit of stock, returns the max profit of k transactions.

Can only hold one share of stock at a time, can't buy more than one share on any given day,
and can't buy a share of stock if you're still holding a share.  Also don't need
to use all k transactions if profit does not increase.
'''
# Solution 2 - Only relevant dynamic programming array rows / last 2
# Optimizes memory usage
# Complexity O(nk) time | O(n) space
# where n is the number of days / length of prices array
# k is the number of transactions allowed
def maxProfitWithKTransactions(prices, k):
    if not len(prices):
        return 0
    evenProfits = [0 for d in prices]
    oddProfits = [0 for d in prices]
    for t in range(1, k + 1):
        maxThusFar = float("-inf")
        if t % 2 == 1:
            currentProfits = oddProfits
            previousProfits = evenProfits
        else:
            currentProfits = evenProfits
            previousProfits = oddProfits
        for d in range(1, len(prices)):
            maxThusFar = max(maxThusFar, previousProfits[d - 1] - prices[d - 1])
            currentProfits[d] = max(currentProfits[d - 1], maxThusFar + prices[d])
    return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]


# Solution 1 - Full dynamic programming array
# O(nk) time | O(nk) space
# where n is number of days / elements in prices
# and k is the # of transactions we can have
# def maxProfitWithKTransactions(prices, k):
#     if not len(prices):
#         return 0
#     profits = [[0 for d in prices] for t in range(k + 1)]
#     for t in range(1, k + 1):
#         maxThusFar = float("-inf")
#         for d in range(1, len(prices)):
#             maxThusFar = max(maxThusFar, profits[t - 1][d - 1] - prices[d - 1])
#             profits[t][d] = max(profits[t][d - 1], maxThusFar + prices[d])
#     return profits[-1][-1]
