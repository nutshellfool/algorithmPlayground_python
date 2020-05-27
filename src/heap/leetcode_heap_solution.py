# -*- coding: utf-8 -*-
import heapq
import itertools
from collections import Counter
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

    def remove(self, element):
        self.queue.remove(element)
        heapq.heapify(self.queue)


def _array_median(_nums):
    _nums = sorted(_nums)
    is_odd = len(_nums) & 1
    _median = _nums[(len(_nums)) // 2] if is_odd else (_nums[len(_nums) // 2] + _nums[
        (len(_nums) - 1) // 2]) / 2.0
    return _median


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

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """

        def balancefy(_min_heap, _max_heap):
            while _max_heap.qsize() < _min_heap.qsize():
                _max_heap.put(-_min_heap.get())

            while _min_heap.qsize() < _max_heap.qsize() - 1:
                _min_heap.put(-_max_heap.get())

        if not nums or k <= 0:
            return None
        if k == 1:
            return nums
        if k == len(nums):
            return [_array_median(nums)]

        _length = len(nums)
        min_heap = PriorityQueueX(_length / 2)
        max_heap = PriorityQueueX(_length / 2)
        result = []

        for i, v in enumerate(nums):
            # element get into two PriorityQueue
            if max_heap.qsize() == 0 or v <= max_heap.peek():
                max_heap.put(-1 * v)
            else:
                min_heap.put(v)
            balancefy(min_heap, max_heap)

            # elements get out of the two PriorityQueue
            if i >= k:
                if -max_heap.peek() < nums[i - k]:
                    min_heap.remove(nums[i - k])
                else:
                    max_heap.remove(-nums[i - k])
            balancefy(min_heap, max_heap)

            if i >= k - 1:
                if k & 1:
                    result.append(-max_heap.peek())
                else:
                    result.append((-max_heap.peek() + min_heap.peek()) / 2.0)

        return result

    def medianSlidingWindow_instinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if not nums or k <= 0:
            return None
        if k == 1:
            return nums
        if k == len(nums):
            return [_array_median(nums)]

        result = []
        for i in xrange(len(nums) - k + 1):
            # median = 0
            # for j in xrange(i, i + k):
            median = _array_median(nums[i:i + k])
            result.append(median)

        return result

    def topKFrequent(self, nums, k):
        if not nums or k <= 0 or k > len(nums):
            return []
        bucket = [[] for _ in nums]
        for num, freq in Counter(nums).items():
            bucket[len(nums) - freq].append(num)
        return list(itertools.chain(*bucket))[:k]

    def topKFrequent_instinct(self, nums, k):
        if not nums or k <= 0 or k > len(nums):
            return []
        _counter_dict = Counter(nums)
        _top_k_tuple = _counter_dict.most_common(k)
        result = list(map(lambda a: a[0], _top_k_tuple))
        # result = []
        # for item_tuple in _top_k_tuple:
        #     result.append(item_tuple[0])
        return result


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


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = PriorityQueueX()
        self.max_heap = PriorityQueueX()
        self.queue_size = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.max_heap.qsize() == 0 or num < -self.max_heap.peek():
            self.max_heap.put(-num)
        else:
            self.min_heap.put(num)
        self._balancefy(self.max_heap, self.min_heap)
        self.queue_size += 1

    def findMedian(self):
        """
        :rtype: float
        """
        return -self.max_heap.peek() if self.queue_size & 1 else (-self.max_heap.peek() + self.min_heap.peek()) / 2.0

    def _balancefy(self, _max_heap, _min_heap):
        while _min_heap.qsize() > _max_heap.qsize():
            _max_heap.put(-_min_heap.get())
        while _max_heap.qsize() - 1 > _min_heap.qsize():
            _min_heap.put(-_max_heap.get())
