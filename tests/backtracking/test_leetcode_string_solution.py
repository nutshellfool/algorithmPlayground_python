from unittest import TestCase

from src.backtracking.leetcode_string_solution import Solution


class TestLeetCodeStringSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_generateParenthesis(self):
        expected_list = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        result_list = self.solution.generateParenthesis(3)
        self.assertIsNotNone(result_list)
        self.assertEqual(set(expected_list), set(result_list))

    def test_generateParenthesis_n_zero(self):
        result_list = self.solution.generateParenthesis(0)
        self.assertIsNotNone(result_list)
        self.assertEqual(1, len(result_list))
        self.assertEqual("", result_list[0])

    def test_generateParenthesis_negative(self):
        result_list = self.solution.generateParenthesis(-3)
        self.assertIsNone(result_list)

    def test_generateParenthesis_instinct(self):
        expected_list = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        result_list = self.solution.generateParenthesis_instinct(3)
        self.assertIsNotNone(result_list)
        self.assertEqual(set(expected_list), set(result_list))

    def test_generateParenthesis_instinct_n_zero(self):
        result_list = self.solution.generateParenthesis_instinct(0)
        self.assertIsNotNone(result_list)
        self.assertEqual(1, len(result_list))
        self.assertEqual("", result_list[0])

    def test_generateParenthesis_instinct_negative(self):
        result_list = self.solution.generateParenthesis_instinct(-3)
        self.assertIsNone(result_list)
