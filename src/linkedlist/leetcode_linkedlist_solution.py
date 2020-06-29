# -*- coding: utf-8 -*-

from collections import deque

from src.linkedlist.singlelinkedlist_solution import SingleLinkedNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy_node = SingleLinkedNode()
        node = dummy_node

        while l1 is not None and l2 is not None:
            if l1.value < l2.value:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1 is None:
            node.next = l2
        else:
            node.next = l1

        return dummy_node.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left_node = self.mergeKLists(lists[:mid])
        right_node = self.mergeKLists(lists[mid:])

        return self.mergeTwoLists(left_node, right_node)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        dummy_node = SingleLinkedNode()
        node = dummy_node
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            if l1 is not None:
                carry += l1.value
                l1 = l1.next
            if l2 is not None:
                carry += l2.value
                l2 = l2.next

            temp_node = SingleLinkedNode()
            temp_node.value = carry % 10
            node.next = temp_node

            node = node.next
            carry = carry // 10

        return dummy_node.next

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        stack_l1 = deque()
        while l1 is not None:
            stack_l1.append(l1.value)
            l1 = l1.next
        stack_l2 = deque()
        while l2 is not None:
            stack_l2.append(l2.value)
            l2 = l2.next
        dummy_node = None
        carry = 0
        while len(stack_l1) != 0 or len(stack_l2) != 0 or carry != 0:
            if len(stack_l1) != 0:
                carry += stack_l1.pop()
            if len(stack_l2) != 0:
                carry += stack_l2.pop()
            new_node = SingleLinkedNode()
            new_node.value = carry % 10
            new_node.next = dummy_node
            dummy_node = new_node
            carry //= 10
        return dummy_node

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        node = head.next
        p = self.reverseList(node)
        node.next = head
        head.next = None
        return p

    def reverseList_iteration(self, head):
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n < 0:
            return None

        fast = head
        for x in xrange(1, n):
            fast = fast.next

        if not fast:
            return head

        slow = head
        prev = None
        while fast.next:
            prev = slow
            fast = fast.next
            slow = slow.next

        if not prev:
            head = head.next
        else:
            prev.next = prev.next.next

        return head

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        node = head.next
        head.next = self.swapPairs(head.next.next)
        node.next = head
        return node

    def swapPairs_iteration(self, head):
        dummy = pre = SingleLinkedNode()
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, current = None, head

        while current and current.next:
            if current.value == current.next.value:
                while current.next and current.value == current.next.value:
                    current = current.next
                if pre:
                    pre.next = current.next
                else:
                    head = current.next
            else:
                pre = current

            current = current.next
        return head
