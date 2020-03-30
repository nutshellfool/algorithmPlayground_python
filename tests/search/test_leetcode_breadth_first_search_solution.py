from unittest import TestCase

from src.search.leetcode_breadth_first_search_solution import Solution
from src.tree.leetcode_tree_solution import TreeNode


class TestLeetCodeBreadthFirstSearchSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.tree_root = TreeNode(3)
        self.tree_root.left = TreeNode(9)
        self.tree_root.right = TreeNode(20)
        self.tree_root.right.left = TreeNode(15)
        self.tree_root.right.right = TreeNode(7)

    def test_minDepth(self):
        min_depth = self.solution.minDepth(self.tree_root)
        self.assertIsNotNone(min_depth)
        self.assertEqual(2, min_depth)

    def test_minDepth_leaf_root(self):
        leaf_root = TreeNode(1)
        min_depth = self.solution.minDepth(leaf_root)
        self.assertIsNotNone(min_depth)
        self.assertEqual(1, min_depth)

    def test_minDepth_none(self):
        min_depth = self.solution.minDepth(None)
        self.assertIsNotNone(min_depth)
        self.assertEqual(0, min_depth)

    def test_minDepth_dfs(self):
        min_depth = self.solution.minDepth_dfs(self.tree_root)
        self.assertIsNotNone(min_depth)
        self.assertEqual(2, min_depth)

    def test_minDepth_dfs_leaf_root(self):
        leaf_root = TreeNode(1)
        min_depth = self.solution.minDepth_dfs(leaf_root)
        self.assertIsNotNone(min_depth)
        self.assertEqual(1, min_depth)

    def test_minDepth_dfs_none(self):
        min_depth = self.solution.minDepth_dfs(None)
        self.assertIsNotNone(min_depth)
        self.assertEqual(0, min_depth)
