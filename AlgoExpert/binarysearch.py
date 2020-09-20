def binarySearch(array, target):
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx <= rightIdx:
        middleIdx = (leftIdx + rightIdx) // 2
        if array[middleIdx] == target:
            return middleIdx
        elif array[middleIdx] > target:
            rightIdx = middleIdx - 1
        else:
            leftIdx = middleIdx + 1
    return -1
