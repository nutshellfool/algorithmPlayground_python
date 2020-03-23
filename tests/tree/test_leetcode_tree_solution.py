from sys import maxint
from unittest import TestCase

from src.tree.leetcode_tree_solution import Solution, TreeNode


class TestLeetCodeTreeSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

        self.tree_alpha_root_node = TreeNode(2)
        self.tree_alpha_root_node.left = TreeNode(1)
        self.tree_alpha_root_node.right = TreeNode(3)

        self.tree_beta_root_node = TreeNode(5)
        self.tree_beta_root_node.left = TreeNode(1)
        self.tree_beta_root_node.right = TreeNode(4)
        self.tree_beta_root_node.right.left = TreeNode(3)
        self.tree_beta_root_node.right.right = TreeNode(6)

        self.tree_maxint_alpha_root_node = TreeNode(maxint - 1)
        self.tree_maxint_alpha_root_node.left = TreeNode(maxint - 2)
        self.tree_maxint_alpha_root_node.right = TreeNode(maxint)

        minint = - maxint - 1
        self.tree_minint_alpha_root_node = TreeNode(minint + 1)
        self.tree_minint_alpha_root_node.left = TreeNode(minint)
        self.tree_minint_alpha_root_node.right = TreeNode(minint + 2)

    def test_isValidBST(self):
        is_valid = self.solution.isValidBST(self.tree_alpha_root_node)
        self.assertIsNotNone(is_valid)
        self.assertTrue(is_valid)

    def test_isValidBST1(self):
        is_valid = self.solution.isValidBST(self.tree_beta_root_node)
        self.assertIsNotNone(is_valid)
        self.assertFalse(is_valid)

    def test_isValidBST_maxint(self):
        is_valid = self.solution.isValidBST(self.tree_maxint_alpha_root_node)
        self.assertIsNotNone(is_valid)
        self.assertTrue(is_valid)

    def test_isValidBST_minint(self):
        is_valid = self.solution.isValidBST(self.tree_minint_alpha_root_node)
        self.assertIsNotNone(is_valid)
        self.assertTrue(is_valid)

    # noinspection PyTypeChecker
    def test_isValidBST_none(self):
        is_valid = self.solution.isValidBST(None)
        self.assertTrue(is_valid)

    def test_isValidBST_instinct(self):
        is_valid = self.solution.isValidBST_instinct(self.tree_alpha_root_node)
        self.assertIsNotNone(is_valid)
        self.assertTrue(is_valid)

    def test_isValidBST_instinct1(self):
        is_valid = self.solution.isValidBST_instinct(self.tree_beta_root_node)
        self.assertIsNotNone(is_valid)
        self.assertFalse(is_valid)

    def test_isValidBST_instinct_maxint(self):
        is_valid = self.solution.isValidBST_instinct(self.tree_maxint_alpha_root_node)
        self.assertIsNotNone(is_valid)
        self.assertTrue(is_valid)

    def test_isValidBST_instinct_minint(self):
        is_valid = self.solution.isValidBST_instinct(self.tree_minint_alpha_root_node)
        self.assertIsNotNone(is_valid)
        self.assertTrue(is_valid)

    # noinspection PyTypeChecker
    def test_isValidBST_instinct_none(self):
        is_valid = self.solution.isValidBST_instinct(None)
        self.assertTrue(is_valid)

    def test_inorderTraversal(self):
        traversal_list = self.solution.inorderTraversal(self.tree_alpha_root_node)
        expected_list = [1, 2, 3]
        self.assertIsNotNone(traversal_list)
        self.assertEqual(expected_list, traversal_list)

    def test_inorderTraversal_iteration(self):
        traversal_list = self.solution.inorderTraversal_iteration(self.tree_alpha_root_node)
        expected_list = [1, 2, 3]
        self.assertIsNotNone(traversal_list)
        self.assertEqual(expected_list, traversal_list)

    def test_preorderTraversal(self):
        traversal_list = self.solution.preorderTraversal(self.tree_alpha_root_node)
        expected_list = [2, 1, 3]
        self.assertIsNotNone(traversal_list)
        self.assertEqual(expected_list, traversal_list)

    def test_preorderTraversal_iteration(self):
        traversal_list = self.solution.preorderTraversal_iteration(self.tree_alpha_root_node)
        expected_list = [2, 1, 3]
        self.assertIsNotNone(traversal_list)
        self.assertEqual(expected_list, traversal_list)

    def test_postorderTraversal(self):
        traversal_list = self.solution.postorderTraversal(self.tree_alpha_root_node)
        expected_list = [1, 3, 2]
        self.assertIsNotNone(traversal_list)
        self.assertEqual(expected_list, traversal_list)

    def test_postorderTraversal_iteration(self):
        traversal_list = self.solution.postorderTraversal_iteration(self.tree_alpha_root_node)
        expected_list = [1, 3, 2]
        self.assertIsNotNone(traversal_list)
        self.assertEqual(expected_list, traversal_list)

    def test_lowestCommonAncestor(self):
        node_root = TreeNode(3)
        node_root.left = TreeNode(5)
        node_root.left.left = TreeNode(6)
        node_root.left.right = TreeNode(2)
        node_root.left.right.left = TreeNode(7)
        node_root.left.right.right = TreeNode(4)
        node_root.right = TreeNode(1)
        node_root.right.left = TreeNode(0)
        node_root.right.right = TreeNode(8)

        lca = self.solution.lowestCommonAncestor(node_root, node_root.left, node_root.right)
        self.assertIsNotNone(lca)
        self.assertEqual(node_root, lca)
