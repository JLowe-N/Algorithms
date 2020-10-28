'''
This function takes in a Binary Tree (where nodes have an additional pointer to
their parent node) and traverses it iteratively (no additional space complexity).
I.E. traversal should not be done recursively.  As the tree is traversed,
a callback function passed as an argument, should be called on each node.
'''

# Complexity - O(N) Time | O(1) Space
def iterativeInOrderTreeTraversal(tree, callback):
    prevNode = None
    currentNode = tree
    while currentNode is not None:
        if prevNode is None or prevNode == currentNode.parent:
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif prevNode == currentNode.left:
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif prevNode == currentNode.right:
            nextNode = currentNode.parent
        prevNode = currentNode
        currentNode = nextNode
