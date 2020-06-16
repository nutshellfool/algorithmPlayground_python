from unittest import TestCase

from src.backtracking.leetcode_backtracking_solution import Solution


class TestLeetCodeStringSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_generateParenthesis(self):
        expected_list = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        result_list = self.solution.generateParenthesis(3)
        self.assertIsNotNone(result_list)
        # self.assertEqual(set(expected_list), set(result_list))
        self.assertItemsEqual(expected_list, result_list)

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
        # self.assertEqual(set(expected_list), set(result_list))
        self.assertItemsEqual(expected_list, result_list)

    def test_generateParenthesis_instinct_n_zero(self):
        result_list = self.solution.generateParenthesis_instinct(0)
        self.assertIsNotNone(result_list)
        self.assertEqual(1, len(result_list))
        self.assertEqual("", result_list[0])

    def test_generateParenthesis_instinct_negative(self):
        result_list = self.solution.generateParenthesis_instinct(-3)
        self.assertIsNone(result_list)

    def test_combine(self):
        expected_list = [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]
        result_list = self.solution.combine(4, 2)
        self.assertIsNotNone(result_list)
        # self.assertEqual(set(expected_list), set(result_list))
        self.assertItemsEqual(expected_list, result_list)

    def test_combine1(self):
        expected_list = [
            [1],
            [2],
            [3],
            [4],
        ]
        result_list = self.solution.combine(4, 1)
        self.assertIsNotNone(result_list)
        # self.assertEqual(set(expected_list), set(result_list))
        self.assertItemsEqual(expected_list, result_list)

    def test_combine_negative_k(self):
        result_list = self.solution.combine(4, -1)
        self.assertIsNone(result_list)

    def test_combine_zero_k(self):
        result_list = self.solution.combine(4, 0)
        self.assertIsNotNone(result_list)
        self.assertEqual([[]], result_list)

    def test_combine_negative_n(self):
        result_list = self.solution.combine(-1, 1)
        self.assertIsNone(result_list)

    def test_combine_zero_n(self):
        result_list = self.solution.combine(0, 1)
        self.assertIsNotNone(result_list)
        self.assertEqual([[]], result_list)

    def test_combine_backtrace(self):
        expected_list = [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]
        result_list = self.solution.combine_backtrace(4, 2)
        self.assertIsNotNone(result_list)
        # self.assertEqual(set(expected_list), set(result_list))
        self.assertItemsEqual(expected_list, result_list)

    def test_combine_backtrace1(self):
        expected_list = [
            [1],
            [2],
            [3],
            [4],
        ]
        result_list = self.solution.combine_backtrace(4, 1)
        self.assertIsNotNone(result_list)
        # self.assertEqual(set(expected_list), set(result_list))
        self.assertItemsEqual(expected_list, result_list)

    def test_combine_backtrace_negative_k(self):
        result_list = self.solution.combine_backtrace(4, -1)
        self.assertIsNone(result_list)

    def test_combine_backtrace_zero_k(self):
        result_list = self.solution.combine_backtrace(4, 0)
        self.assertIsNotNone(result_list)
        self.assertEqual([[]], result_list)

    def test_combine_backtrace_negative_n(self):
        result_list = self.solution.combine_backtrace(-1, 1)
        self.assertIsNone(result_list)

    def test_combine_backtrace_zero_n(self):
        result_list = self.solution.combine_backtrace(0, 1)
        self.assertIsNotNone(result_list)
        self.assertEqual([[]], result_list)

    def test_combine_instinct(self):
        expected_list = [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]
        result_list = self.solution.combine_instinct(4, 2)
        self.assertIsNotNone(result_list)
        # self.assertEqual(set(expected_list), set(result_list))
        self.assertItemsEqual(expected_list, result_list)

    def test_combine_instinct1(self):
        expected_list = [
            [1],
            [2],
            [3],
            [4],
        ]
        result_list = self.solution.combine_instinct(4, 1)
        self.assertIsNotNone(result_list)
        # self.assertEqual(set(expected_list), set(result_list))
        self.assertItemsEqual(expected_list, result_list)

    def test_combine_instinct_negative_k(self):
        result_list = self.solution.combine_instinct(4, -1)
        self.assertIsNone(result_list)

    def test_combine_instinct_zero_k(self):
        result_list = self.solution.combine_instinct(4, 0)
        self.assertIsNotNone(result_list)
        self.assertEqual([[]], result_list)

    def test_combine_instinct_negative_n(self):
        result_list = self.solution.combine_instinct(-1, 1)
        self.assertIsNone(result_list)

    def test_combine_instinct_zero_n(self):
        result_list = self.solution.combine_instinct(0, 1)
        self.assertIsNotNone(result_list)
        self.assertEqual([[]], result_list)

    def test_subsets(self):
        expected = [
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]
        _subsets = self.solution.subsets([1, 2, 3])
        self.assertItemsEqual(expected, _subsets)

    def test_subsetsWithDup(self):
        expected = [
            [2],
            [1],
            [1, 2, 2],
            [2, 2],
            [1, 2],
            []
        ]

        _subsets_with_dup = self.solution.subsetsWithDup([1, 2, 2])
        self.assertItemsEqual(expected, _subsets_with_dup)

    def test_restoreIpAddresses_1(self):
        expected = ["255.255.11.135", "255.255.111.35"]
        _ip_addresses = self.solution.restoreIpAddresses('25525511135')
        self.assertItemsEqual(expected, _ip_addresses)

    def test_restoreIpAddresses_2(self):
        expected = ["0.0.0.0"]
        _ip_addresses = self.solution.restoreIpAddresses('0000')
        self.assertItemsEqual(expected, _ip_addresses)

    def test_restoreIpAddresses_length_oversize(self):
        _ip_addresses = self.solution.restoreIpAddresses('1111111111111')
        self.assertEqual([], _ip_addresses)
