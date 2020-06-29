from unittest import TestCase

from src.linkedlist.leetcode_linkedlist_solution import Solution
from src.linkedlist.singlelinkedlist_solution import SingleLinkedList, \
    SingleLinkedNode


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
        head_node = self.solution.mergeTwoLists(self.list_alpha.head.next,
                                                self.list_beta.head.next)
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
        head_node = self.solution.mergeTwoLists(None,
                                                self.list_alpha.head.next)
        self.assertIsNotNone(head_node)
        self.assertEqual(self.list_alpha.head.next, head_node)

    def test_mergeKLists(self):
        self.list_gama = SingleLinkedList()
        self.list_gama.append_node_to_tail(0)

        lists = [self.list_alpha.head.next, self.list_beta.head.next,
                 self.list_gama.head.next]
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

    def test_addTwoNumbers2(self):
        l1 = SingleLinkedList()
        l1.append_node_to_tail(7)
        l1.append_node_to_tail(2)
        l1.append_node_to_tail(4)
        l1.append_node_to_tail(3)

        l2 = SingleLinkedList()
        l2.append_node_to_tail(5)
        l2.append_node_to_tail(6)
        l2.append_node_to_tail(4)
        head = self.solution.addTwoNumbers2(l1.head.next, l2.head.next)
        self.assertIsNotNone(head)
        self.assertEqual(7, head.value)
        self.assertEqual(8, head.next.value)
        self.assertEqual(0, head.next.next.value)
        self.assertEqual(7, head.next.next.next.value)
        self.assertIsNone(head.next.next.next.next)

    def test_addTwoNumbers2_more_digits(self):
        l1 = SingleLinkedList()
        l1.append_node_to_tail(9)
        l1.append_node_to_tail(9)
        l1.append_node_to_tail(9)

        l2 = SingleLinkedList()
        l2.append_node_to_tail(2)
        head = self.solution.addTwoNumbers2(l1.head.next, l2.head.next)
        self.assertIsNotNone(head)
        self.assertEqual(1, head.value)
        self.assertEqual(0, head.next.value)
        self.assertEqual(0, head.next.next.value)
        self.assertEqual(1, head.next.next.next.value)
        self.assertIsNone(head.next.next.next.next)

    def test_addTwoNumbers2_none_params(self):
        head = self.solution.addTwoNumbers2(None, None)
        self.assertIsNone(head)

    def test_addTwoNumbers2_none_l1_param(self):
        head = self.solution.addTwoNumbers2(None, self.list_alpha.head.next)
        self.assertEqual(self.list_alpha.head.next, head)

    def test_addTwoNumbers2_none_l2_param(self):
        head = self.solution.addTwoNumbers2(self.list_alpha.head.next, None)
        self.assertEqual(self.list_alpha.head.next, head)

    def test_middleNode(self):
        node = self.solution.middleNode(self.list_alpha.head.next)
        self.assertIsNotNone(node)
        self.assertEqual(2, node.value)

    def test_middleNode_none_param(self):
        node = self.solution.middleNode(None)
        self.assertIsNone(node)

    def test_middleNode_node_length_even(self):
        list_length_even = SingleLinkedList()
        list_length_even.append_node_to_tail(1)
        list_length_even.append_node_to_tail(2)
        list_length_even.append_node_to_tail(3)
        list_length_even.append_node_to_tail(4)
        node = self.solution.middleNode(list_length_even.head.next)
        self.assertIsNotNone(node)
        self.assertEqual(3, node.value)

    def test_middleNode_node_length_odd(self):
        node = self.solution.middleNode(self.list_beta.head.next)
        self.assertIsNotNone(node)
        self.assertEqual(3, node.value)

    def test_reverseList(self):
        node = self.solution.reverseList(self.list_alpha.head.next)
        self.assertIsNotNone(node)
        self.assertEqual(4, node.value)
        self.assertEqual(2, node.next.value)
        self.assertEqual(1, node.next.next.value)
        self.assertIsNone(node.next.next.next)

    def test_reverseList_none(self):
        node = self.solution.reverseList(None)
        self.assertIsNone(node)

    def test_reverseList_single_node(self):
        input_node = SingleLinkedNode()
        node = self.solution.reverseList(input_node)
        self.assertEqual(input_node, node)

    def test_reverseList_iterate(self):
        node = self.solution.reverseList_iteration(self.list_alpha.head.next)
        self.assertIsNotNone(node)
        self.assertEqual(4, node.value)
        self.assertEqual(2, node.next.value)
        self.assertEqual(1, node.next.next.value)
        self.assertIsNone(node.next.next.next)

    def test_reverseList_iterate_none(self):
        node = self.solution.reverseList_iteration(None)
        self.assertIsNone(node)

    def test_reverseList_iterate_single_node(self):
        input_node = SingleLinkedNode()
        node = self.solution.reverseList_iteration(input_node)
        self.assertEqual(input_node, node)

    def test_removeNthFromEnd(self):
        head = self.solution.removeNthFromEnd(self.list_alpha.head.next, 2)
        self.assertIsNotNone(head)
        self.assertEqual(1, head.value)
        self.assertEqual(4, head.next.value)
        self.assertIsNone(head.next.next)

    def test_removeNthFromEnd_1element_k_equals_1(self):
        input_node = SingleLinkedNode()
        input_node.value = 1
        head = self.solution.removeNthFromEnd(input_node, 1)
        self.assertIsNone(head)

    def test_removeNthFromEnd_2elements_k_equals_2(self):
        list_local = SingleLinkedList()
        list_local.append_node_to_tail(1)
        list_local.append_node_to_tail(2)
        head = self.solution.removeNthFromEnd(list_local.head.next, 2)
        self.assertIsNotNone(head)
        self.assertEqual(2, head.value)

    def test_removeNthFromEnd_none_head(self):
        head = self.solution.removeNthFromEnd(None, 2)
        self.assertIsNone(head)

    def test_removeNthFromEnd_negative_k(self):
        head = self.solution.removeNthFromEnd(self.list_alpha.head.next, -1)
        self.assertIsNone(head)

    def test_removeNthFromEnd_k_beyond_list_length(self):
        head = self.solution.removeNthFromEnd(self.list_alpha.head.next, 4)
        self.assertIsNotNone(head)
        self.assertEqual(self.list_alpha.head.next, head)

    def test_swapPairs(self):
        head = self.solution.swapPairs(self.list_alpha.head.next)
        self.assertIsNotNone(head)
        self.assertEqual(2, head.value)
        self.assertEqual(1, head.next.value)
        self.assertEqual(4, head.next.next.value)
        self.assertIsNone(head.next.next.next)

    def test_swapPairs_none_param(self):
        head = self.solution.swapPairs(None)
        self.assertIsNone(head)

    def test_swapPairs_one_node(self):
        input_node = SingleLinkedNode()
        input_node.value = 1
        head = self.solution.swapPairs(input_node)
        self.assertEqual(input_node, head)

    def test_swapPairs_iteration(self):
        head = self.solution.swapPairs(self.list_alpha.head.next)
        self.assertIsNotNone(head)
        self.assertEqual(2, head.value)
        self.assertEqual(1, head.next.value)
        self.assertEqual(4, head.next.next.value)
        self.assertIsNone(head.next.next.next)

    def test_swapPairs_none_param_iteration(self):
        head = self.solution.swapPairs(None)
        self.assertIsNone(head)

    def test_swapPairs_one_node_iteration(self):
        input_node = SingleLinkedNode()
        input_node.value = 1
        head = self.solution.swapPairs(input_node)
        self.assertEqual(input_node, head)

    def test_deleteDuplicates(self):
        list = SingleLinkedList()
        list.append_node_to_tail(1)
        list.append_node_to_tail(1)
        list.append_node_to_tail(2)
        head = self.solution.deleteDuplicates(list.head.next)
        self.assertIsNotNone(head)
        self.assertEqual(1, head.value)
        self.assertEqual(2, head.next.value)
        self.assertIsNone(head.next.next)
