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
