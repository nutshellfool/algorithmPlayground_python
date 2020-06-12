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

    def test_trap_brutal_force(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        unit_of_trapped = self.solution.trap_brutal_force(height)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(6, unit_of_trapped)

    def test_trap_brutal_force_none_params(self):
        unit_of_trapped = self.solution.trap_brutal_force(None)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(0, unit_of_trapped)

    def test_trap_brutal_force_empty_params(self):
        unit_of_trapped = self.solution.trap_brutal_force([])
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(0, unit_of_trapped)

    def test_trap_brutal_force_params_length_less_than_3(self):
        height = [2, 1]
        unit_of_trapped = self.solution.trap_brutal_force(height)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(0, unit_of_trapped)

    def test_trap_brutal_force_params_length_equals_3(self):
        height = [2, 1, 2]
        unit_of_trapped = self.solution.trap_brutal_force(height)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(1, unit_of_trapped)

    def test_trap(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        unit_of_trapped = self.solution.trap(height)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(6, unit_of_trapped)

    def test_trap_none_params(self):
        unit_of_trapped = self.solution.trap(None)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(0, unit_of_trapped)

    def test_trap_empty_params(self):
        unit_of_trapped = self.solution.trap([])
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(0, unit_of_trapped)

    def test_trap_params_length_less_than_3(self):
        height = [2, 1]
        unit_of_trapped = self.solution.trap(height)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(0, unit_of_trapped)

    def test_trap_params_length_equals_3(self):
        height = [2, 1, 2]
        unit_of_trapped = self.solution.trap(height)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(1, unit_of_trapped)

    def test_trap_dynamic_programming(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        unit_of_trapped = self.solution.trap_dynamic_programming(height)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(6, unit_of_trapped)

    def test_trap_dynamic_programming_none_params(self):
        unit_of_trapped = self.solution.trap_dynamic_programming(None)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(0, unit_of_trapped)

    def test_trap_dynamic_programming_empty_params(self):
        unit_of_trapped = self.solution.trap_dynamic_programming([])
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(0, unit_of_trapped)

    def test_trap_dynamic_programming_params_length_less_than_3(self):
        height = [2, 1]
        unit_of_trapped = self.solution.trap_dynamic_programming(height)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(0, unit_of_trapped)

    def test_trap_dynamic_programming_params_length_equals_3(self):
        height = [2, 1, 2]
        unit_of_trapped = self.solution.trap_dynamic_programming(height)
        self.assertIsNotNone(unit_of_trapped)
        self.assertEqual(1, unit_of_trapped)

    def test_sortColors(self):
        _color_array = [2, 0, 2, 1, 1, 0]
        _sorted_array = self.solution.sortColors(_color_array)
        self.assertIsNotNone(_sorted_array)
        self.assertEqual(6, len(_sorted_array))
        self.assertEqual([0, 0, 1, 1, 2, 2], _sorted_array)

    def test_sortColors_None(self):
        _sorted_array = self.solution.sortColors(None)
        self.assertIsNone(_sorted_array)

    def test_sortColors_empty(self):
        _sorted_array = self.solution.sortColors([])
        self.assertIsNotNone(_sorted_array)
        self.assertEqual(0, len(_sorted_array))

    def test_sortColors_instinct(self):
        _color_array = [2, 0, 2, 1, 1, 0]
        _sorted_array = self.solution.sortColors_instinct(_color_array)
        self.assertIsNotNone(_sorted_array)
        self.assertEqual(6, len(_sorted_array))
        self.assertEqual([0, 0, 1, 1, 2, 2], _sorted_array)

    def test_sortColors_instinct_None(self):
        _sorted_array = self.solution.sortColors_instinct(None)
        self.assertIsNone(_sorted_array)

    def test_sortColors_instinct_empty(self):
        _sorted_array = self.solution.sortColors_instinct([])
        self.assertIsNotNone(_sorted_array)
        self.assertEqual(0, len(_sorted_array))

    def test_moveZeroes(self):
        _array = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(_array)
        self.assertIsNotNone(_array)
        self.assertEqual([1, 3, 12, 0, 0], _array)

    def test_moveZeroes1(self):
        _array = [0, 3, 0, 1, 12]
        self.solution.moveZeroes(_array)
        self.assertIsNotNone(_array)
        self.assertEqual([3, 1, 12, 0, 0], _array)

    def test_removeDuplicates(self):
        _array = [1, 1, 2]
        size = self.solution.removeDuplicates(_array)
        self.assertIsNotNone(_array)
        self.assertEqual(2, size)

    def test_removeDuplicates1(self):
        _array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        size = self.solution.removeDuplicates(_array)
        self.assertIsNotNone(_array)
        self.assertEqual(5, size)

    def test_maxEnvelopes(self):
        _envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
        _max_envelopes = self.solution.maxEnvelopes(_envelopes)
        self.assertEqual(3, _max_envelopes)

    def test_maxEnvelopes1(self):
        _envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
        _max_envelopes = self.solution.maxEnvelopes(_envelopes)
        self.assertEqual(4, _max_envelopes)

    def test_merge(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        _merged_interval = self.solution.merge(intervals)
        self.assertEqual(expected, _merged_interval)

    def test_merge1(self):
        intervals = [[1, 4], [4, 6]]
        expected = [[1, 6]]
        _merged_interval = self.solution.merge(intervals)
        self.assertEqual(expected, _merged_interval)

    def test_merge_none(self):
        _merged = self.solution.merge(None)
        self.assertIsNone(_merged)

    def test_merge_empty(self):
        _merged = self.solution.merge([])
        self.assertIsNone(_merged)
