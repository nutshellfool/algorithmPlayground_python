# -*- coding: utf-8 -*-


class Solution(object):
    @staticmethod
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        left_pointer, right_pointer = 0, len(height) - 1
        max_area = 0
        while left_pointer < right_pointer:
            max_area = max(max_area,
                           min(height[left_pointer], height[right_pointer]) * (
                                   right_pointer - left_pointer))
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_area

    @staticmethod
    def maxArea_brutal_force(height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))

        return max_area

    @staticmethod
    def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        unit_of_trapped = 0
        left_max, left, right_max, right = 0, 0, 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    unit_of_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    unit_of_trapped += right_max - height[right]
                right -= 1

        return unit_of_trapped

    @staticmethod
    def trap_brutal_force(height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        unit_of_trapped = 0
        left_max, right_max = 0, 0
        for i in range(1, len(height) - 1):

            for j in range(i):
                left_max = max(left_max, height[j])

            for k in range(i, len(height)):
                right_max = max(right_max, height[k])

            bucket_min = min(left_max, right_max)
            unit_of_trapped += bucket_min - height[i]

        return unit_of_trapped

    @staticmethod
    def trap_dynamic_programming(height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        unit_of_trapped = 0
        left_max, right_max = [0] * (len(height) + 1), [0] * (len(height) + 1)

        left_max[0], right_max[len(height) - 1] = height[0], height[
            len(height) - 1]
        for i in xrange(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        for i in xrange(len(height) - 1 - 1, 0, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in xrange(1, len(height) - 1):
            bucket_min = min(left_max[i], right_max[i])
            unit_of_trapped += bucket_min - height[i]
        return unit_of_trapped

    @staticmethod
    def sortColors(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # this is a Dutch national flag problem, algorithm by Edsger Dijkstra
        # https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        if not nums:
            return nums

        _pointer_front = _current = 0
        _pointer_end = len(nums) - 1

        while _current <= _pointer_end:
            if nums[_current] == 0:
                nums[_pointer_front], nums[_current] = nums[_current], nums[
                    _pointer_front]
                _current += 1
                _pointer_front += 1
            elif nums[_current] == 2:
                nums[_current], nums[_pointer_end] = nums[_pointer_end], nums[
                    _current]
                _pointer_end -= 1
            else:
                _current += 1

        return nums

    @staticmethod
    def sortColors_instinct(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        return sorted(nums)

    @staticmethod
    def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        last_none_zero_p = current = 0

        while current < len(nums):
            if nums[current] != 0:
                nums[last_none_zero_p], nums[current] = nums[current], nums[
                    last_none_zero_p]
                last_none_zero_p += 1
            current += 1

    @staticmethod
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        current, pointer = 0, 1
        while pointer < len(nums):
            if nums[pointer] != nums[current]:
                current += 1
                nums[current] = nums[pointer]
            pointer += 1

        return current + 1
