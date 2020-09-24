# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Complexity - Time O(N + M) where N is elements of LL One, and M is LL Two
# Space O(1) - in-place, mutating LL input
# Iterative Solution
def mergeLinkedLists(headOne, headTwo):
    prevNodeToUpdate = None
    nodeToCompare = headOne
    nodeToMerge = headTwo
    while nodeToMerge is not None and nodeToCompare is not None:
        if nodeToMerge.value <= nodeToCompare.value:
            nextMerge = nodeToMerge.next
            nodeToMerge.next = nodeToCompare
            if prevNodeToUpdate:
                prevNodeToUpdate.next = nodeToMerge
            prevNodeToUpdate = nodeToMerge
            nodeToMerge = nextMerge
        else:
            prevNodeToUpdate = nodeToCompare
            nodeToCompare = nodeToCompare.next
    if nodeToCompare is None:
        prevNodeToUpdate.next = nodeToMerge
    return headOne if headOne.value < headTwo.value else headTwo

# Alternative write-up for iterative solution
# def mergeLinkedLists(headOne, headTwo):
#     p1 = headOne
#     p1Prev = None
#     p2 = headTwo
#     while p1 is not None and p2 is not None:
#         if p1.value < p2.value:
#             p1Prev = p1
#             p1 = p1.next
#         else:
#             if p1Prev is not None:
#                 p1Prev.next = p2
#             p1Prev = p2
#             p2 = p2.next
#             p1Prev.next = p1
#     if p1 is None:
#         p1Prev.next = p2
#     return headOne if headOne.value < headTwo.value else headTwo

### Recursive Solution ###
# Time Complexity also O(N + M)
# Space Complexity is worse O(N + M) on average due to function calls sitting on the call stack

# def mergeLinkedLists(headOne, headTwo):
#     recursiveMerge(headOne, headTwo, None)
#     return headOne if headOne.value < headTwo.value else headTwo

# def recursiveMerge(p1, p2, p1Prev):
#     if p1 is None:
#         p1Prev.next = p2
#         return
#     if p2 is None:
#         return

#     if p1.value < p2.value:
#         recursiveMerge(p1.next, p2, p1)
#     else:
#         if p1Prev is not None:
#             p1Prev.next = p2
#         newP2 = p2.next
#         p2.next = p1
#         recursiveMerge(p1, newP2, p2)
#     return