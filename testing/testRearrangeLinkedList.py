from AlgoExpert import rearrangelinkedlist as program
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
        head = program.LinkedList(3)
        head.next = program.LinkedList(0)
        head.next.next = program.LinkedList(5)
        head.next.next.next = program.LinkedList(2)
        head.next.next.next.next = program.LinkedList(1)
        head.next.next.next.next.next = program.LinkedList(4)
        result = program.rearrangeLinkedList(head, 3)
        array = linkedListToArray(result)

        expected = [0, 2, 1, 3, 5, 4]
        self.assertEqual(expected, array)
