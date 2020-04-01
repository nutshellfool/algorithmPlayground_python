# -*- coding: utf-8 -*-
from collections import deque
from sys import maxsize


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        depth, min_depth = 0, 1
        queue = deque()
        queue.append(root)
        while queue:
            depth += 1
            batch_size = len(queue)
            for i in xrange(batch_size):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return min_depth

    def minDepth_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        min_depth = maxsize
        stack = deque()
        stack.append((root, 1))
        while stack:
            node, level = stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        return min_depth

    def minDepth_recursion(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left:
            return self.minDepth_recursion(root.right) + 1
        if not root.right:
            return self.minDepth_recursion(root.left) + 1
        return min(self.minDepth_recursion(root.left), self.minDepth_recursion(root.right)) + 1

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            level_list_item = []
            batch_size = len(queue)
            for i in xrange(batch_size):
                node = queue.popleft()
                level_list_item.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_list_item)

        return result

    def levelOrder_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None

        result = []
        stack = deque()
        stack.append((root, 0))
        while stack:
            node, level = stack.pop()
            if len(result) <= level:
                result.append([])
            result[level].append(node.val)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return result
