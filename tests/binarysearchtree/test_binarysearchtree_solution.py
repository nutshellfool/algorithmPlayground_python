from unittest import TestCase

from src.binarysearchtree.binarysearchtree_solution import BinarySearchTree, BinaryTreeNode


class TestBinarySearchTree(TestCase):
    def test_add_node(self):
        binary_search_tree = BinarySearchTree()
        binary_search_tree.add_node(3)
        self.assertIsNotNone(binary_search_tree.root)
        self.assertEqual(binary_search_tree.root.val, 3)

    def test__add_node_to_tree_root_node_case(self):
        binary_search_tree = BinarySearchTree()
        node = binary_search_tree._add_node_to_tree(None, 3)
        self.assertIsNotNone(node)
        self.assertEqual(node.val, 3)

    def test__add_node_to_tree_lt_root_node_case(self):
        binary_search_tree = BinarySearchTree()
        root = BinaryTreeNode(3)
        node = binary_search_tree._add_node_to_tree(root, 2)
        self.assertIsNotNone(node)
        self.assertEqual(node.val, 3)
        self.assertIsNotNone(node.left)
        self.assertEqual(node.left.val, 2)
        self.assertIsNone(node.right)

    def test__add_node_to_tree_gt_root_node_case(self):
        binary_search_tree = BinarySearchTree()
        root = BinaryTreeNode(3)
        node = binary_search_tree._add_node_to_tree(root, 4)
        self.assertIsNotNone(node)
        self.assertEqual(node.val, 3)
        self.assertIsNotNone(node.right)
        self.assertEqual(node.right.val, 4)
        self.assertIsNone(node.left)

    def test_print_tree(self):
        tree = self.construct_bst()
        nodes = tree.print_tree()
        self.assertIsNotNone(nodes)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes, [5, 3, 7])

    def test__inorder_traversal(self):
        tree = self.construct_bst()
        nodes = []
        tree._preorder_traversal(tree.root, nodes)
        self.assertIsNotNone(nodes)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes, [5, 3, 7])

    def test__inorder_traversal_none_root_case(self):
        tree = BinarySearchTree()
        nodes = []
        tree._preorder_traversal(tree.root, nodes)
        self.assertEqual(len(nodes), 0)
        self.assertEqual(nodes, [])

    def test_find_node(self):
        pass
        # self.fail()

    def test_delete_tree(self):
        pass
        # self.fail()

    def test_dfs(self):
        tree = self.construct_search_base_tree()
        nodes = tree.dfs()
        self.assertEqual(len(nodes), 7)
        self.assertEqual(nodes, [4, 6, 7, 5, 2, 3, 1])

    def test_bfs(self):
        tree = self.construct_search_base_tree()
        nodes = tree.bfs()
        self.assertEqual(len(nodes), 7)
        self.assertEqual(nodes, [4, 2, 6, 1, 3, 5, 7])

    def test_wfs(self):
        tree = self.construct_search_base_tree()
        nodes = tree.wfs()
        self.assertEqual(len(nodes), 7)
        self.assertEqual(nodes, [4, 6, 7, 5, 2, 3, 1])

    @staticmethod
    def construct_bst():
        tree = BinarySearchTree()
        tree.add_node(5)
        tree.add_node(3)
        tree.add_node(7)
        return tree

    @staticmethod
    def construct_search_base_tree():
        # for convenience construct a 3 level tree
        # actually a complete binary search tree
        tree = BinarySearchTree()
        tree.add_node(4)
        tree.add_node(2)
        tree.add_node(6)
        tree.add_node(1)
        tree.add_node(3)
        tree.add_node(5)
        tree.add_node(7)
        return tree
