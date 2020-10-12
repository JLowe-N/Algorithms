'''
Given an array of positive integers that represent the height of a column, calculate
the surface area of water that will be bounded between the columns (assuming each
index represents a width of 1 unit and the height is determined by the bounding pillars
and the pillar existing in the column)
  _            _      
 | |<<_ WATER>| |
_| |_| |__| |_| |_
0 2 0 1 00 1 0 2 0
'''

# Complexity - Time O(N) | Space O(N)
def waterArea(heights):
    maxes = [0 for x in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)
    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i])
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)
    return sum(maxes)
