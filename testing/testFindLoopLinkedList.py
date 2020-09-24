from AlgoExpert import findlooplinkedlist
import unittest


class StartLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


linkedListClass = StartLinkedList
if hasattr(findlooplinkedlist, "LinkedList"):
    linkedListClass = findlooplinkedlist.LinkedList


class LinkedList(linkedListClass):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNthNode(self, n):
        counter = 1
        current = self
        while counter < n:
            current = current.next
            counter += 1
        return current


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.getNthNode(10).next = test.getNthNode(5)
        self.assertEqual(findlooplinkedlist.findLoop(test), test.getNthNode(5))
