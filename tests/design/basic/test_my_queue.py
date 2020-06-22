from unittest import TestCase

from src.design.basic.my_queue import MyQueue


class TestMyQueue(TestCase):

    def setUp(self):
        self.my_queue = MyQueue()

    def test_happy_case(self):
        self.my_queue.push(1)
        self.my_queue.push(2)
        _peeked_element = self.my_queue.peek()
        _poped_element = self.my_queue.pop()
        _is_empty = self.my_queue.empty()
        self.assertEqual(1, _peeked_element)
        self.assertEqual(1, _poped_element)
        self.assertFalse(_is_empty)
