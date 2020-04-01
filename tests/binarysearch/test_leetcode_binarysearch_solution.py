from unittest import TestCase

from src.binarysearch.leetcode_binarysearch_solution import Solution


class TestLeetCodeBinarySearchSolution(TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_myPow(self):
        result = self.solution.myPow(2.0, 10)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(1024.0, result)

    def test_myPow1(self):
        result = self.solution.myPow(2.1, 3)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(9.26100, result)

    def test_myPow_n_negative(self):
        result = self.solution.myPow(2.0, -2)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(0.25000, result)

    def test_myPow_iteration(self):
        result = self.solution.myPow_iteration(2.0, 10)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(1024.0, result)

    def test_myPow_iteration1(self):
        result = self.solution.myPow_iteration(2.1, 3)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(9.26100, result)

    def test_myPow_iteration_n_negative(self):
        result = self.solution.myPow_iteration(2.0, -2)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(0.25000, result)

    def test_myPow_lazy(self):
        result = self.solution.myPow_lazy(2.0, 10)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(1024.0, result)

    def test_myPow_lazy1(self):
        result = self.solution.myPow_iteration(2.1, 3)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(9.26100, result)

    def test_myPow_lazy_n_negative(self):
        result = self.solution.myPow_iteration(2.0, -2)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(0.25000, result)

    def test_myPow_instinct(self):
        result = self.solution.myPow_instinct(2.0, 10)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(1024.0, result)

    def test_myPow_intinct1(self):
        result = self.solution.myPow_instinct(2.1, 3)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(9.26100, result)

    def test_myPow_instinct_n_negative(self):
        result = self.solution.myPow_instinct(2.0, -2)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(0.25000, result)

    def test_mySqrt(self):
        int_sqrt = self.solution.mySqrt(4)
        self.assertIsNotNone(int_sqrt)
        self.assertEqual(2, int_sqrt)

    def test_mySqrt1(self):
        int_sqrt = self.solution.mySqrt(10)
        self.assertIsNotNone(int_sqrt)
        self.assertEqual(3, int_sqrt)

    def test_mySqrt_negative(self):
        int_sqrt = self.solution.mySqrt(-1)
        self.assertIsNone(int_sqrt)

    def test_mySqrt_instinct(self):
        int_sqrt = self.solution.mySqrt_instinct(4)
        self.assertIsNotNone(int_sqrt)
        self.assertEqual(2, int_sqrt)

    def test_mySqrt_instinct1(self):
        int_sqrt = self.solution.mySqrt_instinct(10)
        self.assertIsNotNone(int_sqrt)
        self.assertEqual(3, int_sqrt)

    def test_mySqrt_instinct_negative(self):
        int_sqrt = self.solution.mySqrt_instinct(-1)
        self.assertIsNone(int_sqrt)

    def test_mySqrtx(self):
        _delta = 0.0000001
        int_sqrt = self.solution.mySqrtx(4, _delta)
        self.assertIsNotNone(int_sqrt)
        self.assertAlmostEqual(2.0, int_sqrt)

    def test_mySqrtx1(self):
        _delta = 0.0000001
        int_sqrt = self.solution.mySqrtx(10, _delta)
        self.assertIsNotNone(int_sqrt)
        self.assertAlmostEqual(3.1622776, int_sqrt, delta=_delta)

    def test_mySqrtx_negative(self):
        _delta = 0.0000001
        int_sqrt = self.solution.mySqrtx(-1, _delta)
        self.assertIsNone(int_sqrt)

    def test_mySqrtx_instinct(self):
        _delta = 0.0000001
        int_sqrt = self.solution.mySqrtx_instinct(4, _delta)
        self.assertIsNotNone(int_sqrt)
        self.assertAlmostEqual(2.0, int_sqrt)

    def test_mySqrtx_instinct1(self):
        _delta = 0.0000001
        int_sqrt = self.solution.mySqrtx_instinct(10, _delta)
        self.assertIsNotNone(int_sqrt)
        self.assertAlmostEqual(3.1622776, int_sqrt, delta=_delta)

    def test_mySqrtx_instinct_negative(self):
        _delta = 0.0000001
        int_sqrt = self.solution.mySqrtx_instinct(-1, _delta)
        self.assertIsNone(int_sqrt)

    def test_divide(self):
        result = self.solution.divide(12, 2)
        self.assertEqual(6, result)

    def test_divide_divisor_zero(self):
        result = self.solution.divide(12, 0)
        # self.assertEqual(-1, result)
        self.assertIsNone(result)

    def test_divide_instinct(self):
        result = self.solution.divide_instinct(12, 2)
        self.assertEqual(6, result)

    def test_divide_instinct_divisor_zero(self):
        result = self.solution.divide_instinct(12, 0)
        # self.assertEqual(-1, result)
        self.assertIsNone(result)
