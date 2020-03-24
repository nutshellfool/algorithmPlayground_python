# -*- coding: utf-8 -*-


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hamming_weight = 0
        while n:
            hamming_weight += 1
            n = n & n - 1
            # if n & 1:
            #     hamming_weight += 1
            # n = n >> 1

        return hamming_weight

    def hammingWeight_instinct(self, n):
        """
        :type n: int
        :rtype: int
        """
        hamming_weight = 0
        while n:
            if n & 1:
                hamming_weight += 1
            n = n >> 1

        return hamming_weight
