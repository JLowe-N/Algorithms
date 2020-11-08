'''
Function that takes in a non-empty list of non-empty sorted arrays of integers
and returns a merged list of all those arrays.  Integers in the merged list
will be in sorted ascending order.
'''

# Solution 2 - Using a min heap to reduce comparison complexity
# Complexity - O(n log(k) + k) | Space (n + k)
# where n is the total number of elements and k is the number of arrays
def mergeSortedArrays(arrays):
    sortedList = []
    smallestItems = []
    for arrayIdx in range(len(arrays)):
        smallestItems.append({"arrayIdx": arrayIdx, "elementIdx": 0, "num": arrays[arrayIdx][0]})
    minHeap = MinHeap(smallestItems)
    while not minHeap.isEmpty():
        smallestItem = minHeap.remove()
        arrayIdx, elementIdx, num = smallestItem["arrayIdx"], smallestItem["elementIdx"], smallestItem["num"]
        sortedList.append(num)
        if elementIdx == len(arrays[arrayIdx]) - 1:
            continue
        minHeap.insert({"arrayIdx": arrayIdx, "elementIdx": elementIdx + 1, "num": arrays[arrayIdx][elementIdx + 1]})
    return sortedList

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
    
    # O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array
    
    # O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx]["num"] < heap[childOneIdx]["num"]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap]["num"] < heap[currentIdx]["num"]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return
                
    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx]["num"] < heap[parentIdx]["num"]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
    
    # O(1) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def isEmpty(self):
        return len(self.heap) == 0

    def peek(self):
        return self.heap[-1]
    
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
        

# Solution 1 - Compare all elements in all arrays
# Complexity O(N * k) Time | Space O(N + k) space
# Where N is the number of elements in all arrays
# and k is the number of arrays
# def mergeSortedArrays(arrays):
#     sortedList = []
#     elementIdxs = [0 for array in arrays]
#     while True:
#         smallestItems = []
#         for arrayIdx in range(len(arrays)):
#             relevantArray = arrays[arrayIdx]
#             elementIdx = elementIdxs[arrayIdx]
#             if elementIdx == len(relevantArray):
#                 continue
#             smallestItems.append({"arrayIdx": arrayIdx, "num": relevantArray[elementIdx]})
#         if len(smallestItems) == 0:
#             break
#         nextItem = getMinValue(smallestItems)
#         sortedList.append(nextItem["num"])
#         elementIdxs[nextItem["arrayIdx"]] += 1
#     return sortedList

# def getMinValue(items):
#     minValueIdx = 0
#     for i in range(1, len(items)):
#         if items[i]["num"] < items[minValueIdx]["num"]:
#             minValueIdx = i
#     return items[minValueIdx]


