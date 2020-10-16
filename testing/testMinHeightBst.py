from AlgoExpert import minheightbst as program
import unittest


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)


def getTreeHeight(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        tree = program.minHeightBst(array)

        self.assertTrue(validateBst(tree))
        self.assertEqual(getTreeHeight(tree), 4)

        inOrder = inOrderTraverse(tree, [])

        self.assertEqual(inOrder, [1, 2, 5, 7, 10, 13, 14, 15, 22])
