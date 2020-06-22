from Queue import Queue


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Queue()
        self.queue_out = Queue()
        self.top_element = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.put(x)
        self.top_element = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while self.queue.qsize() > 1:
            self.top_element = self.queue.get()
            self.queue_out.put(self.top_element)
        _poped = self.queue.get()
        self.queue, self.queue_out = self.queue_out, self.queue
        return _poped

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top_element

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue.qsize() == 0
