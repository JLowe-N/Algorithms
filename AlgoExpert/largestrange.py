# Find the largest consecutive range of integers in the array, regardless of
# array sorting.  If we sort first, time complexity is governed by the sorting
# function O(N log N).
# If we use a hash table, we can access values quickly, and iterate through 
# neighboring numbers until it is not found in the hash table.
# Once a number is visited either in the for-loop or in the consecutive number 
# search, it is already in a range and does not need to be processed again.  
# All numbers initialized as keys with the value True
# As they are visited, flip this value to False

# Using hash table, we get time complexity O(N) and space complexity O(N)

def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange