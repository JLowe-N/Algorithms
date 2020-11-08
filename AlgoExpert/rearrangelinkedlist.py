'''
Takes in the head of a linked list, and mutate the list in place so that
nodes less than k are to the left, nodes equal to k are in the middle, and nodes
greater than k are on the right of the linked list.  Nodes maintain their
original relative order to each other if possible in each segment of the
rearranged list.

Returns the head of the rearranged linked list
'''
# Complexity O(N) time | O(1) space where N is the number of nodes in the Linked List
# Solution 2 - Helper Methods for cleaner code
def rearrangeLinkedList(head, k):
    smallerListHead = None
    smallerListTail = None
    equalListHead = None
    equalListTail = None
    greaterListHead = None
    greaterListTail = None

    node = head
    while node is not None:
        if node.value < k:
            smallerListHead, smallerListTail = growLinkedList(smallerListHead, smallerListTail, node)
        elif node.value > k:
            greaterListHead, greaterListTail = growLinkedList(greaterListHead, greaterListTail, node)
        else:
            equalListHead, equalListTail = growLinkedList(equalListHead, equalListTail, node)

        prevNode = node
        node = node.next
        prevNode.next = None

    firstHead, firstTail = connectLinkedLists(smallerListHead, smallerListTail, equalListHead, equalListTail)
    finalHead, _ = connectLinkedLists(firstHead, firstTail, greaterListHead, greaterListTail)
    return finalHead

def connectLinkedLists(headOne, tailOne, headTwo, tailTwo):
    newHead = headTwo if headOne is None else headOne
    newTail = tailOne if tailTwo is None else tailTwo

    if tailOne is not None:
        tailOne.next = headTwo

    return (newHead, newTail)

def growLinkedList(head, tail, node):
    newHead = head
    newTail = node

    if newHead is None:
        newHead = node
    if tail is not None:
        tail.next = node
    
    return (newHead, newTail)

# Solution 1 - Without Helper Methods (same complexities)
# def rearrangeLinkedList(head, k):
#     smallerHead = None
#     smallerTail = None
#     equalHead = None
#     equalTail = None
#     greaterHead = None
#     greaterTail = None
#     currentNode = head
#     newHead = None
#     while currentNode is not None:
#         nextNode = currentNode.next
#         if currentNode.value < k:
#             if smallerHead is None:
#                 smallerHead = currentNode
#                 smallerTail = currentNode
#             else:
#                 smallerTail.next = currentNode
#                 smallerTail = currentNode
#         elif currentNode.value == k:
#             if equalHead is None:
#                 equalHead = currentNode
#                 equalTail = currentNode
#             else:
#                 equalTail.next = currentNode
#                 equalTail = currentNode
#         else:
#             if greaterHead is None:
#                 greaterHead = currentNode
#                 greaterTail = currentNode
#             else:
#                 greaterTail.next = currentNode
#                 greaterTail = currentNode
#         currentNode = nextNode

#     if smallerHead is not None:
#         newHead = smallerHead
#         if equalHead is not None and greaterHead is not None:
#             smallerTail.next = equalHead
#             equalTail.next = greaterHead
#             greaterTail.next = None
#         elif equalHead is not None:
#             smallerTail.next = equalHead
#             equalTail.next = None
#         elif greaterHead is not None:
#             smallerTail.next = greaterHead
#             greaterTail.next = None
#         else:
#             smallerTail.next = None
#         return newHead
#     elif equalHead is not None:
#         newHead = equalHead
#         if greaterHead is not None:
#             equalTail.next = greaterHead
#             greaterTail.next = None
#         else:
#             equalTail.next = None
#         return newHead
#     elif greaterHead is not None:
#         newHead = greaterHead
#         greaterTail.next = None
#         return newHead
#     else:
#         return None
      

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None    