from unittest import TestCase
from src.sort.insertionsort import InsertionSort


class TestInsertionSort(TestCase):
    def test_insertion_sort(self):
        insertion_sort = InsertionSort()
        sort_result = insertion_sort.insertion_sort([3, 2, 1])
        self.assertEqual(sort_result, [1, 2, 3])
