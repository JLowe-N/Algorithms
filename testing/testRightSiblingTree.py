from AlgoExpert import rightsiblingtree as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
        root.left.right.right = BinaryTree(10)
        root.right.left.left = BinaryTree(11)
        root.right.right.left = BinaryTree(12)
        root.right.right.right = BinaryTree(13)
        root.right.left.left.left = BinaryTree(14)
        mutatedRoot = program.rightSiblingTree(root)
        dfsOrder = mutatedRoot.getDfsOrder([])
        expected = [1, 2, 4, 8, 9, 5, 6, 11, 14,
                    7, 12, 13, 3, 6, 11, 14, 7, 12, 13]
        self.assertEqual(dfsOrder, expected)


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

    def getDfsOrder(self, values):
        values.append(self.value)
        if self.left is not None:
            self.left.getDfsOrder(values)
        if self.right is not None:
            self.right.getDfsOrder(values)
        return values
