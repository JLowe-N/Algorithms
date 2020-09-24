# Given the head of a singly linked list with a loop, return the node
# where the loop occurs

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time Complexity O(N) - We only take N + 1 steps where N is the total number
# of elements in the list
# Space Complexity O(1) - optimal space solution without hash table
def findLoop(head):
    slowPointer = head.next
    fastPointer = head.next.next
    while slowPointer != fastPointer:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    # When slowPointer and fastPointer overlap, move the slow pointer back to
    # the beginning and start moving both pointers forward at the same pace
    # until they overlap again.  This is the node where the loop occurs.
    # This is because the distance to the loop node and the distance from the
    # start of the list are equidistant after the first while loop.
    slowPointer = head
    while slowPointer != fastPointer:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next
    return slowPointer


    

# Hash table implementation
# Time Complexity still O(N)
# Space Complexity not optimal - O(N) for hash table
# def findLoop(head):
#     visited = {}
#     node = head
#     while node not in visited:
# 		visited[node] = True
# 		node = node.next
#     return node
