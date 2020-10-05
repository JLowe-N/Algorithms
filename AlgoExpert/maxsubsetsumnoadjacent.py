# O(N) Time | O(1) Space
# Only need to track previous 2 results, so use variables and avoid array dupe.
# Edge cases that could expand algo. - negative number.
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[1]
    
    first = array[0]
    second = max(array[0], array[1])
    maxSum = second
    for i in range(2, len(array)):
        maxSum = max(second, first + array[i])
        first = second
        second = maxSum
    return maxSum




# # O(N) Time | O(N) Space
# def maxSubsetSumNoAdjacent(array):
#     # Cover base cases for short arrays
#     if len(array) == 0:
#         return 0
#     elif len(array) == 1:
#         return array[0]

#     # Dynamic programming - store the max sum of non-adjacent values
#     # up to the current index in new array
#     nonAdjacentSums = array[:]
#     nonAdjacentSums[1] = max(array[0], array[1])
#     for i in range(2, len(array)):
#         nonAdjacentSums[i] = max(nonAdjacentSums[i-1],
#                                  nonAdjacentSums[i-2] + array[i])
#     return nonAdjacentSums[-1]
