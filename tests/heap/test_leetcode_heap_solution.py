from unittest import TestCase

from src.heap.leetcode_heap_solution import Solution


class TestLeetCodeHeapSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxSlidingWindow(self):
        input_list = [1, 3, -1, -3, 5, 3, 6, 7]
        expected_result = [3, 3, 5, 5, 6, 7]
        result = self.solution.maxSlidingWindow(input_list, 3)
        self.assertIsNotNone(result)
        self.assertEqual(expected_result, result)

    def test_maxSlidingWindow1(self):
        input_list = [1, 3, -1, -3, 5, 3, 6, 7]
        result = self.solution.maxSlidingWindow(input_list, 1)
        self.assertIsNotNone(result)
        self.assertEqual(input_list, result)

    def test_maxSlidingWindow2(self):
        input_list = [7, 2, 4]
        expected_result = [7, 4]
        result = self.solution.maxSlidingWindow(input_list, 2)
        self.assertIsNotNone(result)
        self.assertEqual(expected_result, result)

    def test_maxSlidingWindow_none(self):
        result = self.solution.maxSlidingWindow(None, 0)
        self.assertIsNone(result)

    def test_maxSlidingWindow_k_less_than0(self):
        result = self.solution.maxSlidingWindow([1, 2, 3], -1)
        self.assertIsNone(result)

    def test_maxSlidingWindow_instinct(self):
        input_list = [1, 3, -1, -3, 5, 3, 6, 7]
        expected_result = [3, 3, 5, 5, 6, 7]
        result = self.solution.maxSlidingWindow_instinct(input_list, 3)
        self.assertIsNotNone(result)
        self.assertEqual(expected_result, result)

    def test_maxSlidingWindow_instinct1(self):
        input_list = [1, 3, -1, -3, 5, 3, 6, 7]
        result = self.solution.maxSlidingWindow_instinct(input_list, 1)
        self.assertIsNotNone(result)
        self.assertEqual(input_list, result)

    def test_maxSlidingWindow_instinct2(self):
        input_list = [7, 2, 4]
        expected_result = [7, 4]
        result = self.solution.maxSlidingWindow_instinct(input_list, 2)
        self.assertIsNotNone(result)
        self.assertEqual(expected_result, result)

    def test_maxSlidingWindow_instinct_none(self):
        result = self.solution.maxSlidingWindow_instinct(None, 0)
        self.assertIsNone(result)

    def test_maxSlidingWindow_instinct_k_less_than0(self):
        result = self.solution.maxSlidingWindow_instinct([1, 2, 3], -1)
        self.assertIsNone(result)
