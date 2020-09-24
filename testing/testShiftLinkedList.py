from AlgoExpert import shiftlinkedlist
import unittest


def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = shiftlinkedlist.LinkedList(0)
        head.next = shiftlinkedlist.LinkedList(1)
        head.next.next = shiftlinkedlist.LinkedList(2)
        head.next.next.next = shiftlinkedlist.LinkedList(3)
        head.next.next.next.next = shiftlinkedlist.LinkedList(4)
        head.next.next.next.next.next = shiftlinkedlist.LinkedList(5)
        result = shiftlinkedlist.shiftLinkedList(head, 2)
        array = linkedListToArray(result)

        expected = [4, 5, 0, 1, 2, 3]
        self.assertEqual(expected, array)
