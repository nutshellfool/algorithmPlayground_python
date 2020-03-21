from unittest import TestCase

from src.stack.leetcode_stack_solution import Solution


class TestLeetCodeStackSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isValid(self):
        input_string = '()'
        is_valid = self.solution.isValid(input_string)
        self.assertTrue(is_valid)

    def test_isValid_nested_valid(self):
        input_string = '([])[]{}'
        is_valid = self.solution.isValid(input_string)
        self.assertTrue(is_valid)

    def test_isValid_invalid_case(self):
        input_string = '(]'
        is_valid = self.solution.isValid(input_string)
        self.assertFalse(is_valid)

    def test_isValid_none_param(self):
        is_valid = self.solution.isValid(None)
        self.assertFalse(is_valid)

    def test_isValid_empty_param(self):
        is_valid = self.solution.isValid('')
        self.assertFalse(is_valid)

    def test_isValid_instinct(self):
        input_string = '()'
        is_valid = self.solution.is_valid_instinct(input_string)
        self.assertTrue(is_valid)

    def test_isValid_instinct_nested_valid(self):
        input_string = '([])[]{}'
        is_valid = self.solution.is_valid_instinct(input_string)
        self.assertTrue(is_valid)

    def test_isValid_instinct_invalid_case(self):
        input_string = '(]'
        is_valid = self.solution.is_valid_instinct(input_string)
        self.assertFalse(is_valid)

    def test_isValid_instinct_none_param(self):
        is_valid = self.solution.is_valid_instinct(None)
        self.assertFalse(is_valid)

    def test_isValid_instinct_empty_param(self):
        is_valid = self.solution.is_valid_instinct('')
        self.assertFalse(is_valid)
