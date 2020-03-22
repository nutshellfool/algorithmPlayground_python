# -*- coding: utf-8 -*-


class Solution(object):
    def isAnagram(self, s, t):
        if not s and not t:
            return True
        if (not s and t) or (s and not t):
            return False
        map_s = {}
        for i, char in enumerate(s):
            map_s[char] = map_s.get(char, 0) + 1
        map_t = {}
        for i, char in enumerate(t):
            map_t[char] = map_t.get(char, 0) + 1
        return map_s == map_t

    def isAnagram_instinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        if (not s and t) or (s and not t):
            return False

        map_s = {}
        for i, v in enumerate(s):
            if v in map_s:
                map_s[v] = map_s[v] + 1
            else:
                map_s[v] = 0
        map_t = {}
        for i, v in enumerate(t):
            if v in map_t:
                map_t[v] = map_t[v] + 1
            else:
                map_t[v] = 0

        return map_t == map_s

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None
        map_v_index = {}
        for i in xrange(len(nums)):
            if map_v_index.get(target - nums[i]) is not None:
                return [map_v_index.get(target - nums[i]), i]
            else:
                map_v_index[nums[i]] = i
        return None

    def twoSum_instinct(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None

        for i in xrange(len(nums)):
            for j in xrange(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        result_list = []
        nums = sorted(nums)

        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    result_list.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result_list

    def threeSum_map(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        result_list = []
        map_value_indices = dict()
        nums = sorted(nums)
        for i, v in enumerate(nums):
            map_value_indices[v] = i

        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i, len(nums)):
                if j > 0 and nums[j] == nums[j - 1]:
                    continue
                if map_value_indices.get(0 - nums[i] - nums[j]) is not None:
                    index = map_value_indices[0 - nums[i] - nums[j]]
                    if index != i and index != j \
                            and nums[i] <= nums[j] \
                            and nums[i] <= (0 - nums[i] - nums[j]) \
                            and nums[j] <= (0 - nums[i] - nums[j]):
                        result_list.append([nums[i], nums[j], -nums[i] - nums[j]])

        return result_list

    def threeSum_instinct(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        nums = sorted(nums)
        result_list_set = set()
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                for k in xrange(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result_list_set.add((nums[i], nums[j], nums[k]))

        return list(map(list, result_list_set))

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return None

        nums = sorted(nums)
        result_list = []
        length = len(nums)
        for i in xrange(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i + 1, length):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, length - 1
                sum_i_j = nums[i] + nums[j]
                while left < right:
                    sum_four = sum_i_j + nums[left] + nums[right]
                    if sum_four < target:
                        left += 1
                    elif sum_four > target:
                        right -= 1
                    else:
                        result_list.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

        return result_list

    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return None

        left, right = 0, len(numbers) - 1
        while left < right:
            sum_2 = numbers[left] + numbers[right]
            if sum_2 - target > 0:
                right -= 1
            elif sum_2 - target < 0:
                left += 1
            else:
                return [left + 1, right + 1]

        return None
