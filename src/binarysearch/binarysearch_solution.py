# -*- coding: utf-8 -*-


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search_lower_bound(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                else:
                    right = mid - 1

        return -1

    def search_higher_bound(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                else:
                    left = mid + 1

        return -1

    def search_lower_bound_below(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] > target:
                right = mid - 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid
                else:
                    left = mid + 1

        return -1

    def search_higher_bound_over(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            else:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1

        return -1
