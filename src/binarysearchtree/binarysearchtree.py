# -*- coding: utf-8 -*-
from Queue import PriorityQueue
from collections import deque


class BinaryTreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def __cmp__(self, other):
        return other.val - self.val


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if self.root is None:
            self.root = BinaryTreeNode(value)

        self._add_node_to_tree(self.root, value)

    def _add_node_to_tree(self, root, value):
        if root is None:
            return BinaryTreeNode(value)
        if root.val == value:
            root.val = value
        elif root.val < value:
            root.right = self._add_node_to_tree(root.right, value)
        else:
            root.left = self._add_node_to_tree(root.left, value)
        return root

    def print_tree(self):
        if self.root is None:
            return []
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node is None:
            return
        result.append(node.val)
        self._inorder_traversal(node.left, result)
        self._inorder_traversal(node.right, result)

    def find_node(self):
        pass

    def delete_tree(self):
        self.root = None

    def dfs(self):
        if self.root is None:
            return []
        result = []
        stack = []
        visited = set()
        stack.append(self.root)
        visited.add(self.root)
        while stack:
            node = stack.pop()
            visited.add(node)

            # do something
            result.append(node.val)

            # if not visited.__contains__(node):
            if node.left and node.left not in visited:
                stack.append(node.left)
            if node.right and node.right not in visited:
                stack.append(node.right)
        return result

    def bfs(self):
        if self.root is None:
            return []

        result = []
        queue = deque()
        visited = set()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            # do something
            result.append(node.val)
            if node.left and node.left not in visited:
                queue.append(node.left)
            if node.right and node.right not in visited:
                queue.append(node.right)
        return result

    def wfs(self):
        if self.root is None:
            return []
        result = []
        priority_queue = PriorityQueue()
        visited = set()
        priority_queue.put(self.root)

        while not priority_queue.empty():
            node = priority_queue.get()
            result.append(node.val)

            if node.left and node.left not in visited:
                priority_queue.put(node.left)
            if node.right and node.right not in visited:
                priority_queue.put(node.right)
        return result


# if __name__ == '__main__':
#     bst = BinarySearchTree()
#     bst.add_node(3)
#     bst.add_node(1)
#     bst.add_node(2)
#     bst.add_node(0)
#     bst.add_node(5)
#     bst.add_node(4)
#     bst.add_node(6)
#
#     tree_nodes = bst.print_tree()
#     print tree_nodes
#     print "*" * 20
#     print('DFS:')
#     print "*" * 20
#     print(bst.dfs())
#     print "*" * 20
#     print ('BFS:')
#     print "*" * 20
#     print(bst.bfs())
#     print("*" * 20)
#     print("heuristic Search: Weight First Search")
#     print("*" * 20)
#     print(bst.wfs())
