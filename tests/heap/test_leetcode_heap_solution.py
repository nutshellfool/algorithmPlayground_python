from unittest import TestCase

from src.heap.leetcode_heap_solution import Solution, KthLargest, MedianFinder


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

    def test_findKthLargest(self):
        input_list = [3, 2, 1, 5, 6, 4]
        kth_largest_element = self.solution.findKthLargest(input_list, 2)
        self.assertIsNotNone(kth_largest_element)
        self.assertEqual(5, kth_largest_element)

    def test_findKthLargest_none(self):
        kth_largest_element = self.solution.findKthLargest(None, 2)
        self.assertIsNone(kth_largest_element)

    def test_findKthLargest_k_zero(self):
        input_list = [3, 2, 1, 5, 6, 4]
        kth_largest_element = self.solution.findKthLargest(input_list, 0)
        self.assertIsNone(kth_largest_element)

    def test_findKthLargest_k_larger_than_length(self):
        input_list = [3, 2, 1, 5, 6, 4]
        kth_largest_element = self.solution.findKthLargest(input_list, 7)
        self.assertIsNone(kth_largest_element)

    def test_findKthLargest_instinct(self):
        input_list = [3, 2, 1, 5, 6, 4]
        kth_largest_element = self.solution.findKthLargest_instinct(input_list, 2)
        self.assertIsNotNone(kth_largest_element)
        self.assertEqual(5, kth_largest_element)

    def test_findKthLargest_instinct_none(self):
        kth_largest_element = self.solution.findKthLargest_instinct(None, 2)
        self.assertIsNone(kth_largest_element)

    def test_findKthLargest_instinct_k_zero(self):
        input_list = [3, 2, 1, 5, 6, 4]
        kth_largest_element = self.solution.findKthLargest_instinct(input_list, 0)
        self.assertIsNone(kth_largest_element)

    def test_findKthLargest_instinct_k_larger_than_length(self):
        input_list = [3, 2, 1, 5, 6, 4]
        kth_largest_element = self.solution.findKthLargest_instinct(input_list, 7)
        self.assertIsNone(kth_largest_element)

    def test_KthLargestInStream(self):
        arr = [4, 5, 8, 2]
        kth_largest_in_stream = KthLargest(3, arr)
        pop_value = kth_largest_in_stream.add(3)
        self.assertEqual(4, pop_value)
        pop_value = kth_largest_in_stream.add(5)
        self.assertEqual(5, pop_value)
        pop_value = kth_largest_in_stream.add(10)
        self.assertEqual(5, pop_value)
        pop_value = kth_largest_in_stream.add(9)
        self.assertEqual(8, pop_value)
        pop_value = kth_largest_in_stream.add(4)
        self.assertEqual(8, pop_value)

    def test_medianSlidingWindow(self):
        input_array = [1, 3, -1, -3, 5, 3, 6, 7]
        expect_array = [1, -1, -1, 3, 5, 6]
        median_sliding_window_array = self.solution.medianSlidingWindow(input_array, 3)
        self.assertIsNotNone(median_sliding_window_array)
        self.assertEqual(expect_array, median_sliding_window_array)

    def test_medianSlidingWindow_none(self):
        median_sliding_window_array = self.solution.medianSlidingWindow(None, 3)
        self.assertIsNone(median_sliding_window_array)

    def test_medianSlidingWindow_k_equals_1(self):
        input_array = [1, 3, -1, -3, 5, 3, 6, 7]
        median_sliding_window_array = self.solution.medianSlidingWindow(input_array, 1)
        self.assertIsNotNone(median_sliding_window_array)
        self.assertEqual(input_array, median_sliding_window_array)

    def test_medianSlidingWindow_instinct(self):
        input_array = [1, 3, -1, -3, 5, 3, 6, 7]
        expect_array = [1, -1, -1, 3, 5, 6]
        median_sliding_window_array = self.solution.medianSlidingWindow_instinct(input_array, 3)
        self.assertIsNotNone(median_sliding_window_array)
        self.assertEqual(expect_array, median_sliding_window_array)

    def test_medianSlidingWindow_instinct_float_median(self):
        input_array = [1, 4, 2, 3]
        expect_array = [2.5]
        median_sliding_window_array = self.solution.medianSlidingWindow_instinct(input_array, 4)
        self.assertIsNotNone(median_sliding_window_array)
        self.assertEqual(expect_array, median_sliding_window_array)

    def test_medianSlidingWindow_instinct_none(self):
        median_sliding_window_array = self.solution.medianSlidingWindow_instinct(None, 3)
        self.assertIsNone(median_sliding_window_array)

    def test_medianSlidingWindow_instinct_k_equals_1(self):
        input_array = [1, 3, -1, -3, 5, 3, 6, 7]
        median_sliding_window_array = self.solution.medianSlidingWindow_instinct(input_array, 1)
        self.assertIsNotNone(median_sliding_window_array)
        self.assertEqual(input_array, median_sliding_window_array)

    def test_medianFinder(self):
        finder = MedianFinder()
        finder.addNum(1)
        finder.addNum(2)
        _median = finder.findMedian()
        self.assertIsNotNone(_median)
        self.assertEqual(1.5, _median)
        finder.addNum(3)
        _median = finder.findMedian()
        self.assertIsNotNone(_median)
        self.assertEqual(2, _median)
