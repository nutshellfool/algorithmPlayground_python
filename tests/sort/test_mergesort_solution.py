from unittest import TestCase

from src.sort.mergesort_solution import MergeSort


class TestMergeSort(TestCase):
    def test_merge_sort(self):
        merge_sort = MergeSort()
        merge_result = merge_sort.merge_sort([3, 2, 1])
        self.assertEqual(merge_result, [1, 2, 3])
