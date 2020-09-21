# Given an array, return the longest peak length in the array
# A peak is strictly increasing from left to right until it reaches it's max value
# then it strictly decreases from right to left /\

# Time Complexity O(N) - will have some duplication on peak overlap, but
# simplifies to O(N) despite while loops

# Space Complexity O(1) - only several integer variables needed
# that do not scale with input size.

def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1
            
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx
    return longestPeakLength