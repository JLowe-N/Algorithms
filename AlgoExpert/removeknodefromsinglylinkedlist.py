# With a singly linked list input, remove the kTh node from the end
# of ths list.  Removal should be done in place.  If head is removed, reset
# head to the next element
# Input linked list will always have at least two nodes, and at least
# k nodes

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time, O(1) space
def removeKthNodeFromEnd(head, k):
    finishPointer = head
    targetPointer = head
    for _ in range(k):
        finishPointer = finishPointer.next

    # if finish pointer passes the last list element, target element is the head
    # If so, reset the head to next element
    if finishPointer is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    
    # Move all pointers along the list, with target pointer k positions behind
    # end pointer
    while finishPointer is not None:
        finishPointer = finishPointer.next
        prevNode = targetPointer
        targetPointer = targetPointer.next

    # Finally update the prevNode's next reference
    # then garbage collect the target node
    prevNode.next = targetPointer.next
    targetPointer.value = None
    targetPointer.next = None