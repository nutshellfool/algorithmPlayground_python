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
