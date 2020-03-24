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

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n - 1)

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        for i in xrange(num + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result

    def countBits_instinct(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        for i in xrange(num + 1):
            result[i] = self.hammingWeight(i)

        return result
