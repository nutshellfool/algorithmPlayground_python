# -*- coding: utf-8 -*-


class Solution(object):

    def __init__(self):
        self.__DX = [0, 0, 1, -1]
        self.__DY = [1, -1, 0, 0]

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
