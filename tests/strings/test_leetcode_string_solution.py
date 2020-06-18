from unittest import TestCase

from src.strings.leetcode_string_solution import Solution


class TestLeetCodeStringSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_strStr(self):
        _index = self.solution.strStr("hello", "ll")
        self.assertEqual(2, _index)

    def test_strStr1(self):
        _index = self.solution.strStr("aaaaa", "bba")
        self.assertEqual(-1, _index)

    def test_strStr2(self):
        _index = self.solution.strStr("aaaaa", "")
        self.assertEqual(0, _index)
