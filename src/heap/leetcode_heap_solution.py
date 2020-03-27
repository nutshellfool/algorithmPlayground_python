# -*- coding: utf-8 -*-
from collections import deque

try:
    from Queue import PriorityQueue  # Version < 3.0
except ImportError:
    from queue import PriorityQueue


class PriorityQueueX(PriorityQueue):
    def peek(self):
        try:
            return self.queue[0]
        except IndexError:
            return None


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:
            return None
        result = []
        d = deque()

        for i, v in enumerate(nums):
            # kick off the small elements from the deque
            while d and nums[d[-1]] < v:
                d.pop()

            d.append(i)

            # remove the element that out of k range from deque
            if d[0] == i - k:
                d.popleft()
            if i + 1 >= k:
                result.append(nums[d[0]])

        return result

    def maxSlidingWindow_instinct(self, nums, k):
        """
        Time complexity :   $O(N * k)$
        Space complexity :  $O(N - k + 1)$
        """
        if not nums or k <= 0:
            return None

        result = []
        for i, v in enumerate(nums):
            if i <= len(nums) - k:
                result.append(max(nums[i:i + k]))
        return result

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k <= 0 or k > len(nums):
            return None

        q = PriorityQueue(k)
        for i, v in enumerate(nums):
            if i < k:
                q.put(v)
            else:
                # priorityQueue do not have peek method
                # so this implementation is so wired
                pq_min_value = q.get()
                q.put(v) if v > pq_min_value else q.put(pq_min_value)

        return q.get()

    def findKthLargest_instinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k <= 0 or k > len(nums):
            return None

        nums = sorted(nums, reverse=True)
        return nums[k - 1]


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.max_size = k
        self.q = PriorityQueueX(k)
        for i, v in enumerate(nums):
            self.add(v)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.max_size > self.q.qsize():
            self.q.put(val)
        else:
            if self.q.peek() < val:
                self.q.get()
                self.q.put(val)

        return self.q.peek()
