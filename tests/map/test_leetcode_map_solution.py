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
