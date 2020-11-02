'''
Takes in an array of integers and returns an array of the same length, where each
element in the output array corresponds to the number of integers in the input array
that are to the right of the relevant index and that are strictly smaller than
the integer at that index.
'''
# BST Solution -build result array as we build BST
# Complexity - Average Case O(N log N) time | O(N) space
# Worst Case (Unbalanced Tree / Linked List) O(N^2) | O(N) space


def rightSmallerThan(array):
    if len(array) == 0:
        return []

    rightSmallerCounts = array[:]
    lastIdx = len(array) - 1
    bst = SpecialBST(array[lastIdx])
    rightSmallerCounts[lastIdx] = 0
    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i, rightSmallerCounts)

    return rightSmallerCounts


class SpecialBST:
    def __init__(self, value):
        self.value = value
        self.leftSubtreeSize = 0
        self.left = None
        self.right = None

    def insert(self, value, idx, rightSmallerCounts, numSmallerAtInsertTime=0):
        if value < self.value:
            self.leftSubtreeSize += 1
            if self.left is None:
                self.left = SpecialBST(value)
                rightSmallerCounts[idx] = numSmallerAtInsertTime
            else:
                self.left.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)
        else:
            numSmallerAtInsertTime += self.leftSubtreeSize
            if value > self.value:
                numSmallerAtInsertTime += 1
            if self.right is None:
                self.right = SpecialBST(value)
                rightSmallerCounts[idx] = numSmallerAtInsertTime
            else:
                self.right.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)


# Naive solution - brute force
# complexity O(N^2) Time | O(N) Space
# def rightSmallerThan(array):
#     result = [0 for i in array]
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             if array[j] < array[i]:
#                 result[i] += 1
#     return result



# BST Solution - with final traversal for array construction
# Complexity - Average Case O(N log N) time | O(N) space
# Worst Case (Unbalanced Tree / Linked List) O(N^2) | O(N) space


# def rightSmallerThan(array):
#     if len(array) == 0:
#         return []

#     lastIdx = len(array) - 1
#     bst = SpecialBST(array[lastIdx], lastIdx, 0)
#     for i in reversed(range(len(array) - 1)):
#         bst.insert(array[i], i)

#     rightSmallerCounts = array[:]
#     getRightSmallerCounts(bst, rightSmallerCounts)
#     return rightSmallerCounts


# def getRightSmallerCounts(bst, rightSmallerCounts):
#     if bst is None:
#         return
#     rightSmallerCounts[bst.idx] = bst.numSmallerAtInsertTime
#     getRightSmallerCounts(bst.left, rightSmallerCounts)
#     getRightSmallerCounts(bst.right, rightSmallerCounts)


# class SpecialBST:
#     def __init__(self, value, idx, numSmallerAtInsertTime):
#         self.value = value
#         self.idx = idx
#         self.numSmallerAtInsertTime = numSmallerAtInsertTime
#         self.leftSubtreeSize = 0
#         self.left = None
#         self.right = None

#     def insert(self, value, idx, numSmallerAtInsertTime=0):
#         if value < self.value:
#             self.leftSubtreeSize += 1
#             if self.left is None:
#                 self.left = SpecialBST(value, idx, numSmallerAtInsertTime)
#             else:
#                 self.left.insert(value, idx, numSmallerAtInsertTime)
#         else:
#             numSmallerAtInsertTime += self.leftSubtreeSize
#             if value > self.value:
#                 numSmallerAtInsertTime += 1
#             if self.right is None:
#                 self.right = SpecialBST(value, idx, numSmallerAtInsertTime)
#             else:
#                 self.right.insert(value, idx, numSmallerAtInsertTime)


# Naive solution - brute force
# complexity O(N^2) Time | O(N) Space
# def rightSmallerThan(array):
#     result = [0 for i in array]
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             if array[j] < array[i]:
#                 result[i] += 1
#     return result
