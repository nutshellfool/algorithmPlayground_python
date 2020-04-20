# -*- coding: utf-8 -*-


class UnionFind(object):

    def __init__(self, n):
        self._roots = [i for i in xrange(n)]
        self._rank = [1 for _ in xrange(n)]
        self.count = n

    def union(self, p, q):
        """

        Union operation for nodes

        Args:
            p: node p
            q: node q

        """
        __root_p = self.__find_root(p)
        __root_q = self.__find_root(q)

        if __root_p != __root_q:
            if self._rank[__root_p] > self._rank[__root_q]:
                self._roots[__root_q] = __root_p
                self._rank[__root_p] += self._rank[__root_q]
            else:
                self._roots[__root_p] = __root_q
                self._rank[__root_q] += self._rank[__root_p]
            self.count -= 1

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
        while root != self._roots[root]:
            root = self._roots[root]

        # Path compress optimization
        while i != self._roots[i]:
            temp = self._roots[i]
            self._roots[i] = root
            i = temp

        return root
