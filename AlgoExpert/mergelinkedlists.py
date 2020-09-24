# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# To Do - what if LL to compare is shorter than LL to merge
# Will need to stop and the rest of the link will be correct


def mergeLinkedLists(headOne, headTwo):
    prevNodeToUpdate = None
    nodeToCompare = headOne
    nodeToMerge = headTwo
    if headTwo.value <= headOne.value:
        newHead = headTwo
    else:
        newHead = headOne

    while nodeToMerge is not None and nodeToCompare is not None:
        if nodeToMerge.value <= nodeToCompare.value:
            nextMerge = nodeToMerge.next
            nodeToMerge.next = nodeToCompare
            if prevNodeToUpdate:
                prevNodeToUpdate.next = nodeToMerge
            prevNodeToUpdate = nodeToMerge
            nodeToMerge = nextMerge
            # Do not move compare pointer until the merge pointer is larger
        else:
            # Compare node is bigger, move to next compare node
            if nodeToCompare.next is None:
                tailOne = nodeToCompare
            prevNodeToUpdate = nodeToCompare
            nodeToCompare = nodeToCompare.next
    if nodeToMerge is not None:
        tailOne.next = nodeToMerge
    return newHead
