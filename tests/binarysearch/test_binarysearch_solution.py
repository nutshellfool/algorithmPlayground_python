from unittest import TestCase

from src.binarysearch.binarysearch_solution import Solution


class TestBinarySearchSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _positon = self.solution.search(array, 4)
        self.assertEqual(3, _positon)

    def test_search_front(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search(array, 1)
        self.assertEqual(0, _position)

    def test_search_end(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search(array, 7)
        self.assertEqual(6, _position)

    def test_search_not_exist(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search(array, 10)
        self.assertEqual(-1, _position)

    def test_search_lower_bound(self):
        array = [1, 2, 3, 4, 5, 6, 6, 6, 7]
        _positon = self.solution.search_lower_bound(array, 6)
        self.assertEqual(5, _positon)

    def test_search_lower_bound_front(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_lower_bound(array, 1)
        self.assertEqual(0, _position)

    def test_search_lower_bound_end(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_lower_bound(array, 7)
        self.assertEqual(6, _position)

    def test_search_lower_bound_not_exist(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_lower_bound(array, 10)
        self.assertEqual(-1, _position)

    def test_search_higher_bound(self):
        array = [1, 2, 3, 4, 5, 6, 6, 6, 7]
        _positon = self.solution.search_higher_bound(array, 6)
        self.assertEqual(7, _positon)

    def test_search_higher_bound_front(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_higher_bound(array, 1)
        self.assertEqual(0, _position)

    def test_search_higher_bound_end(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_higher_bound(array, 7)
        self.assertEqual(6, _position)

    def test_search_higher_bound_not_exist(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_higher_bound(array, 10)
        self.assertEqual(-1, _position)

    def test_search_lower_bound_below(self):
        array = [1, 2, 3, 4, 5, 7]
        _positon = self.solution.search_lower_bound_below(array, 6)
        self.assertEqual(4, _positon)

    def test_search_lower_bound_below_front(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_lower_bound_below(array, 1)
        self.assertEqual(0, _position)

    def test_search_lower_bound_below_end(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_lower_bound_below(array, 7)
        self.assertEqual(6, _position)

    def test_search_lower_bound_below_not_exist(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_lower_bound_below(array, 10)
        self.assertEqual(6, _position)

    def test_search_lower_bound_below_not_exist1(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_lower_bound_below(array, 0)
        self.assertEqual(-1, _position)

    def test_search_higher_bound_over(self):
        array = [1, 2, 3, 4, 5, 7]
        _positon = self.solution.search_higher_bound_over(array, 6)
        self.assertEqual(5, _positon)

    def test_search_higher_bound_over_front(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_higher_bound_over(array, 1)
        self.assertEqual(0, _position)

    def test_search_higher_bound_over_end(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_higher_bound_over(array, 7)
        self.assertEqual(6, _position)

    def test_search_higher_bound_over_not_exist(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_higher_bound_over(array, 10)
        self.assertEqual(-1, _position)

    def test_search_higher_bound_over_not_exist1(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        _position = self.solution.search_higher_bound_over(array, 0)
        self.assertEqual(0, _position)
