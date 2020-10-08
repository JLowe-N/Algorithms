"""
Binary Search Tree Construction
Binary search tree has value, left, and right properties.
Left and Right point to another node/sub-BST, where the value of the left node
is strictly less than it's parent node.  The value of the right node is greater
than or equal to the parent node.

The BST class supports inserting values into the tree with the insert method.
The BST class supports searching for a value in the tree and will return a bool.
The BST class supports removing a value from the tree, while maintaining the BST
property.  If value is the only node in the tree, it will not be removed.

Due to the nature of the BST, insertion, searching, and removal have an average time
complexity of O(log N) where N is the number of elements in the tree.  This is because
we can eliminate half of the remaining tree from consideration at each iteration by following
the BST comparisons.  In the case of an unbalanced tree where all elements are on
a single branch, our worst case time complexity is O(N) time.  This is because we can't use
the BST property to reduce the elements we iterate through.

Due to the iterative nature of this implementation, space complexity is O(1)
constant space.  A recursive implementation would result in worse space complexity
because each level of recursion would remain on the call stack until we reach a leaf node.
The average and worst cases for space complexity during recursion will mirror the time
complexity where space grows O(log N) for the average case, and O(N) for the worst case
which represents an unbalanced or single branch tree.
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value >= currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value > currentNode.value:
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                return True
        return False

    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            if value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
