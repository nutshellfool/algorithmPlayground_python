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
