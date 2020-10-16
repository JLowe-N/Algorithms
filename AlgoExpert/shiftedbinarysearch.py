'''
Given a special sorted array of distinct integers, use binary search to return 
the index of the target search element or -1 if it is not in the array.  The sorted
array may be shifted left or right by one or more positions.
'''
# Complexity O(log N) time | O(1) space without recursion
# Where N is the number of elements in the array to be searched
def shiftedBinarySearch(array, target):
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        leftNum = array[leftIdx]
        rightNum = array[rightIdx]
        potentialMatch = array[midIdx]
        if potentialMatch == target:
            return midIdx
        if leftNum <= potentialMatch: # left side sorted
            if leftNum <= target and potentialMatch > target:
                rightIdx = midIdx - 1
            else:
                leftIdx = midIdx + 1
        else: # right side sorted
            if rightNum >= target and potentialMatch < target:
                leftIdx = midIdx + 1
            else:
                rightIdx = midIdx - 1
    return -1
