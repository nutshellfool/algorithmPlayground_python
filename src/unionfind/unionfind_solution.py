# -*- coding: utf-8 -*-


class UnionFind(object):

    def __init__(self, n):
        self.__roots = [i for i in xrange(n)]

    def union(self, p, q):
        """

        Union operation for nodes

        Args:
            p: node p
            q: node q

        """
        __root_p = self.__find_root(p)
        __root_q = self.__find_root(q)
        self.__roots[__root_p] = __root_q

    def connected(self, p, q):
        """
        Is two node connected

        Args:
            p: node p
            q: node q

        Returns:
            is connected
        """
        return self.__find_root(p) == self.__find_root(q)

    def __find_root(self, i):
        root = i
        while root != self.__roots[root]:
            root = self.__roots[root]

        # Path compress optimization
        while i != self.__roots[i]:
            temp = self.__roots[i]
            self.__roots[i] = root
            i = temp

        return root
