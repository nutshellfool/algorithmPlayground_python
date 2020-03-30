# -*- coding: utf-8 -*-
from collections import deque


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = deque([(root, 1)])
        max_depth = 0
        while stack:
            node, level = stack.pop()
            if not node.left and not node.right:
                max_depth = max(max_depth, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        return max_depth

    def maxDepth_bfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        max_depth = 0
        min_depth = 0
        current_depth = 0
        while queue:
            current_depth += 1
            batch_size = len(queue)
            for i in xrange(batch_size):
                node = queue.popleft()
                if not node.left and not node.right:
                    max_depth = max(max_depth, current_depth)
                    min_depth = min(min_depth, current_depth)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max_depth

    def maxDepth_instinct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.maxDepth_instinct(root.left), self.maxDepth_instinct(root.right)) + 1
