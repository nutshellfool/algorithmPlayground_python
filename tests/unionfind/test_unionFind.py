from unittest import TestCase

from src.unionfind.unionfind_solution import UnionFind


class TestUnionFind(TestCase):
    def setUp(self):
        self._union_find = UnionFind(5)

    def test_union(self):
        self._union_find.union(0, 4)
        self.assertTrue(self._union_find.connected(0, 4))

    def test_connected(self):
        self._union_find.connected(0, 4)
        self.assertFalse(0, 4)

    def test_count(self):
        self.assertEqual(5, self._union_find.count)
        self._union_find.union(0, 4)
        self.assertEqual(4, self._union_find.count)
