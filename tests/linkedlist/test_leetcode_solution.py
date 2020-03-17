from unittest import TestCase

from src.linkedlist.LeetCodeLinkedListSolution import Solution
from src.linkedlist.SingleLinkedList import SingleLinkedList


class TestLeetCodeSolution(TestCase):

    def setUp(self):
        self.solution = Solution()

        self.list_alpha = SingleLinkedList()
        self.list_alpha.append_node_to_tail(1)
        self.list_alpha.append_node_to_tail(2)
        self.list_alpha.append_node_to_tail(4)

        self.list_beta = SingleLinkedList()
        self.list_beta.append_node_to_tail(1)
        self.list_beta.append_node_to_tail(3)
        self.list_beta.append_node_to_tail(5)

    def tearDown(self):
        self.list_alpha = None
        self.list_beta = None

    def test_mergeTwoLists(self):
        head_node = self.solution.mergeTwoLists(self.list_alpha.head.next, self.list_beta.head.next)
        self.assertIsNotNone(head_node)
        self.assertEqual(1, head_node.value)
        self.assertEqual(1, head_node.next.value)
        self.assertEqual(2, head_node.next.next.value)
        self.assertEqual(3, head_node.next.next.next.value)
        self.assertEqual(4, head_node.next.next.next.next.value)
        self.assertEqual(5, head_node.next.next.next.next.next.value)
        self.assertIsNone(head_node.next.next.next.next.next.next)
