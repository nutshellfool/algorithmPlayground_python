from unittest import TestCase

from src.unionfind.leetcode_unionfind_solution import Solution


class TestLeetCodeUnionFindSolution(TestCase):
    def setUp(self):
        self.__solution = Solution()

    def test_numIslands(self):
        grid = [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]
        num_island = self.__solution.numIslands(grid)
        self.assertEqual(1, num_island)

    def test_numIslands1(self):
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
        num_island = self.__solution.numIslands(grid)
        self.assertEqual(3, num_island)

    def test_numIslands_dfs(self):
        grid = [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]
        num_island = self.__solution.numIslands_dfs(grid)
        self.assertEqual(1, num_island)

    def test_numIslands_dfs1(self):
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
        num_island = self.__solution.numIslands_dfs(grid)
        self.assertEqual(3, num_island)

    def test_findCircleNum(self):
        matrix = [[1, 1, 0],
                  [1, 1, 0],
                  [0, 0, 1]]
        number_of_circles = self.__solution.findCircleNum(matrix)
        self.assertEqual(2, number_of_circles)

    def test_findCircleNum1(self):
        matrix = [[1, 1, 0],
                  [1, 1, 1],
                  [0, 1, 1]]
        number_of_circles = self.__solution.findCircleNum(matrix)
        self.assertEqual(1, number_of_circles)

    def test_findCircleNum2(self):
        matrix = [[1, 0, 0, 1],
                  [0, 1, 1, 0],
                  [0, 1, 1, 1],
                  [1, 0, 1, 1]]
        number_of_circles = self.__solution.findCircleNum(matrix)
        self.assertEqual(1, number_of_circles)
