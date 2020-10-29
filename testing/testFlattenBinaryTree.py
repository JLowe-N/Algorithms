from AlgoExpert import flattenbinarytree as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1).insert([2, 3, 4, 5, 6])
        root.left.right.left = BinaryTree(7)
        root.left.right.right = BinaryTree(8)
        leftMostNode = program.flattenBinaryTree(root)
        leftToRightToLeft = leftMostNode.leftToRightToLeft()
        expected = [4, 2, 7, 5, 8, 1, 6, 3, 3, 6, 1, 8, 5, 7, 2, 4]
        self.assertEqual(leftToRightToLeft, expected)


class BinaryTree(program.BinaryTree):
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

    def leftToRightToLeft(self):
        nodes = []
        current = self
        while current.right is not None:
            nodes.append(current.value)
            current = current.right
        nodes.append(current.value)
        while current is not None:
            nodes.append(current.value)
            current = current.left
        return nodes
