from AlgoExpert.iterativeinordertreetraversal import iterativeInOrderTreeTraversal
import unittest


class BinaryTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


def testCallback(testArray, tree):
    if tree is None:
        return
    testArray.append(tree.value)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2, parent=root)
        root.left.left = BinaryTree(4, parent=root.left)
        root.left.left.right = BinaryTree(9, parent=root.left.left)
        root.right = BinaryTree(3, parent=root)
        root.right.left = BinaryTree(6, parent=root.right)
        root.right.right = BinaryTree(7, parent=root.right)

        testArray = []
        def actualTestCallback(x): return testCallback(testArray, x)
        iterativeInOrderTreeTraversal(root, actualTestCallback)
        self.assertEqual(testArray, [4, 9, 2, 1, 6, 3, 7])
