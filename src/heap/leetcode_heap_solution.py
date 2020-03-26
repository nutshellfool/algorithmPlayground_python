# -*- coding: utf-8 -*-
from collections import deque


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
