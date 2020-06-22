from collections import deque


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()
        self.stack_out = deque()
        self.front_element = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.front_element = x
        while len(self.stack) != 0:
            self.stack_out.append(self.stack.pop())

        self.stack_out.append(x)

        while len(self.stack_out) != 0:
            self.stack.append(self.stack_out.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        _poped_element = self.stack.pop()
        if len(self.stack) != 0:
            self.front_element = self.stack[-1]
        return _poped_element

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.front_element

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0
