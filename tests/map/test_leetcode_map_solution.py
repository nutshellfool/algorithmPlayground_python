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

    def test_threeSum(self):
        input_list = [-1, 0, 1, 2, -1, -4]
        expected_lists = [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
        result_lists = self.solution.threeSum(input_list)
        self.assertIsNotNone(result_lists)
        self.assertEqual(sorted(expected_lists), result_lists)

    def test_threeSum1(self):
        input_list = [0, 0, 0]
        expected_lists = [
            [0, 0, 0]
        ]
        result_lists = self.solution.threeSum(input_list)
        self.assertIsNotNone(result_lists)
        self.assertEqual(sorted(expected_lists), result_lists)

    def test_threeSum_none(self):
        result_list = self.solution.threeSum(None)
        self.assertIsNone(result_list)

    def test_threeSum_map(self):
        input_list = [-1, 0, 1, 2, -1, -4]
        expected_lists = [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
        result_lists = self.solution.threeSum_map(input_list)
        self.assertIsNotNone(result_lists)
        self.assertEqual(sorted(expected_lists), result_lists)

    def test_threeSum_map1(self):
        input_list = [0, 0, 0]
        expected_lists = [
            [0, 0, 0]
        ]
        result_lists = self.solution.threeSum_map(input_list)
        self.assertIsNotNone(result_lists)
        self.assertEqual(sorted(expected_lists), result_lists)

    def test_threeSum_map_none(self):
        result_list = self.solution.threeSum_map(None)
        self.assertIsNone(result_list)

    def test_threeSum_instinct(self):
        input_list = [-1, 0, 1, 2, -1, -4]
        expected_lists = [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
        result_lists = self.solution.threeSum_instinct(input_list)
        self.assertIsNotNone(result_lists)
        self.assertEqual(sorted(expected_lists), result_lists)

    def test_threeSum_instinct1(self):
        input_list = [0, 0, 0]
        expected_lists = [
            [0, 0, 0]
        ]
        result_lists = self.solution.threeSum_instinct(input_list)
        self.assertIsNotNone(result_lists)
        self.assertEqual(sorted(expected_lists), result_lists)

    def test_threeSum_instinct_none(self):
        result_list = self.solution.threeSum_instinct(None)
        self.assertIsNone(result_list)

    def test_fourSum(self):
        input_list = [1, 0, -1, 0, -2, 2]
        expected_list = [
            [-1, 0, 0, 1],
            [-2, -1, 1, 2],
            [-2, 0, 0, 2]
        ]
        result_list = self.solution.fourSum(input_list, 0)
        self.assertIsNotNone(result_list)
        self.assertEqual(sorted(expected_list), result_list)

    def test_fourSum1(self):
        input_list = [0, 0, 0, 0]
        expected_list = [
            [0, 0, 0, 0]
        ]
        result_list = self.solution.fourSum(input_list, 0)
        self.assertIsNotNone(result_list)
        self.assertEqual(sorted(expected_list), result_list)

    def test_fourSum_none(self):
        result_list = self.solution.fourSum(None, 0)
        self.assertIsNone(result_list)

    def test_twoSum2(self):
        input_list = [2, 7, 11, 15]
        expected_list = [1, 2]
        result_list = self.solution.twoSum2(input_list, 9)
        self.assertIsNotNone(result_list)
        self.assertEqual(sorted(expected_list), result_list)

    # this problem may have follow up case:
    #   the result may not unique
    #
    # def test_twoSum2_1(self):
    #     input_list = [2,7,7,15]
    #     expected_list = [[1, 2], [1, 3]]
    #     result_list = self.solution.twoSum2(input_list, 9)
    #     self.assertIsNotNone(result_list)
    #     self.assertEqual(sorted(expected_list), sorted(result_list))
    #
    # def test_twoSum2_2(self):
    #     input_list = [0, 0, 0]
    #     expected_list = [[1, 2], [1, 3]]
    #     result_list = self.solution.twoSum2(input_list, 0)
    #     self.assertIsNotNone(result_list)
    #     self.assertEqual(sorted(expected_list), sorted(result_list))

    def test_twoSum2_none(self):
        result_list = self.solution.twoSum2(None, 0)
        self.assertIsNone(result_list)

    def test_majorityElement(self):
        input_list = [3, 2, 3]
        majority = self.solution.majorityElement(input_list)
        self.assertIsNotNone(majority)
        self.assertEqual(3, majority)

    def test_majorityElement1(self):
        input_list = [2, 2, 1, 1, 1, 2, 2]
        majority = self.solution.majorityElement(input_list)
        self.assertIsNotNone(majority)
        self.assertEqual(2, majority)

    def test_majorityElement_none(self):
        majority = self.solution.majorityElement(None)
        self.assertIsNone(majority)

    def test_majorityElement_instinct(self):
        input_list = [3, 2, 3]
        majority = self.solution.majorityElement_instinct(input_list)
        self.assertIsNotNone(majority)
        self.assertEqual(3, majority)

    def test_majorityElement_instinct1(self):
        input_list = [2, 2, 1, 1, 1, 2, 2]
        majority = self.solution.majorityElement_instinct(input_list)
        self.assertIsNotNone(majority)
        self.assertEqual(2, majority)

    def test_majorityElement_instinct_none(self):
        majority = self.solution.majorityElement_instinct(None)
        self.assertIsNone(majority)
