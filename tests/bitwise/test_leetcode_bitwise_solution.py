from unittest import TestCase

from src.bitwise.leetcode_bitwise_solution import Solution


class TestLeetCodeBitwiseSolution(TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_hammingWeight(self):
        hamming_weight = self.solution.hammingWeight(2)
        self.assertIsNotNone(hamming_weight)
        self.assertEqual(1, hamming_weight)

    def test_hammingWeight3(self):
        hamming_weight = self.solution.hammingWeight(3)
        self.assertIsNotNone(hamming_weight)
        self.assertEqual(2, hamming_weight)

    def test_hammingWeight0(self):
        hamming_weight = self.solution.hammingWeight(0)
        self.assertEqual(0, hamming_weight)
        self.assertIsNotNone(hamming_weight)

    def test_hammingWeight_instinct(self):
        hamming_weight = self.solution.hammingWeight_instinct(2)
        self.assertIsNotNone(hamming_weight)
        self.assertEqual(1, hamming_weight)

    def test_hammingWeight_instinct3(self):
        hamming_weight = self.solution.hammingWeight_instinct(3)
        self.assertIsNotNone(hamming_weight)
        self.assertEqual(2, hamming_weight)

    def test_hammingWeight_instinct0(self):
        hamming_weight = self.solution.hammingWeight_instinct(0)
        self.assertEqual(0, hamming_weight)
        self.assertIsNotNone(hamming_weight)

    def test_isPowerof2(self):
        is_power_of2 = self.solution.isPowerOfTwo(4)
        self.assertTrue(is_power_of2)

    def test_isPowerof2_3(self):
        is_power_of2 = self.solution.isPowerOfTwo(3)
        self.assertFalse(is_power_of2)

    def test_isPowerof2_0(self):
        is_power_of2 = self.solution.isPowerOfTwo(0)
        self.assertFalse(is_power_of2)
