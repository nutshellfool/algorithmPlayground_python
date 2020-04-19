from unittest import TestCase

from src.unionfind.unionfind_solution import UnionFind


class TestUnionFind(TestCase):
    def setUp(self):
        self.__union_find = UnionFind(5)

    def test_union(self):
        self.__union_find.union(0, 4)
        self.assertTrue(self.__union_find.connected(0, 4))

    def test_connected(self):
        self.__union_find.connected(0, 4)
        self.assertFalse(0, 4)
