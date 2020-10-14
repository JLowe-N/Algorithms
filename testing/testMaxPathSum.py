from AlgoExpert.maxpathsum import maxPathSum
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
        self.assertEqual(maxPathSum(test), 18)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self
