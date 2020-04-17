# -*- coding: utf-8 -*-
from sys import maxsize


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 0:
            return None
        if N == 0:
            return 0
        if N < 3:
            return 1

        result = [0] * (N + 1)
        result[0] = 0
        result[1] = 1

        for i in xrange(2, N + 1):
            result[i] = result[i - 1] + result[i - 2]

        return result[N]

    def fib_math_induction(self, n):
        """
        :param n: int
        :return: int
        """
        if n < 0:
            return None
        gold_ratio = (1 + pow(5, 0.5)) / 2.0
        other_ratio = (1 - pow(5, 0.5)) / 2.0

        return int(round((pow(gold_ratio, n) - pow(other_ratio, n)) / pow(5, 0.5)))

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return None
        if n == 0:
            return 0
        result = [0] * (n + 1)
        result[0] = 1
        result[1] = 1
        for i in xrange(2, n + 1):
            result[i] = result[i - 1] + result[i - 2]

        return result[n]

    def climbStairs_math_induction(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return None
        if n == 0:
            return 0
        gold_ratio = (1 + pow(5, 0.5)) / 2.0
        other_ratio = (1 - pow(5, 0.5)) / 2.0

        return int(round((pow(gold_ratio, n + 1) - pow(other_ratio, n + 1)) / pow(5, 0.5)))

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return None

        row_length = len(triangle)
        column_length = len(triangle[len(triangle) - 1])

        position_min_total = [[0] * column_length] * row_length

        for i in xrange(column_length):
            position_min_total[row_length - 1][i] = triangle[row_length - 1][i]

        for i in reversed(xrange(row_length - 1)):
            column_size = len(triangle[i])
            for j in xrange(column_size):
                position_min_total[i][j] = min(position_min_total[i + 1][j], position_min_total[i + 1][j + 1]) + \
                                           triangle[i][j]

        return position_min_total[0][0]

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        row_len = len(nums)
        dp_max = [0] * row_len
        dp_min = [0] * row_len
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        result = nums[0]
        for i in xrange(1, row_len):
            if nums[i] >= 0:
                dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i])
                dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i])
            else:
                dp_max[i] = max(nums[i], dp_min[i - 1] * nums[i])
                dp_min[i] = min(nums[i], dp_max[i - 1] * nums[i])
            result = max(dp_max[i], result)

        return result

    def maxProduct1(self, nums):
        if not nums:
            return None

        row_len = len(nums)
        column_len = 2
        dp = [[0 for i in xrange(column_len)] for j in xrange(row_len)]
        dp[0][0], dp[0][1] = nums[0], nums[0]

        result = nums[0]

        for i in xrange(1, row_len):
            # brutal force beauty
            dp[i][0] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            dp[i][1] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])

            result = max(result, dp[i][0])

        return result

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [1] * len(nums)
        result = 0

        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])

        return result

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount <= 0:
            return -1

        # dp = [float('inf')] * (amount + 1)
        # dp = [maxsize] * (amount + 1)
        dp = [0] * (amount + 1)
        for i in xrange(amount + 1):
            dp[i] = amount + 1
        dp[0] = 0

        for coin in coins:
            for x in xrange(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        # return dp[amount] if dp[amount] != float('inf') else -1
        # return dp[amount] if dp[amount] != maxsize else -1
        return -1 if dp[amount] > amount else dp[amount]

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return None

        min_price = maxsize
        max_profit = 0
        for i, price in enumerate(prices):
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, (price - min_price))

        return max_profit

    def maxProfit_instinct(self, prices):
        if not prices:
            return None

        max_profit = 0
        for i, price_i in enumerate(prices):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - price_i
                max_profit = max(max_profit, profit)
        return max_profit

    def maxProfit_dp(self, prices):
        if not prices:
            return None

        # max_profit(i, j, k)
        #
        #   i = 0 ... i day
        #   j = 0, 1
        #   k = 0, 1, ... k
        #
        #   i means day indices
        #   j means stock holding status (0: do NoT holding, 1: holding )
        #   k means already completed transaction times
        _MAX_TRANSACTION_NUM = 1
        max_profit = [[[0 for k in range(_MAX_TRANSACTION_NUM + 1)] for j in range(2)] for i in range(len(prices))]

        for k in xrange(_MAX_TRANSACTION_NUM + 1):
            max_profit[0][0][k] = 0
            max_profit[0][1][k] = - prices[0]

        for i in xrange(1, len(prices)):
            for k in xrange(_MAX_TRANSACTION_NUM):
                # 'buy-in' can be count as a transaction
                # 'sell-out' should NOT count again
                max_profit[i][0][k] = max(max_profit[i - 1][1][k] + prices[i], max_profit[i - 1][0][k])
                max_profit[i][1][k] = max(max_profit[i - 1][0][k - 1] - prices[i], max_profit[i - 1][1][k])

        return max(max_profit[len(prices) - 1][0])
