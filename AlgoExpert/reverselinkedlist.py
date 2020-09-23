# Given the head of a singly linked list, reverse the linked list in place
# and return the new head.  # Each linked list node has an integer value and 
# next node property pointing to the next node or None / null if its the tail
# The linked list input will always have at least 1 node

# Complexity O(N) Time, O(1) Space
def reverseLinkedList(head):
    prevNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    return prevNode
