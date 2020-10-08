'''
Demonstrates different traversal methods through a BST structure.
All methods have Time Complexity O(N) where N is number of nodes
All methods have Space Complexity O(N) due to building an array of all nodes,
but if we were printing or doing non-space operations to each node, the call stack from
recursion will cause O(d) Space complexity where d is node count for the deepest branch of the BST.
'''

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array