from unittest import TestCase

from src.arrays.leetcode_arrays_solution import Solution


class TestArrayLeetCodeSolution(TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_maxArea(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        max_area = self.solution.maxArea(height)
        self.assertIsNotNone(max_area)
        self.assertEqual(49, max_area)

    def test_maxArea_none_params(self):
        max_area = self.solution.maxArea(None)
        self.assertIsNotNone(max_area)
        self.assertEqual(0, max_area)

    def test_maxArea_params_length_less_than_3(self):
        max_area = self.solution.maxArea([1, 2])
        self.assertIsNotNone(max_area)
        self.assertEqual(0, max_area)

    def test_maxArea_params_length_equals_3(self):
        max_area = self.solution.maxArea([1, 1, 1])
        self.assertIsNotNone(max_area)
        self.assertEqual(2, max_area)

    def test_maxArea_brutal_force(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        max_area = self.solution.maxArea_brutal_force(height)
        self.assertIsNotNone(max_area)
        self.assertEqual(49, max_area)

    def test_maxArea_brutal_force_none_params(self):
        max_area = self.solution.maxArea_brutal_force(None)
        self.assertIsNotNone(max_area)
        self.assertEqual(0, max_area)

    def test_maxArea_brutal_force_params_length_less_than_3(self):
        max_area = self.solution.maxArea_brutal_force([1, 2])
        self.assertIsNotNone(max_area)
        self.assertEqual(0, max_area)

    def test_maxArea_brutal_force_params_length_equals_3(self):
        max_area = self.solution.maxArea_brutal_force([1, 1, 1])
        self.assertIsNotNone(max_area)
        self.assertEqual(2, max_area)
