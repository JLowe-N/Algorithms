
'''
Given an array that can contain both positive and negative integers, find the max sum
of any subarray consisting of adjacent elements
'''

# Complexity - Time O(N) | Space O(1)
def kadanesAlgorithm(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        maxEndingHere = max(maxEndingHere + array[i], array[i])
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar