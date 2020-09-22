# Quicksort uses a pivot to compare to, and iterate through all elements
# moving elements with respect to the pivot
# Pick a pivot - first element pivot for simple example
# Use 2 pointers - left and right.  For ascending order, left pointer should be
# smaller than pivot, right pointer greater than pivot.  If a pointer is correct,
# move the pointer inward.  If both pointers are wrong, then swap the elements.
# Once the left pointer is past the right pointer, swap the pivot with the right pointer
# A new pivot has been chosen so repeat this process.  Can have up to 2 subarrays
# that need sorted.  Due to recursion, best to work on the smaller subarray first.

# 1. Pick Pivot 2. Iterate through with left & right pointer, moving pointers or
# swap elements 3. Do a final swap, now have 2 subarrays to work through with
# new pivots

# Time Complexity  Worst O(N^2) if pivot poorly chosen - left with large, small 
# unsorted arrays.  Best Case O(N log N) - good pivot is the median - splits array 
# in half.  Average Case O(N log N)
# Space Complexity - O(log N) - need to use recursion, memory usage
# due to using space on call stack.  Tail recursion comes in play
# A bad implementation may cause O(N) space due to recursion - always work 
# on smaller subarray first in recursion.

def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, startIdx, endIdx):
    # Base Case
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(pivotIdx, rightIdx, array)
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)
            
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    