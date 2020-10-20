'''
Given 2 arrays that represent BSTs and the order in which elements are inserted into 
each BST, check and return a boolean if the 2 arrays produce equivalent BSTs.
Do not construct a BST to implement this algorithm.
'''

# Solution 1 - Recursive Approach with Pointers
# Complexity - O(N^2) Time | O(d) Space
# Where N is the number of elements in the array
# Where d is the depth of the deepest branch of the array due to recursion calls
#  on the call stack
def checkBstEquality(arrayOne, arrayTwo):
    return bstEqualityHelper(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))

def bstEqualityHelper(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo
    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False
    
    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxVal)

    parentNodeValue = arrayOne[rootIdxOne]
    leftAreSame = bstEqualityHelper(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, parentNodeValue)
    rightAreSame =  bstEqualityHelper(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, parentNodeValue, maxVal)

    return leftAreSame and rightAreSame

def getIdxOfFirstSmaller(array, startingIdx, minVal):
    for i in range(startingIdx + 1, len(array)):
        if array[i] < array[startingIdx] and array[i] >= minVal:
            return i
    return -1

def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
    for i in range(startingIdx + 1, len(array)):
        if array[i] >= array[startingIdx] and array[i] <= maxVal:
            return i
    return -1

# Solution 2 - Recursive Approach with Array Copies
# Complexity - O(N^2) Time | O(N^2) Space
# def checkBstEquality(arrayOne, arrayTwo):
#     if len(arrayOne) != len(arrayTwo):
#         return False
#     if len(arrayOne) == 0 or len(arrayTwo) == 0:
#         return True
#     if arrayOne[0] != arrayTwo[0]:
#         return False
    
#     leftOne = getSmaller(arrayOne)
#     leftTwo = getSmaller(arrayTwo)
#     rightOne = getBiggerOrEqual(arrayOne)
#     rightTwo = getBiggerOrEqual(arrayTwo)

#     return checkBstEquality(leftOne, leftTwo) and checkBstEquality(rightOne, rightTwo)
    

# def getSmaller(array):
#     smaller = []
#     for i in range(1, len(array)):
#         if array[i] < array[0]:
#             smaller.append(array[i])
#     return smaller

# def getBiggerOrEqual(array):
#     biggerOrEqual = []
#     for i in range(1, len(array)):
#         if array[i] >= array[0]:
#             biggerOrEqual.append(array[i])
#     return biggerOrEqual

