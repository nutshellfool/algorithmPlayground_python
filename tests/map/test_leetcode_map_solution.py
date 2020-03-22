from unittest import TestCase

from src.map.leetcode_map_solution import Solution


class TestLeetCodeMapSolution(TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_isAnagram(self):
        s = "anagram"
        t = "nagaram"
        is_anagram = self.solution.isAnagram(s, t)
        self.assertTrue(is_anagram)

    def test_isAnagram_invalid(self):
        s = "rat"
        t = "cat"
        is_anagram = self.solution.isAnagram(s, t)
        self.assertFalse(is_anagram)

    def test_isAnagram_invalid1(self):
        s = "cook"
        t = "cok"
        is_anagram = self.solution.isAnagram(s, t)
        self.assertFalse(is_anagram)

    def test_isAnagram_none_params(self):
        is_anagram = self.solution.isAnagram(None, None)
        self.assertTrue(is_anagram)

    def test_twoSum(self):
        result_list = self.solution.twoSum([2, 7, 11, 15], 9)
        self.assertIsNotNone(result_list)
        self.assertEqual([0, 1], result_list)

    def test_twoSum_none(self):
        result_list = self.solution.twoSum(None, 2)
        self.assertIsNone(result_list)

    def test_twoSum_instinct(self):
        result_list = self.solution.twoSum_instinct([2, 7, 11, 15], 9)
        self.assertIsNotNone(result_list)
        self.assertEqual([0, 1], result_list)

    def test_twoSum_none_instinct(self):
        result_list = self.solution.twoSum_instinct(None, 2)
        self.assertIsNone(result_list)

    def test_threeSum(self):
        input_list = [-1, 0, 1, 2, -1, -4]
        expected_lists = [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
        result_lists = self.solution.threeSum(input_list)
        self.assertIsNotNone(result_lists)
        self.assertEqual(sorted(expected_lists), result_lists)

    def test_threeSum_none(self):
        result_list = self.solution.threeSum(None)
        self.assertIsNone(result_list)

    def test_threeSum_map(self):
        input_list = [-1, 0, 1, 2, -1, -4]
        expected_lists = [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
        result_lists = self.solution.threeSum_map(input_list)
        self.assertIsNotNone(result_lists)
        self.assertEqual(sorted(expected_lists), result_lists)

    def test_threeSum_map_none(self):
        result_list = self.solution.threeSum_map(None)
        self.assertIsNone(result_list)

    def test_threeSum_instinct(self):
        input_list = [-1, 0, 1, 2, -1, -4]
        expected_lists = [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
        result_lists = self.solution.threeSum_instinct(input_list)
        self.assertIsNotNone(result_lists)
        self.assertEqual(sorted(expected_lists), result_lists)

    def test_threeSum_instinct_none(self):
        result_list = self.solution.threeSum_instinct(None)
        self.assertIsNone(result_list)
