'''
Given an array, whose elements correspond to the maximum number of indexes you can jump,
find the minimum number of jumps to traverse to the last element of the array
'''

# Solution 1: Dynamic Programming with Constant Number Variables
# Complexity - Time O(N) | Space O(1) - where N is length of input array
def minNumberOfJumps(array):
    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps + 1


# Solution 2: Aux. Array Used for # of Jumps To Get to Each Index
# Complexity - Time O(N^2) | Space O(N) where N is the length of the input array
# def minNumberOfJumps(array):
#     jumps = [float("inf") for x in range(len(array))]
#     jumps[0] = 0
#     for i in range(1, len(array)):
#         for j in range(0, i):
#             if array[j] + j >= i:
#                 jumps[i] = min(jumps[i], jumps[j] + 1)
#     return jumps[-1]