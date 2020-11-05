'''
This function takes in a Binary tree, and transforms it into a Right Sibling Tree,
returning the root of the mutated tree.

A right sibling tree is obtained by making every node in a Binary Tree have its
right property point to its right sibling instead of its right child.  The sibling
is the node immediately to its right on the same level or None/null if there is
no node immediately to its right.
'''
# Complexity O(N) time | O(d) space
# where N is # of nodes and d is the deepest branch of tree
# average case / balanced tree O(log N) space on call stack
# worst case / unbalanced tree (effectively linked list) O(N) space on call stack
def rightSiblingTree(root):
    mutate(root, None, None)
    return root


def mutate(node, parent, isLeftChild):
    if node is None:
        return
    left, right = node.left, node.right
    mutate(left, node, True)
    #
    if parent is None:
        node.right = None
    elif isLeftChild:
        node.right = parent.right
    else:
        if parent.right is None:
            node.right = None
        else:
            node.right = parent.right.left
    mutate(right, node, False)

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right