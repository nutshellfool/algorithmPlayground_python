from unittest import TestCase

from src.dynamicprogramming.leetcode_dynamicprogramming_solution import Solution


class TestLeetCodeDynamicProgrammingSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_fib(self):
        fib_num = self.solution.fib(4)
        self.assertEqual(3, fib_num)

    def test_fib_zero(self):
        fib_num = self.solution.fib(0)
        self.assertEqual(0, fib_num)

    def test_fib_negative(self):
        fib_num = self.solution.fib(-1)
        self.assertIsNone(fib_num)

    def test_fib_math_induction(self):
        fib_num = self.solution.fib_math_induction(4)
        self.assertEqual(3, fib_num)

    def test_fib_math_induction_zero(self):
        fib_num = self.solution.fib_math_induction(0)
        self.assertEqual(0, fib_num)

    def test_fib_math_induction_negative(self):
        fib_num = self.solution.fib_math_induction(-1)
        self.assertIsNone(fib_num)

    def test_climbStairs(self):
        steps = self.solution.climbStairs(3)
        self.assertEqual(3, steps)

    def test_climbStairs_zero(self):
        steps = self.solution.climbStairs(0)
        self.assertEqual(0, steps)

    def test_climbStairs_negative(self):
        steps = self.solution.climbStairs(-1)
        self.assertIsNone(steps)

    def test_climbStairs_math_induction(self):
        steps = self.solution.climbStairs_math_induction(3)
        self.assertEqual(3, steps)

    def test_climbStairs_math_induction_zero(self):
        steps = self.solution.climbStairs_math_induction(0)
        self.assertEqual(0, steps)

    def test_climbStairs_math_induction_negative(self):
        steps = self.solution.climbStairs_math_induction(-1)
        self.assertIsNone(steps)

    def test_minimumTotal(self):
        triangle = [[2],
                    [3, 4],
                    [6, 5, 7],
                    [4, 1, 8, 3]]
        min_total = self.solution.minimumTotal(triangle)
        self.assertEqual(11, min_total)

    def test_minimumTotal_none(self):
        min_total = self.solution.minimumTotal(None)
        self.assertIsNone(min_total)

    def test_maxProduct(self):
        array = [2, 3, -2, 4]
        max_product = self.solution.maxProduct(array)
        self.assertEqual(6, max_product)

    def test_maxProduct_zero(self):
        array = [-2, 0, -1]
        max_product = self.solution.maxProduct(array)
        self.assertEqual(0, max_product)

    def test_maxProduct_None(self):
        max_product = self.solution.maxProduct(None)
        self.assertIsNone(max_product)

    def test_maxProduct1(self):
        array = [2, 3, -2, 4]
        max_product = self.solution.maxProduct1(array)
        self.assertEqual(6, max_product)

    def test_maxProduct1_zero(self):
        array = [-2, 0, -1]
        max_product = self.solution.maxProduct1(array)
        self.assertEqual(0, max_product)

    def test_maxProduct1_None(self):
        max_product = self.solution.maxProduct1(None)
        self.assertIsNone(max_product)

    def test_lengthOfLIS(self):
        array = [10, 9, 2, 5, 3, 7, 101, 18]
        len_lis = self.solution.lengthOfLIS(array)
        self.assertEqual(4, len_lis)

    def test_lengthOfLIS_descend_order(self):
        array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        len_lis = self.solution.lengthOfLIS(array)
        self.assertEqual(1, len_lis)

    def test_lengthOfLIS_same(self):
        array = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        len_lis = self.solution.lengthOfLIS(array)
        self.assertEqual(1, len_lis)

    def test_lengthOfLIS_empty(self):
        len_lis = self.solution.lengthOfLIS([])
        self.assertEqual(0, len_lis)

    def test_lengthOfLIS_none(self):
        len_lis = self.solution.lengthOfLIS(None)
        self.assertEqual(0, len_lis)

    def test_coinChange(self):
        coins = [1, 2, 5]
        nums_coin = self.solution.coinChange(coins, 11)
        self.assertEqual(3, nums_coin)

    def test_coinChange_not_exist(self):
        nums_coin = self.solution.coinChange([2], 3)
        self.assertEqual(-1, nums_coin)

    def test_coinChange_none_coins(self):
        nums_coin = self.solution.coinChange([], 3)
        self.assertEqual(-1, nums_coin)

    def test_coinChange_negative_amount(self):
        nums_coin = self.solution.coinChange([1, 2, 5], -1)
        self.assertEqual(-1, nums_coin)

    #
    #   A further consideration:
    #
    #   what if the amount is a very big value ? for example sys.maxsize
    #
    # def test_coinChange_maxint_coin(self):
    #     nums_coin = self.solution.coinChange([1, maxsize - 2], maxsize - 1)
    #     self.assertEqual(2, nums_coin)

    def test_maxProfit(self):
        stock_prices_array = [7, 1, 5, 3, 6, 4]
        max_profit = self.solution.maxProfit(stock_prices_array)
        self.assertEqual(5, max_profit)

    def test_maxProfit_descent(self):
        stock_prices_array = [7, 6, 5, 4, 3, 1]
        max_profit = self.solution.maxProfit(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit_equal(self):
        stock_prices_array = [7, 7, 7, 7, 7, 7]
        max_profit = self.solution.maxProfit(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit_empty_array(self):
        stock_prices_array = []
        max_profit = self.solution.maxProfit(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit_none(self):
        max_profit = self.solution.maxProfit(None)
        self.assertEqual(0, max_profit)

    def test_maxProfit_instinct(self):
        stock_prices_array = [7, 1, 5, 3, 6, 4]
        max_profit = self.solution.maxProfit_instinct(stock_prices_array)
        self.assertEqual(5, max_profit)

    def test_maxProfit_instinct_descent(self):
        stock_prices_array = [7, 6, 5, 4, 3, 1]
        max_profit = self.solution.maxProfit_instinct(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit_instinct_equal(self):
        stock_prices_array = [7, 7, 7, 7, 7, 7]
        max_profit = self.solution.maxProfit_instinct(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit_instinct_empty_array(self):
        stock_prices_array = []
        max_profit = self.solution.maxProfit_instinct(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit_instinct_none(self):
        max_profit = self.solution.maxProfit_instinct(None)
        self.assertEqual(0, max_profit)

    def test_maxProfit_dp(self):
        stock_prices_array = [7, 1, 5, 3, 6, 4]
        max_profit = self.solution.maxProfit_dp(stock_prices_array)
        self.assertEqual(5, max_profit)

    def test_maxProfit_instinct_dp(self):
        stock_prices_array = [7, 6, 5, 4, 3, 1]
        max_profit = self.solution.maxProfit_dp(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit_dp_equal(self):
        stock_prices_array = [7, 7, 7, 7, 7, 7]
        max_profit = self.solution.maxProfit_dp(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit_dp_empty_array(self):
        stock_prices_array = []
        max_profit = self.solution.maxProfit_dp(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit_dp_none(self):
        max_profit = self.solution.maxProfit_dp(None)
        self.assertEqual(0, max_profit)

    def test_maxProfitUnlimitedTransaction(self):
        stock_prices_array = [7, 1, 5, 3, 6, 4]
        max_profit = self.solution.maxProfitUnlimitedTransaction(stock_prices_array)
        self.assertEqual(7, max_profit)

    def test_maxProfitUnlimitedTransaction_ascend(self):
        stock_prices_array = [1, 2, 3, 4, 5]
        max_profit = self.solution.maxProfitUnlimitedTransaction(stock_prices_array)
        self.assertEqual(4, max_profit)

    def test_maxProfitUnlimitedTransaction_descend(self):
        stock_prices_array = [7, 6, 5, 4, 3, 1]
        max_profit = self.solution.maxProfitUnlimitedTransaction(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfitUnlimitedTransaction_equal(self):
        stock_prices_array = [7, 7, 7, 7, 7, 7]
        max_profit = self.solution.maxProfitUnlimitedTransaction(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfitUnlimitedTransaction_empty_array(self):
        stock_prices_array = []
        max_profit = self.solution.maxProfitUnlimitedTransaction(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfitUnlimitedTransaction_none(self):
        max_profit = self.solution.maxProfitUnlimitedTransaction(None)
        self.assertEqual(0, max_profit)

    def test_maxProfitUnlimitedTransaction_op(self):
        stock_prices_array = [7, 1, 5, 3, 6, 4]
        max_profit = self.solution.maxProfitUnlimitedTransaction_op(stock_prices_array)
        self.assertEqual(7, max_profit)

    def test_maxProfitUnlimitedTransaction_op_ascend(self):
        stock_prices_array = [1, 2, 3, 4, 5]
        max_profit = self.solution.maxProfitUnlimitedTransaction_op(stock_prices_array)
        self.assertEqual(4, max_profit)

    def test_maxProfitUnlimitedTransaction_op_descend(self):
        stock_prices_array = [7, 6, 5, 4, 3, 1]
        max_profit = self.solution.maxProfitUnlimitedTransaction_op(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfitUnlimitedTransaction_op_equal(self):
        stock_prices_array = [7, 7, 7, 7, 7, 7]
        max_profit = self.solution.maxProfitUnlimitedTransaction_op(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfitUnlimitedTransaction_op_empty_array(self):
        stock_prices_array = []
        max_profit = self.solution.maxProfitUnlimitedTransaction_op(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfitUnlimitedTransaction_op_none(self):
        max_profit = self.solution.maxProfitUnlimitedTransaction_op(None)
        self.assertEqual(0, max_profit)

    def test_maxProfit2limitedTransaction(self):
        stock_prices_array = [3, 3, 5, 0, 0, 3, 1, 4]
        max_profit = self.solution.maxProfit2limitedTransaction(stock_prices_array)
        self.assertEqual(6, max_profit)

    def test_maxProfit2limitedTransaction_ascend(self):
        stock_prices_array = [1, 2, 3, 4, 5]
        max_profit = self.solution.maxProfit2limitedTransaction(stock_prices_array)
        self.assertEqual(4, max_profit)

    def test_maxProfit2limitedTransaction_descend(self):
        stock_prices_array = [7, 6, 5, 4, 3, 1]
        max_profit = self.solution.maxProfit2limitedTransaction(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit2limitedTransaction_equal(self):
        stock_prices_array = [7, 7, 7, 7, 7, 7]
        max_profit = self.solution.maxProfit2limitedTransaction(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit2limitedTransaction_empty_array(self):
        stock_prices_array = []
        max_profit = self.solution.maxProfit2limitedTransaction(stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfit2limitedTransaction_none(self):
        max_profit = self.solution.maxProfit2limitedTransaction(None)
        self.assertEqual(0, max_profit)
