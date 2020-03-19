from unittest import TestCase

from src.linkedlist.singlelinkedlist_solution import SingleLinkedList


class TestSingleLinkedList(TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSingleLinkedList, self).__init__(*args, **kwargs)
        self.linked_list = None

    def setUp(self):
        self.linked_list = SingleLinkedList()
        self.linked_list.append_node_to_tail(1)

    def tearDown(self):
        self.linked_list = None

    def test_append_node_to_tail(self):
        nodes = self.linked_list.traversal_list()
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], 1)

    def test_find_node(self):
        node = self.linked_list.find_node(1)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 1)

    def test_delete_node(self):
        self.linked_list.delete_node(1)
        nodes = self.linked_list.traversal_list()
        self.assertEqual(len(nodes), 0)

    def test_traversal_list(self):
        nodes = self.linked_list.traversal_list()
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], 1)

    def test_clear_list(self):
        nodes = self.linked_list.traversal_list()
        self.assertEqual(len(nodes), 1)
        self.linked_list.clear_list()
        nodes = self.linked_list.traversal_list()
        self.assertIsNone(nodes)
