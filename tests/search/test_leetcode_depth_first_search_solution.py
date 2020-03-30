from unittest import TestCase

from src.search.leetcode_depth_first_search_solution import Solution
from src.tree.leetcode_tree_solution import TreeNode


class TestLeetCodeDepthFirstSearchSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.tree_root = TreeNode(3)
        self.tree_root.left = TreeNode(9)
        self.tree_root.right = TreeNode(20)
        self.tree_root.right.left = TreeNode(15)
        self.tree_root.right.right = TreeNode(7)

    def test_maxDepth(self):
        tree_depth = self.solution.maxDepth(self.tree_root)
        self.assertIsNotNone(tree_depth)
        self.assertEqual(3, tree_depth)

    def test_maxDepth_leaf_root(self):
        root_leaf = TreeNode(0)
        tree_depth = self.solution.maxDepth(root_leaf)
        self.assertEqual(1, tree_depth)

    def test_maxDepth_none(self):
        tree_depth = self.solution.maxDepth(None)
        self.assertEqual(0, tree_depth)

    def test_maxDepth_bfs(self):
        tree_depth = self.solution.maxDepth_bfs(self.tree_root)
        self.assertIsNotNone(tree_depth)
        self.assertEqual(3, tree_depth)

    def test_maxDepth_bfs_leaf_root(self):
        root_leaf = TreeNode(0)
        tree_depth = self.solution.maxDepth_bfs(root_leaf)
        self.assertEqual(1, tree_depth)

    def test_maxDepth_bfs_none(self):
        tree_depth = self.solution.maxDepth_bfs(None)
        self.assertEqual(0, tree_depth)

    def test_maxDepth_instinct(self):
        tree_depth = self.solution.maxDepth_instinct(self.tree_root)
        self.assertIsNotNone(tree_depth)
        self.assertEqual(3, tree_depth)

    def test_maxDepth_instinct_leaf_root(self):
        root_leaf = TreeNode(0)
        tree_depth = self.solution.maxDepth_instinct(root_leaf)
        self.assertEqual(1, tree_depth)

    def test_maxDepth_instinct_none(self):
        tree_depth = self.solution.maxDepth_instinct(None)
        self.assertEqual(0, tree_depth)
