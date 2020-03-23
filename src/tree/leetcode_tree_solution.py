# -*- coding: utf-8 -*-
from collections import deque
from sys import maxsize


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        minint = - maxsize - 1
        return self._valid_bst(root, minint - 1, maxsize + 1)

    def _valid_bst(self, root, min, max):
        if not root:
            return True
        if root.val >= max or root.val <= min:
            return False
        return self._valid_bst(root.left, min, root.val) and self._valid_bst(root.right, root.val, max)

    def isValidBST_instinct(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        in_order_traversal = self._traversal_tree_in_order(root)

        return self._is_list_in_ascend_order(in_order_traversal)

    def _traversal_tree_in_order(self, root):
        traversal_list = []
        self._traversal_in_order_bst_helper(root, traversal_list)
        return traversal_list

    def _traversal_in_order_bst_helper(self, node, result):
        if not node:
            return
        self._traversal_in_order_bst_helper(node.left, result)
        result.append(node.val)
        self._traversal_in_order_bst_helper(node.right, result)

    @staticmethod
    def _is_list_in_ascend_order(order_list):
        for i in xrange(1, len(order_list)):
            if order_list[i] < order_list[i - 1]:
                return False
        return True

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self._traversal_tree_in_order(root)

    def inorderTraversal_iteration(self, root):
        result_list = []
        stack = deque()
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result_list.append(current.val)
            current = current.right
        return result_list

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        self._traversal_tree_pre_order(root, result_list)
        return result_list

    def _traversal_tree_pre_order(self, root, result):
        if not root:
            return
        result.append(root.val)
        self._traversal_tree_pre_order(root.left, result)
        self._traversal_tree_pre_order(root.right, result)

    def preorderTraversal_iteration(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        stack = deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                result_list.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return result_list

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        self._traversal_tree_post_order(root, result_list)
        return result_list

    def _traversal_tree_post_order(self, root, result):
        if not root:
            return
        self._traversal_tree_post_order(root.left, result)
        self._traversal_tree_post_order(root.right, result)
        result.append(root.val)

    def postorderTraversal_iteration(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        stack = deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                result_list.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return result_list[::-1]

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if not left:
        #     return right
        # else:
        #     if not right:
        #         return left
        #     else:
        #         return root
        return root if left and right else left or right
