
'''
Given a sorted array of integers as well as a target integer, returns an array with
the range where the target can be found in the format [startIdx, endIdx] inclusive.
If the target is not contained in the array, returns [-1, -1]. Uses binary search
to implement the algorithm.
'''

# Iterative Solution
# Complexity - O(N log N) time | O(1) space
# where N is the number of elements in the array to be searched
def searchForRange(array, target):
    finalRange = [-1, -1]
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, True)
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, False)
    return finalRange

def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                    return
                else: 
                    right = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return
                else:
                    left = mid + 1

# Recursive Implementation
# Complexity O(N log N) time | O(N log N) space
# def searchForRange(array, target):
#     finalRange = [-1, -1]
#     alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, True)
#     alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, False)
#     return finalRange

# def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
#     if left > right:
#         return
#     mid = (left + right) // 2
#     if array[mid] < target:
#         alteredBinarySearch(array, target, mid + 1, right, finalRange, goLeft)
#     elif array[mid] > target:
#         alteredBinarySearch(array, target, left, mid - 1, finalRange, goLeft)
#     else:
#         if goLeft:
#             if mid == 0 or array[mid - 1] != target:
#                 finalRange[0] = mid
#             else: 
#                 alteredBinarySearch(array, target, left, mid - 1, finalRange, goLeft)
#         else:
#             if mid == len(array) - 1 or array[mid + 1] != target:
#                 finalRange[1] = mid
#             else:
#                 alteredBinarySearch(array, target, mid + 1, right, finalRange, goLeft)
