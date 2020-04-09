from unittest import TestCase

from src.dynamicprogramming.leetcode_dynamicprogramming_solution import Solution


class TestLeetCodeDynamicProgrammingSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_fib(self):
        fib_num = self.solution.fib(4)
        self.assertEqual(3, fib_num)

    def test_fib_zero(self):
        fib_num = self.solution.fib(0)
        self.assertEqual(0, fib_num)

    def test_fib_negative(self):
        fib_num = self.solution.fib(-1)
        self.assertIsNone(fib_num)

    def test_fib_math_induction(self):
        fib_num = self.solution.fib_math_induction(4)
        self.assertEqual(3, fib_num)

    def test_fib_math_induction_zero(self):
        fib_num = self.solution.fib_math_induction(0)
        self.assertEqual(0, fib_num)

    def test_fib_math_induction_negative(self):
        fib_num = self.solution.fib_math_induction(-1)
        self.assertIsNone(fib_num)

    def test_climbStairs(self):
        steps = self.solution.climbStairs(3)
        self.assertEqual(3, steps)

    def test_climbStairs_zero(self):
        steps = self.solution.climbStairs(0)
        self.assertEqual(0, steps)

    def test_climbStairs_negative(self):
        steps = self.solution.climbStairs(-1)
        self.assertIsNone(steps)

    def test_climbStairs_math_induction(self):
        steps = self.solution.climbStairs_math_induction(3)
        self.assertEqual(3, steps)

    def test_climbStairs_math_induction_zero(self):
        steps = self.solution.climbStairs_math_induction(0)
        self.assertEqual(0, steps)

    def test_climbStairs_math_induction_negative(self):
        steps = self.solution.climbStairs_math_induction(-1)
        self.assertIsNone(steps)
