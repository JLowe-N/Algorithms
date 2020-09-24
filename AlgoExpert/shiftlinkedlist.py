# Given a linked list, shift the list (wrapping elements) forward k
# positions.  k can be either positive or negative, as well as longer than
# the list length.

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Complexity O(N) Time O(1) Space
def shiftLinkedList(head, k):
    listTail = head
    listLength = 1
    while listTail.next is not None:
        listLength += 1
        listTail = listTail.next

    offset = abs(k) % listLength
    if offset == 0:
        return head

    newTailPosition = listLength - offset if k > 0 else offset
    newTail = head
    for _ in range(1, newTailPosition):
        newTail = newTail.next

    newHead = newTail.next
    newTail.next = None
    listTail.next = head
    return newHead
