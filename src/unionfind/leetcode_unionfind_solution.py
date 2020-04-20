# -*- coding: utf-8 -*-


class GridUnionFind:
    def __init__(self, grid):
        row_len, col_len = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (row_len * col_len)
        self.rank = [0] * (row_len * col_len)
        for i in xrange(row_len):
            for j in xrange(col_len):
                if grid[i][j] == '1':
                    self.parent[i * col_len + j] = i * col_len + j
                    self.count += 1

    def find(self, i):
        root = i
        while self.parent[root] != root:
            root = self.parent[root]

        return root

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_x] = root_y
                self.rank[root_x] += 1
            self.count -= 1


class Solution(object):

    def __init__(self):
        self.__DX = [0, 0, 1, -1]
        self.__DY = [1, -1, 0, 0]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        _union_find = GridUnionFind(grid)
        _row_length, _column_length = len(grid), len(grid[0])

        for i in xrange(_row_length):
            for j in xrange(_column_length):
                if grid[i][j] == '0':
                    continue
                for k in xrange(4):
                    nr, nc = i + self.__DX[k], j + self.__DY[k]
                    if 0 <= nr < _row_length and 0 <= nc < _column_length and grid[nr][nc] == '1':
                        _union_find.union(i * _column_length + j, nr * _column_length + nc)

        return _union_find.count

    def numIslands_dfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        _row_length, _column_length = len(grid), len(grid[0])
        _visited = set()
        _num_islands = 0

        for i in xrange(_row_length):
            for j in xrange(_column_length):
                _num_islands += self._flood_fill_dfs(grid, _row_length, _column_length, i, j, _visited)

        return _num_islands

    def _flood_fill_dfs(self, grid, x_len, y_len, x, y, visited):
        if not self._is_valid(grid, x_len, y_len, x, y, visited):
            return 0

        visited.add((x, y))
        for k in xrange(len(self.__DX)):
            self._flood_fill_dfs(grid, x_len, y_len, x + self.__DX[k], y + self.__DY[k], visited)
        return 1

    def _is_valid(self, grid, x_len, y_len, x, y, visited):
        return 0 <= x < x_len and 0 <= y < y_len \
               and grid[x][y] == '1' and (x, y) not in visited
