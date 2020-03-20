from unittest import TestCase

from src.linkedlist.leetcode_linkedlist_solution import Solution
from src.linkedlist.singlelinkedlist_solution import SingleLinkedList


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

    def test_mergeTwoListsNoneParams(self):
        head_node = self.solution.mergeTwoLists(None, None)
        self.assertIsNone(head_node)

    def test_mergeTwoListP1None(self):
        head_node = self.solution.mergeTwoLists(None, self.list_alpha.head.next)
        self.assertIsNotNone(head_node)
        self.assertEqual(self.list_alpha.head.next, head_node)

    def test_mergeKLists(self):
        self.list_gama = SingleLinkedList()
        self.list_gama.append_node_to_tail(0)

        lists = [self.list_alpha.head.next, self.list_beta.head.next, self.list_gama.head.next]
        head_node = self.solution.mergeKLists(lists)
        self.assertIsNotNone(head_node)
        self.assertEqual(0, head_node.value)
        self.assertEqual(1, head_node.next.value)
        self.assertEqual(1, head_node.next.next.value)
        self.assertEqual(2, head_node.next.next.next.value)
        self.assertEqual(3, head_node.next.next.next.next.value)
        self.assertEqual(4, head_node.next.next.next.next.next.value)
        self.assertEqual(5, head_node.next.next.next.next.next.next.value)
        self.assertIsNone(head_node.next.next.next.next.next.next.next)

    def test_mergeKLists_none(self):
        head_node = self.solution.mergeKLists(None)
        self.assertIsNone(head_node)

    def test_mergeKList_empty(self):
        head_node = self.solution.mergeKLists([])
        self.assertEqual(None, head_node)

    def test_addTwoNumbers(self):
        l1 = SingleLinkedList()
        l1.append_node_to_tail(2)
        l1.append_node_to_tail(4)
        l1.append_node_to_tail(3)

        l2 = SingleLinkedList()
        l2.append_node_to_tail(5)
        l2.append_node_to_tail(6)
        l2.append_node_to_tail(4)
        head = self.solution.addTwoNumbers(l1.head.next, l2.head.next)
        self.assertIsNotNone(head)
        self.assertEqual(7, head.value)
        self.assertEqual(0, head.next.value)
        self.assertEqual(8, head.next.next.value)
        self.assertIsNone(head.next.next.next)

    def test_addTwoNumbers_more_digits(self):
        l1 = SingleLinkedList()
        l1.append_node_to_tail(9)
        l1.append_node_to_tail(9)
        l1.append_node_to_tail(9)

        l2 = SingleLinkedList()
        l2.append_node_to_tail(2)
        head = self.solution.addTwoNumbers(l1.head.next, l2.head.next)
        self.assertIsNotNone(head)
        self.assertEqual(1, head.value)
        self.assertEqual(0, head.next.value)
        self.assertEqual(0, head.next.next.value)
        self.assertEqual(1, head.next.next.next.value)
        self.assertIsNone(head.next.next.next.next)

    def test_addTwoNumbers_none_params(self):
        head = self.solution.addTwoNumbers(None, None)
        self.assertIsNone(head)

    def test_addTwoNumbers_none_l1_param(self):
        head = self.solution.addTwoNumbers(None, self.list_alpha.head.next)
        self.assertEqual(self.list_alpha.head.next, head)

    def test_addTwoNumbers_none_l2_param(self):
        head = self.solution.addTwoNumbers(self.list_alpha.head.next, None)
        self.assertEqual(self.list_alpha.head.next, head)
