from unittest import TestCase

from src.design.basic.my_stack import MyStack


class TestMyStack(TestCase):
    def setUp(self):
        self.my_stack = MyStack()

    def test_happy_case(self):
        self.my_stack.push(1)
        self.my_stack.push(2)
        _top_element = self.my_stack.top()
        _poped = self.my_stack.pop()
        _empty = self.my_stack.empty()
        self.assertEqual(2, _top_element)
        self.assertEqual(2, _poped)
        self.assertFalse(_empty)
