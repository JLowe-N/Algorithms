'''
Given an array of integers, find the max sum of any strictly increasing subsequence.
Array will not be empty, and will only have 1 max increasing subsequence.
Subsequence can be a single element, or the entire array itself.

Return a new array where the 1st element is the max possible sum, and the 
2nd element is the subsequence array that produces that sum.
'''

# Complexity - Time O(N^2), Space O(N) where N is the # of elements in the input array
# 2 Inner for loops leads to N^2 time, storing result array, as well as sequences
# and sum arrays leads to N space complexity


def maxSumIncreasingSubsequence(array):
    # Stores the index of the previous number in max subsequence
    sequences = [None for x in array]
    # Stores the max sum up to and including the current index of each index
    sums = array[:]
    # Stores the index of the max sum throughout the function
    maxSumIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))
