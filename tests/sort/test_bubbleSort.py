from unittest import TestCase
from src.sort.bubblesort import BubbleSort


class TestBubbleSort(TestCase):
    def test_bubble_sort(self):
        bubble_sort = BubbleSort()
        ordered_list = bubble_sort.bubble_sort([3, 2, 1])
        self.assertEqual(ordered_list, [1, 2, 3])
