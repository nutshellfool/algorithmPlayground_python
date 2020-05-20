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

    def test_maxProfitklimitedTransaction(self):
        stock_prices_array = [3, 2, 6, 5, 0, 3]
        max_profit = self.solution.maxProfitklimitedTransaction(2, stock_prices_array)
        self.assertEqual(7, max_profit)

    def test_maxProfitklimitedTransaction_ascend(self):
        stock_prices_array = [1, 2, 3, 4, 5]
        max_profit = self.solution.maxProfitklimitedTransaction(2, stock_prices_array)
        self.assertEqual(4, max_profit)

    def test_maxProfitklimitedTransaction_descend(self):
        stock_prices_array = [7, 6, 5, 4, 3, 1]
        max_profit = self.solution.maxProfitklimitedTransaction(2, stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfitklimitedTransaction_equal(self):
        stock_prices_array = [7, 7, 7, 7, 7, 7]
        max_profit = self.solution.maxProfitklimitedTransaction(2, stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfitklimitedTransaction_empty_array(self):
        stock_prices_array = []
        max_profit = self.solution.maxProfitklimitedTransaction(2, stock_prices_array)
        self.assertEqual(0, max_profit)

    def test_maxProfitklimitedTransaction_none(self):
        max_profit = self.solution.maxProfitklimitedTransaction(2, None)
        self.assertEqual(0, max_profit)

    def test_maxProfitklimitedTransaction_extrem_case(self):
        stock_price_array = [106, 373, 495, 46, 359, 919, 906, 440, 783, 583, 784, 73, 238, 701, 972, 308, 165, 774,
                             990, 675, 737, 990, 713, 157, 211, 880, 961, 132, 980, 136, 285, 239, 628, 221, 948, 939,
                             28, 541, 414, 180, 171, 640, 297, 873, 59, 814, 832, 611, 868, 633, 101, 67, 396, 264, 445,
                             548, 257, 656, 624, 71, 607, 67, 836, 14, 373, 205, 434, 203, 661, 793, 45, 623, 140, 67,
                             177, 885, 155, 764, 363, 269, 599, 32, 228, 111, 102, 565, 918, 592, 604, 244, 982, 533,
                             781, 604, 115, 429, 33, 894, 778, 885, 145, 888, 577, 275, 644, 824, 277, 302, 182, 94,
                             479, 563, 52, 771, 544, 794, 964, 827, 744, 366, 548, 761, 477, 434, 999, 86, 1000, 5, 99,
                             311, 346, 609, 778, 937, 372, 793, 754, 191, 592, 860, 748, 297, 610, 386, 146, 220, 7,
                             113, 657, 438, 482, 700, 158, 884, 877, 964, 777, 139, 809, 489, 383, 92, 581, 970, 899,
                             947, 864, 443, 490, 825, 674, 906, 402, 270, 416, 611, 949, 476, 775, 899, 837, 796, 227,
                             232, 226, 11, 266, 889, 215, 6, 182, 430, 5, 706, 994, 128, 359, 841, 439, 263, 491, 689,
                             638, 485, 763, 695, 135, 800, 763, 54, 569, 387, 112, 316, 193, 675, 546, 531, 954, 571,
                             208, 282, 557, 892, 469, 875, 765, 592, 374, 276, 892, 843, 625, 180, 249, 292, 477, 882,
                             837, 112, 46, 667, 187, 93, 418, 790, 903, 12, 978, 510, 647, 446, 597, 958, 678, 897, 420,
                             907, 256, 170, 669, 920, 711, 635, 995, 259, 994, 634, 583, 175, 380, 435, 942, 739, 921,
                             132, 455, 986, 567, 464, 301, 10, 579, 84, 745, 717, 588, 414, 375, 319, 770, 310, 510,
                             521, 88, 445, 59, 460, 120, 765, 480, 441, 169, 374, 180, 947, 179, 346, 490, 417, 149,
                             140, 577, 624, 427, 238, 341, 686, 623, 228, 672, 859, 372, 938, 567, 141, 133, 671, 255,
                             997, 272, 591, 115, 340, 692, 531, 235, 123, 677, 980, 31, 774, 135, 194, 956, 723, 779,
                             375, 546, 59, 695, 616, 416, 362, 38, 145, 782, 184, 418, 806, 444, 177, 360, 485, 941,
                             998, 85, 840, 740, 545, 49, 570, 17, 824, 845, 749, 177, 727, 238, 656, 787, 425, 473, 323,
                             683, 578, 442, 436, 444, 595, 367, 44, 467, 93, 507, 949, 598, 579, 471, 1, 347, 982, 232,
                             878, 217, 845, 777, 284, 527, 529, 100, 482, 456, 814, 457, 251, 494, 419, 922, 139, 706,
                             384, 954, 365, 680, 70, 810, 764, 820, 992, 622, 29, 697, 294, 553, 655, 63, 934, 827, 157,
                             680, 812, 729, 486, 403, 151, 988, 926, 460, 193, 294, 423, 774, 715, 906, 957, 598, 929,
                             339, 119, 686, 88, 228, 803, 806, 743, 430, 315, 224, 712, 724, 69, 606, 411, 271, 700,
                             520, 179, 916, 490, 652, 319, 69, 245, 827, 185, 200, 911, 363, 335, 50, 353, 551, 737, 15,
                             429, 966, 766, 307, 829, 379, 184, 779, 239, 254, 904, 262, 719, 321, 380, 253, 564, 348,
                             878, 570, 470, 313, 752, 563, 164, 301, 239, 856, 491, 154, 795, 640, 199, 940, 420, 201,
                             254, 400, 865, 886, 819, 424, 292, 257, 572, 112, 590, 984, 421, 639, 705, 707, 779, 660,
                             4, 817, 265, 465, 737, 56, 564, 797, 178, 552, 988, 621, 98, 665, 379, 607, 300, 439, 269,
                             196, 94, 860, 540, 830, 756, 294, 806, 321, 930, 623, 206, 440, 730, 829, 566, 420, 488,
                             49, 438, 447, 294, 548, 804, 514, 45, 383, 431, 373, 424, 11, 377, 868, 559, 316, 831, 464,
                             211, 710, 803, 680, 665, 39, 523, 951, 219, 293, 909, 838, 708, 663, 627, 220, 100, 565,
                             269, 982, 236, 185, 194, 697, 556, 767, 541, 360, 103, 497, 271, 919, 19, 206, 73, 393, 50,
                             421, 466, 970, 329, 105, 618, 17, 687, 578, 260, 759, 366, 334, 686, 613, 616, 893, 351,
                             847, 861, 452, 454, 454, 88, 135, 357, 194, 220, 504, 36, 916, 246, 718, 172, 395, 292,
                             613, 533, 662, 983, 701, 877, 842, 445, 263, 529, 679, 526, 31, 385, 918, 898, 584, 846,
                             474, 648, 67, 331, 890, 174, 766, 274, 476, 414, 701, 835, 537, 531, 578, 7, 479, 906, 93,
                             667, 735, 435, 899, 49, 953, 854, 843, 326, 322, 13, 865, 791, 828, 686, 760, 957, 655,
                             601, 406, 185, 738, 788, 519, 874, 630, 440, 839, 511, 149, 715, 566, 988, 0, 354, 498, 81,
                             193, 335, 196, 157, 515, 590, 768, 366, 287, 386, 502, 143, 547, 659, 616, 822, 479, 813,
                             497, 222, 285, 6, 453, 363, 906, 388, 733, 804, 624, 963, 634, 319, 817, 674, 754, 378,
                             999, 373, 793, 419, 246, 274, 960, 1, 130, 186, 576, 382, 204, 227, 607, 435, 299, 790,
                             603, 196, 236, 955, 654, 812, 214, 297, 926, 721, 977, 568, 339, 913, 297, 621, 783, 242,
                             257, 483, 325, 998, 164, 586, 782, 597, 210, 522, 369, 676, 339, 626, 650, 634, 477, 793,
                             85, 12, 695, 655, 53, 287, 730, 0, 689, 225, 805, 593, 430, 610, 963, 172, 148, 740, 579,
                             16, 523, 570, 802, 627, 220, 664, 945, 788, 500, 90, 410, 916, 481, 454, 538, 622, 161,
                             373, 523, 757, 446, 855, 958, 390, 333, 927, 253, 814, 442, 77, 325, 14, 655, 502, 200,
                             791, 58, 714, 951, 370, 557, 261, 859, 199, 46, 775, 249, 369, 233, 321, 733, 310, 503,
                             539, 618, 839, 272, 315, 999, 229, 390, 359, 528, 334, 878, 342, 977, 869, 704, 564, 506,
                             867, 77, 248, 674, 557, 258, 710, 126, 617, 531, 969, 289, 578, 947, 103, 581, 599, 918,
                             686, 143, 253, 56, 393, 58, 144, 211, 806, 285, 635, 203, 194, 884, 687, 653, 856, 688,
                             623, 568, 394, 749, 302, 534, 631, 894, 167, 111, 227, 296, 41, 854, 81, 147, 656, 319,
                             748, 530, 457, 340, 223, 896, 77, 166, 974, 659, 36, 338, 177, 496, 483, 690, 569, 504,
                             211, 554, 758, 732, 660, 61, 62, 669, 273, 0, 616, 899, 789, 380, 386, 357, 403, 251, 926,
                             636, 419, 148, 820, 774, 485, 497, 370, 907, 973, 255, 277, 341, 466, 254, 333, 219, 819,
                             521, 974, 213, 590, 981, 697, 927, 904, 717, 726, 574, 94, 625, 991, 378, 249, 388, 786,
                             355, 69, 318, 357, 467, 695, 825, 585, 940, 323, 993, 549, 485, 564, 833, 530, 398, 789,
                             608, 59, 541, 915, 81, 681, 544, 460, 318, 954, 764, 879, 708, 258, 276, 259, 505, 649,
                             529, 824, 914, 660, 490, 666, 676, 618, 339, 712, 981, 802, 239, 605, 270, 29, 491, 41,
                             243, 361, 644, 327, 472, 460, 725, 864, 129, 142, 610, 782, 935, 929, 63, 865, 287, 316,
                             740, 212, 152, 567, 620, 591, 394, 805, 586, 177, 918, 516, 911, 944, 427, 128, 778, 930,
                             965, 27, 633, 534, 567, 575, 247, 691, 571, 775, 456, 622, 219, 698, 772, 305, 27, 810,
                             690, 555, 222, 877, 985, 493, 202, 84, 180, 133, 129, 539, 151, 275, 234, 999, 676, 629,
                             715, 839, 6, 789, 663, 467, 435, 275, 580, 296, 8, 73, 849, 456, 681, 794, 954, 543, 602,
                             615, 4, 131, 593, 778, 175, 587, 670, 88, 648, 79, 703, 99, 457, 261, 722, 357, 966, 724,
                             523, 612, 610, 376, 575, 174, 2, 53, 637, 478, 850, 250, 238, 344, 381, 543, 686, 761, 582,
                             598, 804, 12, 128, 928, 133, 998, 188, 598, 590, 507, 898, 402, 771, 703, 912, 744, 317,
                             300, 852, 631, 767, 157, 278, 520, 452, 721, 560, 112, 206, 69, 317, 498, 942, 942, 963,
                             347, 61, 186, 390, 128, 946, 462, 230, 551, 956, 195, 960, 143, 225, 654, 255, 370, 778,
                             770, 487, 192, 479, 180, 505, 509, 508, 717, 976, 826, 346, 521, 472, 148, 965, 965, 971,
                             421, 402, 233, 76, 543, 533, 815, 281, 986, 638, 936, 139, 754, 728, 779, 551, 425, 17,
                             546, 516, 862, 963, 648, 127, 510, 453, 311, 759, 654, 550, 755, 654, 567, 129, 34, 927,
                             900, 421, 961, 923, 117, 766, 71, 132, 680, 917, 460, 609, 874, 179, 336, 496, 287, 61,
                             846, 228, 871, 590, 858, 404, 646, 449, 770, 724, 245, 634, 900, 496, 157, 864, 407, 632,
                             998, 596, 451, 482, 921, 102, 624, 148, 346, 282, 624, 150, 523, 598, 492, 267, 54, 889,
                             872, 979, 38, 1, 282, 513, 877, 798, 994, 400, 254, 435, 487, 707, 459, 575, 275, 297, 165,
                             104, 468, 80, 820, 571, 215, 869, 381, 107, 209, 762, 455, 415, 810, 137, 674, 304, 692,
                             639, 304, 534, 348, 938, 575, 432, 471, 74, 631, 291, 405, 622, 352, 58, 549, 832, 655,
                             458, 688, 468, 827, 447, 946, 181, 908, 585, 53, 905, 733, 363, 210, 536, 960, 577, 815,
                             462, 193, 31, 731, 8, 538, 695, 936, 795, 139, 782, 357, 52, 492, 610, 512, 544, 323, 276,
                             649, 940, 54, 749, 723, 544, 365, 500, 441, 284, 17, 660, 748, 871, 701, 591, 356, 64, 34,
                             422, 713, 978, 96, 218, 756, 833, 177, 832, 61, 91, 764, 510, 188, 415, 622, 473, 549, 944,
                             716, 998, 528, 61, 829, 953, 280, 284, 706, 323, 981, 405, 91, 887, 568, 874, 725, 236,
                             933, 41, 895, 940, 375, 468, 314, 667, 694, 609, 631, 621, 655, 640, 835, 513, 461, 854,
                             419, 455, 860, 912, 572, 769, 963, 213, 818, 158, 840, 699, 414, 969, 430, 59, 855, 997,
                             997, 884, 349, 723, 837, 488, 430, 671, 743, 943, 310, 399, 884, 423, 486, 587, 491, 106,
                             716, 0, 768, 704, 483, 663, 827, 587, 915, 904, 742, 976, 6, 455, 221, 849, 920, 548, 156,
                             35, 101, 270, 684, 123, 549, 649, 977, 711, 965, 492, 525, 130, 744, 697, 910, 699, 301,
                             285, 696, 313, 117, 122, 777, 163, 789, 924, 543, 446, 60, 214, 102, 97, 45, 670, 960, 23,
                             522, 680, 178, 757, 792, 633, 244, 327, 129, 188, 357, 733, 419, 496, 774, 408, 90, 615,
                             663, 321, 526, 946, 990, 273, 135, 373, 719, 870, 810, 798, 826, 64, 971, 156, 233, 587,
                             253, 712, 384, 964, 173, 511, 116, 291, 639, 450, 947, 623, 656, 548, 605, 498, 709, 143,
                             895, 739, 663, 160, 442, 820, 802, 380, 413, 356, 742, 744, 764, 421, 355, 499, 614, 678,
                             336, 850, 1000, 463, 794, 388, 478, 188, 576, 822, 164, 209, 465, 901, 116, 729, 891, 952,
                             611, 15, 798, 731, 711, 6, 459, 587, 278, 996, 220, 642, 563, 363, 271, 16, 379, 959, 332,
                             315, 414, 659, 602, 786, 571, 78, 450, 544, 393, 404, 953, 480, 215, 771, 419, 8, 738, 36,
                             191, 138, 204, 146, 923, 413, 908, 998, 46, 928, 678, 425, 584, 372, 689, 245, 721, 177,
                             833, 44, 784, 121, 164, 16, 714, 680, 974, 685, 340, 810, 101, 301, 791, 716, 697, 768, 33,
                             901, 994, 417, 353, 248, 559, 807, 64, 450, 724, 896, 889, 880, 818, 89, 495, 848, 915,
                             450, 409, 958, 413, 149, 743, 782, 64, 687, 196, 737, 769, 311, 429, 598, 585, 690, 919,
                             331, 94, 211, 633, 888, 856, 844, 870, 931, 934, 66, 407, 121, 902, 417, 522, 423, 821,
                             196, 625, 855, 830, 673, 463, 181, 857, 775, 374, 490, 971, 751, 835, 823, 770, 79, 916,
                             80, 829, 810, 856, 674, 524, 352, 251, 548, 899, 363, 465, 0, 989, 322, 51, 86, 740, 542,
                             920, 310, 365, 677, 287, 688, 373, 225, 774, 331, 430, 482, 630, 46, 567, 236, 370, 502,
                             347, 191, 137, 646, 218, 634, 399, 278, 423, 540, 26, 612, 700, 43, 508, 176, 268, 525,
                             267, 676, 257, 651, 88, 349, 556, 6, 463, 29, 410, 753, 224, 693, 535, 747, 40, 854, 155,
                             376, 192, 434, 12, 342, 98, 718, 639, 951, 205, 923, 354, 564, 988, 960, 676, 965, 29, 104,
                             898, 535, 915, 868, 768, 269, 294, 944, 523, 145, 895, 382, 53, 935, 671, 518, 338, 623,
                             524, 204, 146, 900, 161, 258, 739, 417, 119, 825, 336, 182, 123, 749, 355, 188, 109, 740,
                             945, 826, 921, 123, 65, 69, 682, 461, 259, 661, 247, 523, 796, 153, 142, 851, 411, 536,
                             190, 478, 417, 296, 113, 158, 263, 754, 532, 368, 748, 42, 890, 129, 643, 717, 564, 525, 5,
                             348, 204, 383, 427, 696, 861, 684, 902, 591, 609, 467, 837, 104, 565, 168, 828, 916, 645,
                             232, 153, 794, 384, 642, 753, 550, 176, 142, 132, 141, 192, 635, 14, 634, 329, 403, 790,
                             460, 29, 512, 443, 15, 74, 114, 456, 487, 303, 13, 822, 429, 136, 113, 637, 283, 542, 519,
                             411, 564, 220, 346, 907, 389, 780, 479, 480, 179, 385, 285, 445, 393, 508, 885, 697, 168,
                             542, 357, 553, 149, 710, 126, 508, 271, 845, 689, 231, 217, 984, 848, 905, 87, 168, 1000,
                             169, 336, 672, 595, 501, 411, 81, 707, 708, 634, 150, 722, 379, 77, 762, 737, 585, 419,
                             428, 37, 869, 509, 222, 335, 192, 980, 209, 883, 864, 215, 497, 992, 155, 408, 652, 927,
                             990, 708, 439, 857, 934, 838, 69, 140, 713, 573, 939, 338, 628, 685, 412, 147, 530, 643,
                             471, 545, 58, 111, 132, 665, 572, 38, 176, 460, 555, 997, 61, 602, 471, 901, 620, 830, 577,
                             436, 495, 685, 619, 600, 549, 270, 77, 512, 249, 697, 466, 864, 336, 981, 901, 573, 702,
                             694, 937, 299, 565, 436, 613, 187, 377, 364, 473, 405, 384, 280, 658, 561, 85, 987, 302,
                             856, 107, 191, 486, 464, 165, 514, 948, 227, 310, 133, 799, 363, 481, 289, 153, 990, 445,
                             246, 454, 729, 887, 980, 546, 730, 528, 817, 521, 437, 376, 238, 965, 511, 995, 432, 227,
                             883, 550, 904, 818, 556, 295, 413, 786, 861, 248, 113, 660, 982, 445, 292, 562, 722, 433,
                             621, 783, 375, 53, 236, 856, 275, 898, 532, 915, 804, 362, 545, 373, 397, 740, 453, 726,
                             983, 665, 715, 379, 176, 408, 3, 911, 573, 883, 195, 254, 469, 758, 844, 355, 409, 562,
                             307, 752, 274, 105, 227, 635, 121, 335, 338, 46, 993, 243, 567, 765, 589, 806, 405, 558,
                             25, 246, 526, 490, 306, 295, 112, 847, 792, 759, 881, 500, 398, 791, 266, 33, 372, 546,
                             217, 286, 898, 596, 955, 720, 70, 9, 458, 698, 367, 936, 134, 95, 887, 300, 975, 72, 235,
                             77, 870, 943, 511, 883, 923, 619, 812, 904, 990, 643, 871, 346, 588, 807, 957, 681, 581,
                             195, 82, 448, 146, 807, 559, 21, 412, 950, 536, 681, 541, 856, 631, 378, 258, 736, 116,
                             580, 20, 606, 748, 537, 343, 681, 22, 711, 628, 536, 395, 422, 874, 135, 519, 294, 876,
                             185, 583, 392, 253, 220, 80, 341, 203, 970, 825, 762, 558, 942, 797, 651, 290, 8, 414, 375,
                             913, 167, 977, 94, 706, 970, 286, 278, 349, 909, 422, 887, 921, 492, 467, 550, 538, 555,
                             841, 446, 199, 312, 816, 562, 296, 609, 39, 393, 240, 763, 222, 828, 802, 944, 714, 325,
                             334, 936, 995, 950, 487, 433, 195, 370, 498, 926, 109, 543, 885, 463, 687, 171, 703, 985,
                             292, 123, 314, 174, 183, 588, 487, 857, 63, 736, 126, 156, 172, 367, 313, 672, 494, 56,
                             202, 470, 821, 735, 72, 812, 282, 570, 756, 633, 82, 52, 920, 300, 199, 927, 534, 214, 354,
                             764, 84, 419, 462, 5, 246, 787, 305, 788, 852, 58, 698, 241, 184, 904, 533, 333, 857, 215,
                             531, 81, 862, 567, 56, 773, 741, 169, 982, 965, 302, 724, 145, 342, 731, 184, 914, 977,
                             933, 727, 918, 420, 438, 491, 300, 104, 107, 730, 506, 214, 214, 968, 351, 66, 844, 965,
                             758, 845, 503, 495, 503, 208, 281, 622, 905, 49, 751, 660, 268, 420, 360, 354, 971, 441,
                             565, 513, 711, 283, 695, 109, 432, 127, 399, 177, 640, 67, 77, 364, 327, 943, 1000, 979,
                             278, 526, 222, 929, 120, 753, 580, 743, 456, 241, 148, 339, 599, 919, 11, 473, 101, 365,
                             789, 465, 819, 778, 134, 278, 89, 598, 801, 904, 681, 695, 599, 43, 897, 763, 193, 257,
                             719, 410, 610, 58, 72, 912, 598, 793, 347, 640, 725, 855, 390, 754, 785, 70, 449, 24, 962,
                             843, 735, 729, 893, 797, 512, 390, 57, 474, 336, 855, 970, 389, 722, 735, 464, 28, 894,
                             664, 645, 96, 357, 255, 117, 795, 479, 151, 790, 432, 748, 780, 940, 255, 204, 607, 999,
                             989, 48, 139, 945, 783, 736, 826, 640, 597, 171, 423, 457, 972, 424, 419, 140, 706, 333,
                             648, 557, 155, 707, 547, 337, 66, 338, 818, 829, 972, 13, 500, 310, 961, 668, 991, 407,
                             386, 893, 589, 308, 129, 739, 689, 452, 361, 822, 418, 606, 961, 981, 385, 132, 7, 938,
                             102, 942, 534, 154, 133, 921, 51, 257, 205, 281, 771, 215, 508, 816, 466, 744, 85, 141,
                             163, 418, 894, 386, 779, 142, 137, 825, 556, 764, 647, 414, 792, 605, 945, 36, 427, 173,
                             907, 356, 893, 875, 449, 621, 181, 963, 801, 14, 502, 234, 495, 437, 86, 635, 846, 182,
                             182, 540, 340, 648, 772, 195, 93, 539, 716, 573, 431, 342, 989, 156, 745, 436, 709, 22,
                             532, 100, 504, 0, 985, 838, 461, 725, 555, 219, 710, 568, 914, 736, 791, 507, 615, 442,
                             494, 977, 546, 519, 389, 614, 78, 172, 991, 255, 154, 243, 495, 876, 267, 948, 657, 692,
                             46, 107, 864, 168, 785, 965, 740, 16, 878, 713, 79, 517, 68, 208, 621, 13, 362, 99, 379,
                             109, 823, 960, 645, 440, 944, 342, 710, 267, 656, 646, 639, 453, 155, 867, 456, 606, 328,
                             444, 136, 89, 104, 650, 36, 240, 320, 31, 352, 522, 520, 260, 510, 981, 591, 655, 668, 23,
                             544, 320, 541, 707, 133, 708, 809, 972, 196, 59, 383, 642, 153, 993, 837, 98, 300, 751,
                             564, 399, 848, 325, 903, 534, 662, 201, 690, 300, 404, 115, 104, 600, 236, 752, 651, 640,
                             244, 254, 40, 549, 304, 86, 600, 755, 59, 662, 106, 290, 368, 725, 138, 705, 28, 550, 955,
                             277, 959, 346, 721, 759, 569, 420, 424, 59, 989, 438, 867, 725, 544, 178, 575, 137, 21,
                             536, 72, 617, 194, 421, 226, 378, 483, 880, 688, 791, 930, 97, 831, 113, 711, 445, 308,
                             813, 967, 120, 769, 329, 718, 899, 364, 638, 308, 644, 25, 138, 88, 732, 922, 721, 850,
                             835, 367, 831, 292, 651, 966, 268, 628, 925, 205, 824, 429, 917, 534, 323, 887, 3, 302,
                             134, 904, 300, 678, 929, 491, 229, 671, 817, 442, 678, 879, 373, 664, 990, 53, 395, 738,
                             570, 497, 113, 322, 557, 341, 641, 331, 932, 830, 433, 590, 738, 780, 50, 446, 504, 743,
                             311, 980, 88, 224, 732, 316, 664, 742, 69, 146, 801, 334, 41, 198, 629, 690, 869, 598, 612,
                             662, 385, 637, 769, 984, 316, 741, 980, 2, 794, 814, 730, 297, 503, 734, 836, 604, 674,
                             376, 692, 277, 727, 455, 975, 703, 115, 25, 552, 404, 460, 543, 738, 86, 488, 356, 929,
                             668, 835, 222, 413, 172, 221, 1000, 30, 888, 350, 514, 908, 870, 323, 991, 201, 738, 335,
                             189, 437, 604, 316, 514, 575, 531, 514, 318, 43, 592, 594, 9, 773, 609, 952, 708, 868, 291,
                             962, 572, 772, 291, 214, 992, 238, 275, 36, 882, 631, 376, 150, 838, 376, 862, 996, 258,
                             545, 331, 907, 958, 925, 503, 1, 745, 559, 147, 617, 487, 185, 623, 287, 658, 340, 84, 835,
                             563, 168, 845, 401, 395, 928, 277, 136, 890, 276, 45, 806, 121, 264, 416, 417, 596, 208,
                             106, 738, 352, 995, 746, 731, 72, 258, 112, 885, 445, 165, 74, 847, 633, 343, 721, 237, 20,
                             91, 575, 410, 765, 274, 233, 738, 893, 999, 283, 104, 414, 981, 448, 761, 47, 48, 725, 459,
                             265, 318, 564, 353, 260, 896, 874, 563, 492, 710, 336, 952, 80, 195, 326, 311, 716, 167,
                             561, 556, 234, 680, 631, 112, 573, 248, 422, 130, 219, 134, 75, 722, 188, 221, 238, 193,
                             689, 63, 787, 657, 956, 214, 895, 657, 169, 349, 575, 577, 869, 64, 325, 187, 471, 535,
                             572, 39, 872, 966, 22, 232, 427, 501, 855, 239, 487, 263, 335, 645, 461, 973, 447, 923,
                             922, 788, 286, 610, 55, 708, 827, 250, 355, 481, 379, 322, 926, 796, 815, 2, 952, 268, 257,
                             61, 795, 364, 999, 535, 494, 664, 619, 711, 228, 411, 587, 292, 345, 671, 640, 231, 384,
                             859, 88, 640, 838, 904, 27, 235, 605, 766, 887, 23, 438, 816, 764, 91, 12, 324, 709, 411,
                             659, 405, 927, 769, 505, 259, 383, 714, 333, 652, 648, 663, 604, 596, 231, 114, 320, 955,
                             689, 626, 495, 758, 96, 848, 43, 189, 848, 656, 114, 475, 349, 148, 995, 467, 94, 519, 141,
                             125, 598, 738, 822, 701, 194, 46, 936, 332, 370, 764, 944, 711, 889, 568, 508, 186, 981,
                             48, 400, 69, 182, 698, 25, 526, 808, 272, 963, 451, 335, 883, 718, 199, 185, 437, 81, 987,
                             4, 274, 482, 263, 509, 584, 767, 141, 53, 365, 14, 657, 712, 837, 161, 378, 525, 313, 685,
                             183, 869, 202, 382, 339, 351, 686, 15, 667, 636, 756, 553, 848, 57, 740, 862, 962, 838,
                             410, 722, 409, 589, 891, 370, 520, 790, 880, 276, 478, 26, 459, 671, 728, 301, 296, 75,
                             194, 173, 116, 938, 933, 977, 812, 863, 868, 286, 973, 984, 265, 631, 456, 436, 683, 28,
                             126, 319, 285, 62, 247, 88, 60, 824, 710, 26, 602, 897, 765, 998, 610, 138, 773, 555, 153,
                             114, 932, 21, 111, 171, 282, 246, 909, 419, 647, 781, 166, 966, 200, 521, 188, 808, 295,
                             685, 1000, 890, 353, 301, 983, 862, 527, 974, 241, 705, 437, 523, 213, 704, 421, 225, 428,
                             310, 255, 719, 243, 962, 757, 27, 476, 181, 138, 95, 309, 122, 500, 846, 627, 371, 470,
                             759, 255, 373, 520, 748, 856, 459, 71, 431, 782, 307, 524, 644, 130, 120, 56, 406, 387,
                             435, 201, 7, 392, 922, 503, 578, 331, 827, 954, 21, 351, 869, 65, 300, 697, 908, 505, 315,
                             198, 744, 892, 510, 307, 985, 129, 634, 773, 343, 640, 702, 748, 973, 594, 271, 151, 254,
                             513, 339, 843, 425, 153, 19, 309, 489, 333, 944, 442, 904, 447, 239, 487, 6, 230, 988, 656,
                             716, 488, 779, 362, 738, 663, 516, 432, 964, 142, 823, 353, 175, 797, 645, 613, 553, 26,
                             41, 946, 47, 479, 181, 964, 901, 251, 843, 715, 211, 366, 335, 16, 103, 547, 171, 276, 29,
                             165, 993, 424, 274, 334, 754, 982, 63, 963, 904, 150, 342, 301, 238, 152, 314, 892, 498,
                             958, 192, 806, 208, 681, 703, 970, 688, 5, 809, 705, 182, 230, 658, 531, 793, 303, 475,
                             825, 924, 538, 488, 100, 655, 524, 569, 655, 430, 808, 820, 402, 852, 760, 691, 751, 779,
                             868, 247, 688, 545, 780, 350, 400, 550, 307, 577, 803, 527, 302, 916, 984, 829, 257, 172,
                             392, 41, 233, 241, 587, 159, 176, 904, 926, 540, 324, 918, 177, 817, 585, 722, 89, 987,
                             476, 637, 210, 980, 905, 911, 547, 762, 490, 197, 718, 774, 982, 484, 781, 675, 152, 144,
                             412, 255, 800, 480, 901, 892, 309, 382, 873, 469, 662, 375, 499, 646, 436, 410, 866, 440,
                             708, 613, 842, 663, 604, 555, 133, 77, 458, 66, 660, 504, 635, 896, 621, 126, 995, 506, 7,
                             283, 11, 610, 11, 727, 667, 101, 589, 309, 240, 508, 368, 830, 805, 4, 259, 936, 39, 510,
                             645, 772, 993, 530, 932, 393, 19, 82, 915, 994, 853, 683, 183, 797, 61, 292, 942, 434, 846,
                             265, 316, 991, 751, 579, 182, 162, 454, 5, 194, 97, 451, 906, 177, 761, 988, 314, 425, 5,
                             63, 127, 565, 427, 774, 66, 195, 627, 731, 750, 586, 874, 599, 878, 759, 807, 192, 9, 971,
                             279, 127, 424, 357, 671, 573, 451, 104, 51, 105, 699, 375, 99, 775, 421, 490, 968, 442,
                             965, 492, 974, 639, 584, 647, 676, 186, 586, 730, 345, 617, 337, 256, 477, 985, 847, 681,
                             689, 696, 893, 198, 631, 509, 662, 813, 33, 137, 808, 412, 165, 97, 698, 309, 276, 670,
                             364, 939, 595, 125, 663, 384, 582, 775, 262, 978, 256, 928, 783, 275, 651, 657, 240, 759,
                             522, 354, 609, 400, 487, 57, 269, 251, 927, 953, 700, 591, 186, 287, 873, 511, 768, 269,
                             880, 767, 487, 518, 812, 434, 154, 299, 203, 664, 316, 14, 688, 350, 15, 51, 383, 550, 736,
                             903, 420, 727, 313, 789, 110, 300, 675, 435, 334, 243, 887, 503, 30, 878, 322, 859, 670,
                             77, 219, 972, 156, 539, 775, 234, 469, 887, 441, 444, 108, 688, 856, 805, 358, 634, 699,
                             855, 741, 949, 119, 996, 103, 676, 289, 382, 722, 337, 307, 301, 389, 213, 663, 131, 987,
                             573, 748, 151, 655, 117, 637, 566, 802, 226, 888, 672, 259, 740, 769, 627, 880, 709, 877,
                             995, 264, 379, 310, 485, 133, 73, 511, 50, 326, 239, 931, 187, 502, 459, 661, 263, 446,
                             370, 911, 260, 153, 89, 285, 254, 563, 293, 981, 218, 507, 304, 102, 702, 294, 335, 147,
                             242, 529, 158, 677, 617, 58, 590, 835, 734, 453, 292, 41, 285, 357, 161, 98, 166, 378, 338,
                             436, 469, 760, 448, 582, 266, 242, 356, 140, 222, 711, 879, 285, 435, 724, 631, 509, 379,
                             685, 757, 534, 787, 682, 755, 786, 978, 351, 339, 27, 282, 436, 302, 403, 396, 817, 66,
                             792, 371, 916, 858, 742, 611, 426, 123, 992, 761, 936, 206, 946, 974, 615, 158, 117, 314,
                             343, 277, 748, 545, 584, 39, 913, 319, 444, 927, 787, 880, 293, 108, 962, 706, 679, 884,
                             728, 783, 920, 994, 763, 540, 768, 545, 6, 561, 369, 608, 335, 695, 791, 271, 768, 686,
                             844, 982, 606, 23, 379, 259, 943, 956, 459, 358, 434, 606, 794, 985, 424, 939, 116, 508,
                             998, 48, 582, 927, 150, 310, 402, 764, 913, 749, 304, 446, 755, 928, 236, 572, 566, 600,
                             451, 659, 660, 651, 224, 959, 70, 449, 191, 883, 984, 396, 904, 837, 763, 475, 53, 344,
                             703, 86, 707, 528, 715, 853, 327, 447, 163, 389, 379, 497, 385, 673, 915, 407, 756, 630,
                             921, 700, 423, 546, 224, 170, 23, 595, 113, 854, 445, 397, 466, 885, 24, 854, 765, 259,
                             951, 139, 897, 629, 226, 938, 182, 963, 168, 198, 428, 613, 925, 103, 516, 491, 580, 857,
                             539, 19, 21, 426, 147, 417, 299, 785, 375, 198, 984, 480, 131, 358, 31, 925, 764, 75, 963,
                             140, 725, 681, 501, 154, 204, 626, 822, 775, 378, 396, 988, 756, 60, 598, 965, 738, 617,
                             492, 566, 264, 640, 912, 4, 554, 474, 524, 371, 730, 638, 452, 679, 776, 353, 799, 381,
                             188, 603, 328, 528, 120, 24, 835, 350, 737, 572, 759, 220, 329, 813, 93, 896, 502, 44, 351,
                             862, 825, 914, 868, 575, 911, 25, 414, 956, 566, 247, 761, 921, 901, 317, 93, 466, 719,
                             251, 9, 434, 26, 735, 754, 602, 402, 956, 702, 295, 144, 833, 564, 459, 664, 447, 791, 731,
                             325, 945, 904, 787, 704, 265, 91, 790, 587, 120, 514, 521, 325, 215, 985, 859, 861, 190,
                             721, 969, 16, 641, 638, 713, 274, 495, 272, 701, 20, 319, 933, 979, 19, 824, 753, 323, 924,
                             162, 534, 786, 18, 834, 269, 626, 800, 490, 944, 571, 782, 842, 578, 225, 264, 345, 481,
                             369, 636, 158, 390, 92, 777, 622, 662, 115, 939, 515, 692, 95, 398, 696, 146, 606, 554,
                             214, 637, 776, 996, 241, 730, 755, 596, 247, 258, 112, 703, 643, 142, 663, 729, 27, 962,
                             737, 930, 222, 199, 595, 188, 184, 287, 120, 135, 352, 625, 486, 684, 465, 261, 246, 574,
                             744, 212, 28, 266, 491, 651, 843, 652, 80, 796, 412, 545, 912, 311, 913, 447, 180, 540,
                             108, 578, 742, 216, 140, 881, 679, 767, 528, 987, 233, 241, 376, 285, 845, 722, 381, 319,
                             139, 118, 779, 727, 741, 388, 284, 677, 163, 81, 453, 612, 495, 479, 408, 493, 159, 545,
                             956, 806, 802, 269, 140, 748, 110, 734, 621, 334, 614, 395, 74, 972, 840, 118, 613, 48,
                             962, 460, 318, 278, 637, 334, 787, 766, 373, 417, 672, 430, 490, 232, 626, 745, 721, 219,
                             133, 958, 181, 875, 209, 199, 637, 886, 908, 495, 311, 547, 365, 141, 292, 233, 453, 292,
                             941, 703, 38, 487, 63, 408, 394, 876, 460, 582, 270, 553, 169, 63, 789, 753, 4, 601, 828,
                             591, 627, 886, 411, 354, 863, 758, 18, 173, 92, 147, 170, 572, 951, 727, 252, 97, 207, 742,
                             185, 906, 713, 324, 706, 129, 744, 400, 897, 201, 801, 913, 225, 937, 981, 526, 925, 655,
                             611, 901, 582, 302, 329, 98, 365, 887, 926, 829, 332, 425, 887, 188, 809, 222, 293, 552,
                             553, 604, 554, 399, 95, 442, 941, 82, 95, 250, 602, 282, 932, 953, 400, 245, 997, 456, 789,
                             783, 856, 172, 739, 323, 440, 928, 961, 161, 926, 700, 281, 28, 767, 740, 981, 798, 836,
                             655, 431, 98, 862, 28, 624, 110, 417, 446, 11, 17, 784, 757, 160, 124, 40, 655, 17, 411,
                             162, 933, 425, 890, 27, 529, 739, 398, 385, 449, 827, 688, 959, 723, 148, 916, 814, 638,
                             642, 560, 361, 134, 115, 659, 204, 376, 260, 337, 184, 413, 354, 510, 704, 325, 241, 538,
                             588, 977, 31, 936, 805, 486, 237, 546, 70, 458, 947, 150, 683, 990, 673, 57, 47, 803, 208,
                             508, 452, 396, 169, 838, 492, 706, 532, 878, 685, 200, 111, 261, 564, 403, 340, 31, 526,
                             779, 326, 329, 640, 990, 863, 334, 506, 28, 521, 489, 981, 515, 451, 803, 742, 486, 248,
                             716, 967, 622, 774, 938, 378, 180, 195, 853, 663, 699, 865, 589, 856, 27, 971, 687, 483,
                             230, 517, 845, 279, 882, 535, 166, 937, 43, 648, 756, 40, 12, 76, 338, 501, 714, 287, 973,
                             766, 47, 489, 633, 56, 248, 718, 430, 431, 237, 620, 725, 567, 648, 253, 51, 63, 382, 146,
                             28, 830, 409, 286, 628, 657, 828, 129, 256, 902, 249, 738, 84, 90, 128, 979, 864, 839, 582,
                             57, 611, 278, 534, 844, 977, 819, 98, 840, 203, 169, 461, 564, 299, 270, 282, 327, 721,
                             748, 759, 164, 883, 885, 924, 772, 622, 997, 944, 627, 821, 277, 224, 890, 680, 494, 313,
                             298, 990, 583, 790, 842, 455, 352, 966, 878, 878, 741, 765, 742, 951, 593, 828, 662, 150,
                             702, 359, 61, 394, 428, 368, 939, 948, 528, 890, 262, 432, 982, 898, 160, 822, 68, 27, 853,
                             9, 964, 208, 382, 881, 257, 653, 189, 701, 20, 861, 693, 560, 945, 225, 907, 94, 899, 489,
                             605, 788, 545, 621, 532, 222, 478, 551, 376, 16, 984, 907, 426, 548, 386, 249, 418, 298,
                             399, 60, 309, 578, 637, 443, 233, 619, 135, 415, 465, 664, 560, 42, 674, 463, 306, 573,
                             153, 593, 558, 32, 708, 910, 124, 890, 52, 296, 514, 823, 172, 459, 821, 833, 409, 460,
                             363, 745, 658, 290, 50, 607, 912, 127, 595, 563, 193, 802, 238, 439, 23, 741, 729, 793,
                             402, 325, 671, 766, 669, 517, 374, 318, 468, 489, 639, 136, 553, 31, 448, 740, 834, 114,
                             313, 879, 721, 16, 778, 503, 716, 55, 806, 14, 876, 429, 380, 223, 646, 487, 160, 922, 653,
                             159, 379, 18, 970, 68, 840, 383, 505, 776, 912, 461, 251, 707, 634, 803, 821, 47, 650, 865,
                             851, 311, 206, 449, 48, 859, 192, 337, 634, 991, 515, 78, 331, 190, 747, 210, 320, 469, 45,
                             299, 376, 491, 449, 948, 194, 579, 824, 470, 543, 632, 131, 807, 535, 824, 696, 266, 106,
                             65, 701, 90, 457, 502, 929, 745, 660, 592, 319, 280, 45, 218, 977, 853, 365, 562, 864, 890,
                             551, 788, 27, 849, 295, 29, 670, 872, 554, 77, 80, 105, 524, 11, 123, 707, 376, 269, 883,
                             316, 263, 650, 80, 590, 767, 793, 943, 948, 396, 753, 786, 227, 1, 973, 53, 984, 116, 795,
                             551, 273, 141, 288, 836, 450, 501, 459, 574, 536, 730, 398, 660, 213, 211, 501, 94, 336,
                             272, 100, 582, 356, 874, 51, 921, 745, 853, 980, 714, 360, 102, 479, 26, 988, 68, 701, 965,
                             635, 641, 95, 812, 727, 253, 464, 155, 784, 911, 997, 746, 652, 431, 402, 104, 12, 417,
                             401, 796, 71, 459, 64, 214, 834, 525, 319, 160, 718, 188, 228, 270, 309, 910, 630, 389,
                             826, 759, 680, 506, 928, 749, 58, 670, 933, 918, 84, 329, 421, 410, 860, 280, 238, 986,
                             873, 928, 120, 486, 257, 310, 579, 436, 950, 164, 143, 393, 535, 280, 187, 122, 713, 703,
                             345, 560, 913, 568, 529, 197, 172, 358, 6, 140, 781, 0, 525, 275, 755, 504, 429, 58, 8,
                             460, 444, 883, 151, 971, 992, 694, 707, 595, 745, 236, 470, 925, 527, 427, 331, 163, 903,
                             739, 455, 430, 485, 485, 60, 552, 743, 3, 771, 335, 448, 863, 675, 107, 99, 255, 105, 397,
                             702, 317, 171, 863, 497, 653, 313, 158, 668, 975, 425, 417, 981, 188, 172, 141, 946, 688,
                             276, 389, 969, 86, 198, 893, 771, 547, 153, 875, 203, 963, 463, 553, 92, 160, 348, 37, 401,
                             599, 370, 394, 537, 698, 676, 38, 927, 755, 3, 333, 814, 361, 763, 583, 974, 778, 342, 473,
                             277, 690, 34, 84, 393, 612, 178, 414, 342, 576, 628, 863, 321, 1000, 378, 977, 572, 12,
                             255, 161, 126, 970, 691, 822, 941, 999, 934, 815, 939, 409, 676, 379, 976, 664, 357, 328,
                             115, 350, 745, 739, 189, 326, 283, 90, 916, 940, 976, 41, 607, 264, 599, 341, 12, 999, 716,
                             72, 406, 984, 839, 254, 721, 150, 741, 496, 9, 626, 759, 467, 262, 595, 415, 828, 620, 47,
                             305, 446, 496, 786, 106, 564, 969, 969, 286, 174, 276, 377, 300, 512, 139, 574, 734, 804,
                             69, 459, 831, 598, 68, 453, 912, 666, 984, 571, 945, 465, 693, 582, 153, 185, 72, 503, 496,
                             170, 8, 370, 413, 10, 746, 329, 530, 89, 192, 495, 376, 251, 337, 875, 37, 460, 630, 410,
                             247, 609, 947, 623, 261, 768, 348, 278, 655, 432, 913, 349, 384, 482, 170, 822, 938, 255,
                             869, 310, 593, 869, 202, 695, 240, 232, 981, 168, 398, 911, 601, 230, 95, 156, 335, 229,
                             678, 724, 986, 277, 451, 274, 237, 509, 889, 652, 752, 543, 106, 438, 690, 574, 568, 897,
                             508, 188, 434, 800, 623, 830, 113, 774, 49, 730, 556, 763, 637, 956, 784, 341, 744, 114,
                             232, 479, 731, 320, 636, 648, 813, 48, 280, 288, 883, 867, 789, 871, 36, 972, 245, 485,
                             150, 102, 884, 700, 142, 58, 890, 757, 894, 400, 989, 679, 433, 57, 368, 209, 968, 672,
                             852, 892, 655, 442, 620, 435, 759, 202, 529, 890, 892, 989, 26, 88, 336, 728, 67, 510, 40,
                             898, 10, 172, 954, 10, 472, 11, 668, 23, 482, 177, 936, 469, 360, 393, 564, 611, 695, 912,
                             42, 708, 198, 149, 34, 90, 556, 450, 550, 101, 879, 52, 978, 134, 458, 634, 843, 385, 803,
                             263, 404, 704, 462, 529, 145, 448, 929, 363, 412, 803, 86, 212, 556, 997, 517, 230, 619,
                             258, 33, 528, 549, 653, 500, 361, 300, 393, 784, 955, 986, 970, 966, 672, 371, 87, 75, 271,
                             876, 487, 65, 870, 401, 149, 476, 5, 683, 164, 439, 761, 124, 779, 918, 788, 479, 720, 491,
                             246, 334, 623, 774, 811, 330, 14, 965, 164, 216, 565, 468, 659, 149, 395, 151, 766, 152,
                             527, 28, 486, 565, 889, 0, 119, 259, 690, 144, 771, 354, 86, 212, 428, 5, 942, 773, 957,
                             799, 631, 168, 678, 553, 468, 555, 53, 522, 859, 222, 672, 27, 379, 690, 335, 371, 10, 527,
                             430, 439, 693, 611, 210, 116, 97, 202, 174, 193, 747, 245, 135, 391, 341, 117, 508, 336,
                             97, 839, 232, 310, 796, 400, 350, 293, 489, 583, 668, 506, 910, 391, 64, 287, 341, 515,
                             467, 481, 296, 438, 694, 81, 748, 716, 978, 805, 299, 921, 789, 225, 85, 628, 118, 417,
                             838, 771, 475, 620, 589, 751, 203, 634, 815, 228, 692, 133, 689, 235, 626, 339, 569, 976,
                             272, 408, 184, 376, 610, 17, 808, 842, 480, 754, 545, 455, 520, 477, 889, 751, 806, 719,
                             651, 457, 568, 970, 541, 475, 635, 221, 169, 987, 345, 987, 817, 829, 371, 743, 218, 282,
                             244, 788, 857, 170, 297, 747, 378, 345, 220, 190, 127, 114, 152, 285, 221, 98, 236, 388,
                             421, 410, 390, 251, 43, 288, 125, 64, 586, 811, 313, 687, 528, 579, 916, 110, 187, 44, 88,
                             552, 46, 423, 152, 964, 872, 7, 999, 644, 477, 883, 319, 734, 558, 737, 835, 405, 291, 597,
                             739, 342, 150, 583, 736, 638, 836, 918, 799, 482, 417, 202, 258, 176, 562, 33, 24, 585,
                             458, 477, 407, 842, 764, 309, 606, 440, 182, 999, 375, 112, 987, 26, 825, 771, 185, 660,
                             882, 66, 907, 883, 450, 383, 501, 567, 223, 17, 227, 724, 152, 387, 368, 645, 803, 327,
                             294, 620, 861, 421, 848, 826, 119, 146, 878, 751, 928, 434, 589, 220, 356, 710, 33, 278,
                             754, 447, 365, 674, 5, 848, 424, 888, 916, 881, 186, 678, 614, 129, 207, 721, 385, 422,
                             313, 403, 970, 264, 80, 324, 456, 486, 117, 430, 308, 993, 366, 617, 104, 903, 365, 926,
                             281, 22, 902, 593, 685, 710, 923, 818, 379, 421, 3, 734, 187, 120, 22, 236, 11, 420, 366,
                             515, 199, 486, 310, 927, 261, 678, 630, 786, 954, 29, 246, 241, 502, 89, 811, 581, 459,
                             864, 193, 629, 442, 105, 78, 837, 153, 345, 377, 13, 804, 803, 596, 94, 814, 115, 31, 82,
                             51, 486, 510, 420, 352, 544, 951, 842, 479, 71, 234, 917, 70, 70, 790, 177, 921, 44, 553,
                             176, 270, 675, 797, 859, 331, 463, 94, 30, 275, 794, 440, 552, 752, 527, 8, 305, 491, 296,
                             667, 310, 272, 292, 43, 169, 987, 695, 589, 50, 219, 537, 567, 732, 716, 320, 952, 711,
                             542, 572, 813, 698, 317, 43, 315, 151, 347, 164, 691, 157, 12, 590, 728, 424, 366, 41, 904,
                             814, 161, 340, 273, 512, 131, 507, 538, 963, 866, 417, 397, 703, 767, 643, 345, 265, 378,
                             103, 828, 352, 127, 937, 764, 701, 148, 572, 279, 208, 206, 569, 861, 899, 171, 97, 462,
                             733, 490, 728, 65, 554, 23, 763, 221, 995, 32, 974, 280, 242, 410, 533, 852, 433, 745, 939,
                             914, 480, 81, 601, 370, 446, 808, 724, 321, 410, 514, 45, 987, 189, 240, 195, 886, 308,
                             431, 207, 73, 463, 650, 382, 607, 835, 633, 465, 325, 294, 794, 519, 379, 262, 290, 722,
                             982, 498, 149, 87, 467, 168, 390, 537, 896, 577, 917, 68, 319, 525, 89, 429, 329, 176, 759,
                             741, 797, 320, 871, 325, 957, 366, 39, 449, 776, 44, 974, 161, 920, 650, 400, 671, 46, 76,
                             422, 333, 134, 125, 664, 722, 837, 455, 983, 466, 326, 468, 999, 129, 749, 902, 688, 393,
                             639, 748, 127, 666, 853, 874, 779, 988, 337, 876, 384, 468, 549, 381, 29, 671, 417, 558,
                             292, 471, 454, 201, 671, 200, 208, 464, 88, 28, 761, 625, 161, 906, 865, 209, 827, 319,
                             428, 977, 993, 411, 625, 907, 85, 482, 405, 620, 495, 584, 292, 136, 726, 305, 574, 802,
                             588, 58, 382, 153, 170, 388, 210, 479, 522, 182, 1000, 323, 952, 97, 972, 164, 874, 963,
                             536, 375, 331, 216, 756, 526, 513, 110, 34, 247, 824, 356, 90, 908, 389, 217, 684, 1000,
                             320, 882, 926, 695, 634, 347, 123, 508, 893, 157, 795, 215, 147, 416, 944, 964, 157, 139,
                             509, 76, 117, 378, 990, 817, 695, 798, 235, 258, 81, 765, 357, 109, 780, 335, 30, 486, 435,
                             543, 841, 677, 918, 771, 744, 775, 522, 787, 17, 839, 837, 931, 148, 71, 36, 422, 45, 275,
                             877, 22, 218, 630, 204, 612, 972, 811, 891, 788, 556, 448, 793, 923, 179, 162, 814, 355,
                             266, 113, 763, 482, 997, 668, 739, 151, 761, 379, 636, 61, 188, 87, 774, 687, 380, 276,
                             128, 57, 640, 464, 335, 751, 34, 540, 115, 588, 412, 783, 487, 957, 634, 443, 750, 477,
                             774, 127, 779, 1, 204, 301, 909, 696, 330, 411, 733, 264, 278, 648, 243, 603, 889, 163,
                             913, 280, 498, 365, 287, 232, 127, 565, 84, 820, 853, 407, 1, 199, 178, 875, 841, 882, 865,
                             605, 969, 47, 339, 405, 263, 336, 295, 594, 113, 134, 446, 371, 28, 213, 248, 129, 309,
                             452, 472, 53, 740, 556, 573, 257, 205, 142, 1000, 101, 251, 150, 368, 632, 16, 289, 557,
                             759, 948, 280, 993, 146, 980, 149, 348, 592, 932, 953, 621, 191, 710, 311, 940, 325, 556,
                             338, 773, 1, 188, 310, 706, 325, 708, 639, 77, 959, 434, 474, 698, 980, 658, 144, 199, 316,
                             191, 800, 325, 389, 927, 587, 292, 678, 624, 401, 237, 974, 465, 105, 34, 643, 685, 260,
                             317, 320, 891, 541, 557, 661, 365, 152, 693, 160, 171, 386, 564, 986, 191, 915, 119, 3,
                             505, 5, 132, 432, 420, 49, 31, 858, 365, 670, 429, 149, 350, 208, 885, 819, 95, 676, 465,
                             625, 103, 394, 326, 645, 502, 289, 350, 454, 925, 870, 427, 510, 668, 552, 978, 551, 343,
                             5, 259, 687, 779, 447, 158, 170, 65, 50, 835, 826, 988, 93, 36, 14, 495, 904, 516, 523,
                             672, 154, 992, 884, 907, 912, 380, 354, 81, 595, 133, 120, 45, 486, 916, 884, 403, 46, 173,
                             663, 947, 359, 221, 871, 956, 51, 227, 65, 546, 878, 273, 904, 279, 655, 500, 660, 284, 75,
                             525, 921, 257, 384, 367, 504, 17, 62, 742, 92, 459, 861, 798, 242, 60, 984, 172, 235, 97,
                             528, 720, 537, 676, 942, 326, 654, 61, 782, 562, 418, 609, 259, 745, 983, 726, 457, 347,
                             957, 440, 112, 152, 888, 360, 141, 555, 423, 432, 845, 827, 140, 593, 80, 870, 95, 10, 400,
                             104, 861, 470, 405, 403, 971, 538, 972, 918, 892, 467, 173, 712, 471, 578, 408, 559, 723,
                             952, 857, 798, 987, 476, 418, 240, 959, 496, 802, 795, 835, 607, 701, 158, 816, 180, 567,
                             975, 496, 542, 876, 54, 722, 646, 418, 78, 49, 858, 191, 935, 42, 127, 222, 574, 37, 636,
                             47, 557, 535, 294, 202, 679, 930, 575, 415, 602, 71, 425, 645, 132, 421, 363, 889, 719, 32,
                             23, 415, 477, 107, 357, 495, 552, 3, 501, 986, 766, 985, 556, 353, 963, 464, 867, 728, 669,
                             637, 309, 575, 500, 666, 967, 842, 135, 270, 176, 831, 683, 283, 700, 897, 127, 927, 116,
                             61, 934, 874, 403, 405, 483, 73, 662, 365, 997, 114, 160, 859, 537, 687, 23, 685, 329, 589,
                             483, 318, 602, 420, 265, 589, 406, 899, 881, 201, 931, 848, 144, 524, 345, 61, 102, 216,
                             928, 832, 269, 387, 549, 866, 552, 803, 367, 676, 877, 175, 304, 701, 395, 918, 886, 909,
                             949, 593, 497, 689, 619, 830, 868, 599, 559, 564, 597, 944, 19, 810, 773, 370, 932, 84,
                             755, 342, 814, 840, 569, 273, 685, 129, 685, 756, 305, 709, 506, 679, 724, 783, 47, 607,
                             197, 869, 318, 43, 409, 41, 773, 153, 560, 589, 655, 184, 764, 936, 976, 259, 545, 660,
                             597, 302, 294, 582, 791, 1000, 806, 497, 999, 575, 88, 506, 401, 996, 488, 108, 530, 515,
                             661, 426, 280, 626, 591, 1000, 531, 884, 620, 523, 566, 74, 775, 871, 167, 163, 275, 385,
                             451, 407, 511, 2, 471, 628, 265, 757, 523, 77, 532, 731, 671, 61, 821, 17, 491, 292, 279,
                             326, 678, 275, 413, 647, 156, 935, 554, 465, 442, 692, 469, 645, 175, 48, 852, 694, 283,
                             997, 400, 282, 574, 381, 149, 471, 196, 701, 730, 339, 767, 459, 779, 997, 641, 691, 908,
                             255, 268, 880, 788, 89, 467, 840, 571, 424, 373, 75, 930, 435, 20, 331, 833, 118, 540, 434,
                             452, 297, 129, 384, 852, 946, 265, 362, 459, 240, 658, 438, 608, 856, 448, 540, 587, 973,
                             91, 675, 44, 132, 297, 721, 545, 351, 298, 605, 801, 127, 31, 178, 872, 51, 65, 867, 981,
                             723, 823, 374, 506, 948, 759, 795, 328, 803, 416, 98, 91, 498, 224, 528, 402, 48, 413, 461,
                             391, 71, 518, 595, 658, 846, 123, 7, 979, 848, 69, 797, 425, 12, 183, 778, 493, 364, 479,
                             35, 132, 513, 938, 554, 802, 765, 181, 644, 336, 484, 932, 264, 940, 42, 484, 661, 348,
                             354, 410, 191, 219, 7, 639, 487, 68, 725, 822, 565, 297, 221, 699, 572, 339, 366, 540, 576,
                             147, 622, 554, 274, 281, 544, 774, 762, 538, 270, 61, 690, 274, 582, 637, 885, 721, 864,
                             239, 646, 386, 746, 276, 473, 777, 658, 881, 97, 529, 975, 736, 29, 897, 620, 151, 564,
                             384, 344, 371, 823, 470, 494, 751, 488, 591, 762, 606, 731, 985, 398, 16, 855, 271, 860,
                             26, 458, 986, 542, 621, 585, 752, 599, 725, 516, 206, 64, 235, 48, 374, 357, 551, 17, 159,
                             708, 275, 340, 845, 519, 743, 84, 385, 587, 623, 7, 148, 157, 361, 65, 435, 47, 49, 118,
                             254, 536, 274, 92, 800, 185, 873, 920, 979, 436, 549, 807, 85, 346, 637, 183, 259, 962,
                             941, 948, 211, 710, 275, 448, 947, 796, 604, 578, 596, 547, 296, 272, 665, 90, 933, 157,
                             663, 839, 189, 919, 613, 605, 868, 10, 913, 449, 85, 534, 924, 28, 883, 427, 979, 100, 948,
                             282, 1, 368, 988, 716, 136, 406, 746, 766, 122, 899, 135, 782, 778, 884, 323, 18, 480, 627,
                             789, 366, 141, 180, 440, 44, 907, 53, 975, 260, 997, 393, 621, 405, 112, 14, 423, 152, 582,
                             324, 708, 42, 362, 395, 106, 923, 37, 494, 551, 73, 726, 471, 941, 796, 507, 8, 117, 293,
                             489, 880, 177, 48, 760, 994, 875, 844, 469, 653, 101, 814, 544, 58, 771, 890, 781, 298,
                             745, 119, 798, 952, 152, 12, 174, 907, 113, 191, 12, 305, 233, 753, 778, 439, 724, 119,
                             719, 554, 870, 189, 510, 121, 173, 539, 788, 609, 261, 199, 187, 725, 91, 867, 561, 914,
                             95, 488, 924, 179, 898, 262, 117, 866, 265, 213, 903, 444, 754, 657, 173, 144, 262, 642,
                             523, 927, 632, 121, 68, 128, 717, 107, 37, 922, 667, 579, 347, 313, 586, 485, 410, 7, 130,
                             754, 755, 22, 605, 787, 11, 193, 701, 15, 114, 580, 86, 88, 417, 826, 461, 915, 321, 974,
                             421, 521, 285, 957, 786, 802, 66, 28, 117, 904, 258, 996, 337, 441, 717, 188, 318, 127,
                             480, 280, 953, 953, 889, 541, 288, 109, 809, 181, 926, 888, 111, 303, 414, 263, 94, 326,
                             642, 416, 987, 742, 24, 35, 950, 888, 55, 165, 903, 169, 690, 986, 175, 938, 623, 734, 212,
                             824, 108, 597, 181, 168, 858, 471, 745, 226, 467, 427, 226, 143, 552, 62, 255, 350, 280,
                             554, 158, 335, 685, 588, 827, 484, 882, 196, 170, 318, 264, 212, 687, 369, 548, 550, 112,
                             895, 599, 676, 605, 105, 862, 934, 688, 729, 949, 843, 806, 341, 523, 168, 576, 455, 204,
                             709, 648, 999, 78, 662, 712, 712, 969, 206, 43, 559, 636, 705, 699, 761, 571, 703, 823,
                             377, 359, 429, 161, 498, 18, 933, 990, 450, 653, 771, 510, 146, 88, 90, 859, 657, 525, 78,
                             886, 852, 610, 353, 586, 207, 898, 140, 823, 470, 63, 458, 747, 221, 585, 169, 879, 699,
                             794, 592, 529, 495, 370, 857, 419, 796, 913, 416, 360, 535, 170, 726, 743, 195, 912, 971,
                             937, 649, 880, 766, 301, 481, 484, 868, 163, 194, 790, 345, 210, 30, 342, 556, 714, 512,
                             398, 297, 912, 121, 856, 832, 858, 19, 454, 532, 531, 672, 438, 366, 500, 234, 672, 977,
                             417, 629, 87, 171, 512, 53, 968, 782, 517, 99, 352, 475, 128, 6, 439, 115, 388, 535, 815,
                             547, 188, 982, 179, 761, 778, 58, 296, 623, 692, 563, 820, 481, 410, 581, 147, 784, 315,
                             774, 857, 549, 828, 659, 959, 798, 956, 888, 345, 736, 630, 433, 611, 853, 828, 726, 614,
                             942, 988, 184, 289, 494, 36, 37, 790, 470, 896, 842, 800, 803, 648, 180, 944, 906, 867,
                             696, 47, 948, 647, 40, 842, 555, 676, 38, 651, 389, 659, 518, 655, 12, 278, 980, 380, 694,
                             930, 619, 867, 854, 710, 279, 113, 768, 557, 827, 914, 317, 301, 53, 832, 665, 222, 229,
                             672, 182, 514, 586, 938, 177, 608, 287, 243, 281, 236, 956, 86, 247, 744, 416, 387, 871,
                             909, 594, 673, 377, 366, 765, 839, 244, 588, 502, 724, 930, 280, 185, 743, 64, 648, 527,
                             15, 116, 517, 876, 370, 246, 347, 441, 546, 283, 95, 304, 849, 574, 125, 116, 13, 295, 198,
                             546, 460, 335, 680, 616, 670, 53, 551, 978, 806, 775, 565, 169, 719, 291, 64, 31, 780, 706,
                             702, 164, 397, 330, 426, 708, 773, 583, 465, 258, 673, 958, 681, 389, 986, 863, 823, 435,
                             406, 961, 454, 107, 799, 615, 318, 884, 52, 705, 65, 845, 484, 579, 246, 363, 46, 286, 217,
                             190, 262, 138, 260, 181, 307, 733, 469, 754, 12, 417, 854, 315, 268, 171, 145, 837, 667,
                             600, 83, 222, 537, 913, 962, 817, 419, 184, 537, 611, 972, 972, 886, 593, 791, 253, 239,
                             377, 37, 967, 301, 661, 608, 122, 177, 33, 368, 577, 543, 221, 319, 624, 673, 919, 879, 27,
                             609, 618, 742, 860, 682, 702, 115, 589, 642, 140, 102, 869, 522, 440, 927, 440, 284, 942,
                             307, 631, 294, 771, 234, 913, 447, 708, 603, 68, 601, 683, 842, 210, 292, 711, 322, 647,
                             246, 749, 159, 799, 385, 393, 857, 630, 36, 542, 523, 992, 421, 406, 5, 835, 396, 535, 708,
                             659, 816, 943, 760, 773, 162, 587, 913, 957, 383, 972, 138, 929, 644, 348, 63, 708, 596,
                             142, 277, 395, 361, 524, 876, 647, 413, 717, 241, 527, 287, 338, 662, 441, 546, 274, 39,
                             404, 806, 598, 23, 638, 180, 725, 497, 462, 180, 332, 444, 998, 205, 108, 6, 898, 203, 226,
                             832, 93, 478, 142, 152, 747, 476, 374, 783, 239, 123, 888, 553, 40, 158, 940, 720, 676,
                             855, 520, 415, 188, 91, 91, 242, 573, 292, 372, 9, 441, 790, 605, 39, 505, 476, 657, 836,
                             252, 504, 397, 303, 731, 723, 115, 181, 903, 802, 657, 746, 821, 40, 982, 549, 898, 859,
                             459, 573, 772, 165, 436, 196, 958, 706, 860, 201, 371, 428, 331, 220, 117, 765, 753, 271,
                             84, 544, 226, 700, 22, 926, 180, 96, 829, 515, 315, 706, 547, 243, 46, 396, 315, 652, 776,
                             895, 989, 65, 582, 901, 282, 684, 676, 915, 882, 653, 539, 969, 693, 1, 651, 244, 500, 65,
                             49, 830, 988, 250, 974, 352, 904, 422, 182, 530, 568, 152, 345, 657, 777, 920, 927, 18,
                             672, 974, 273, 923, 181, 171, 673, 35, 62, 648, 169, 691, 409, 283, 508, 554, 764, 408,
                             478, 200, 623, 241, 940, 113, 579, 284, 854, 493, 231, 779, 435, 237, 194, 692, 444, 538,
                             726, 728, 511, 108, 115, 869, 922, 98, 294, 311, 703, 723, 800, 286, 970, 994, 434, 973,
                             980, 704, 746, 283, 824, 26, 780, 463, 446, 407, 761, 178, 887, 375, 256, 290, 624, 243,
                             327, 398, 390, 482, 227, 660, 482, 816, 254, 951, 82, 235, 860, 5, 545, 121, 882, 766, 513,
                             399, 79, 675, 433, 738, 924, 149, 68, 878, 71, 597, 680, 648, 664, 390, 736, 979, 834, 45,
                             465, 724, 851, 567, 732, 182, 958, 530, 302, 435, 102, 944, 989, 366, 832, 632, 76, 93,
                             252, 2, 244, 945, 522, 336, 751, 230, 415, 331, 855, 506, 726, 496, 663, 662, 862, 447,
                             417, 272, 486, 63, 280, 618, 686, 713, 468, 723, 512, 78, 119, 338, 665, 278, 634, 186,
                             506, 896, 345, 281, 124, 826, 217, 494, 652, 982, 418, 825, 918, 714, 299, 308, 800, 260,
                             793, 365, 989, 873, 396, 110, 576, 533, 690, 734, 635, 235, 743, 356, 792, 508, 313, 866,
                             512, 888, 827, 127, 727, 805, 711, 826, 134, 64, 729, 623, 79, 313, 776, 245, 896, 43, 669,
                             143, 935, 450, 463, 967, 337, 242, 169, 849, 755, 262, 790, 661, 165, 863, 744, 797, 979,
                             86, 432, 67, 202, 813, 244, 112, 54, 844, 327, 106, 708, 892, 535, 667, 870, 740, 150, 695,
                             329, 987, 39, 168, 54, 553, 192, 581, 478, 324, 569, 145, 536, 911, 549, 880, 884, 994,
                             367, 997, 138, 606, 236, 547, 452, 250, 683, 23, 596, 172, 598, 865, 972, 528, 243, 442,
                             560, 342, 840, 643, 221, 174, 282, 746, 779, 686, 709, 657, 623, 258, 770, 793, 364, 770,
                             9, 456, 459, 623, 739, 524, 209, 997, 974, 386, 635, 547, 790, 849, 703, 489, 493, 132,
                             132, 389, 869, 727, 405, 182, 25, 887, 361, 447, 483, 483, 226, 94, 408, 938, 89, 546, 296,
                             497, 551, 704, 152, 816, 955, 674, 856, 594, 598, 711, 766, 336, 852, 258, 653, 849, 322,
                             209, 895, 596, 684, 286, 12, 547, 392, 263, 60, 548, 772, 562, 391, 772, 757, 994, 656,
                             468, 520, 667, 329, 600, 612, 222, 528, 601, 721, 832, 954, 918, 33, 381, 9, 27, 95, 328,
                             623, 163, 783, 854, 313, 635, 943, 25, 619, 121, 676, 993, 115, 614, 651, 76, 157, 744,
                             834, 190, 298, 127, 66, 733, 949, 616, 750, 598, 313, 968, 784, 884, 653, 111, 108, 833,
                             995, 981, 661, 856, 506, 276, 519, 345, 801, 822, 818, 17, 921, 691, 225, 688, 952, 915,
                             50, 532, 401, 412, 258, 193, 752, 757, 890, 714, 156, 157, 20, 371, 43, 723, 426, 976, 725,
                             54, 212, 132, 251, 288, 33, 237, 944, 945, 451, 105, 595, 937, 120, 896, 372, 367, 300,
                             251, 760, 366, 907, 390, 977, 518, 527, 724, 749, 593, 984, 450, 206, 31, 70, 734, 543,
                             986, 944, 965, 180, 8, 933, 148, 936, 84, 441, 557, 167, 689, 412, 378, 642, 29, 179, 324,
                             209, 9, 955, 750, 486, 719, 784, 147, 200, 791, 484, 292, 337, 925, 882, 179, 347, 694,
                             656, 5, 420, 135, 23, 825, 627, 884, 943, 627, 41, 412, 664, 32, 190, 150, 89, 914, 961,
                             952, 906, 453, 568, 348, 840, 296, 632, 672, 164, 209, 77, 743, 994, 965, 787, 616, 288,
                             58, 722, 459, 400, 361, 800, 210, 680, 885, 707, 361, 966, 843, 703, 679, 469, 883, 627,
                             927, 391, 66, 896, 668, 569, 675, 151, 706, 446, 194, 11, 562, 85, 621, 335, 170, 548, 438,
                             455, 821, 363, 861, 466, 673, 560, 430, 737, 216, 403, 401, 895, 559, 589, 434, 561, 188,
                             313, 846, 36, 956, 119, 161, 90, 353, 594, 530, 204, 544, 652, 433, 625, 270, 886, 802,
                             207, 437, 438, 918, 406, 710, 308, 463, 68, 856, 560, 26, 399, 238, 302, 324, 405, 794,
                             488, 194, 737, 711, 409, 451, 920, 599, 184, 693, 165, 153, 76, 501, 139, 583, 646, 845,
                             347, 262, 72, 246, 645, 541, 135, 385, 251, 632, 983, 474, 342, 188, 500, 155, 927, 21,
                             743, 268, 354, 694, 904, 992, 520, 175, 697, 363, 647, 2, 692, 308, 355, 721, 161, 590,
                             104, 497, 305, 177, 493, 531, 486, 918, 634, 821, 46, 952, 313, 843, 915, 376, 478, 325,
                             19, 399, 541, 425, 561, 381, 885, 836, 143, 582, 174, 868, 406, 608, 813, 951, 122, 812,
                             269, 816, 88, 220, 847, 94, 754, 265, 169, 413, 12, 728, 327, 118, 832, 499, 369, 285, 944,
                             246, 953, 182, 205, 357, 463, 884, 142, 220, 32, 639, 84, 902, 275, 827, 389, 828, 982,
                             913, 554, 105, 849, 226, 45, 154, 239, 856, 526, 359, 730, 180, 344, 541, 478, 354, 990,
                             991, 636, 1000, 519, 390, 130, 399, 857, 223, 111, 231, 449, 707, 945, 820, 721, 222, 690,
                             9, 712, 962, 7, 940, 962, 679, 121, 15, 787, 398, 329, 960, 501, 26, 539, 288, 187, 900,
                             200, 414, 338, 399, 513, 602, 661, 459, 460, 198, 815, 53, 161, 891, 264, 412, 989, 646,
                             248, 704, 383, 646, 88, 199, 297, 443, 32, 100, 66, 689, 463, 958, 325, 788, 981, 247, 172,
                             96, 477, 456, 142, 92, 288, 231, 429, 325, 73, 422, 977, 807, 504, 572, 285, 719, 977, 54,
                             806, 118, 455, 532, 479, 50, 343, 871, 333, 561, 472, 995, 197, 609, 314, 936, 440, 102,
                             815, 853, 911, 716, 260, 679, 740, 384, 46, 226, 590, 383, 100, 283, 935, 104, 876, 896,
                             507, 901, 281, 807, 679, 963, 877, 198, 234, 655, 474, 723, 975, 265, 540, 729, 108, 685,
                             404, 460, 635, 237, 788, 488, 344, 665, 704, 644, 65, 56, 989, 131, 115, 769, 350, 738,
                             982, 580, 641, 883, 545, 328, 290, 290, 684, 313, 413, 198, 73, 395, 656, 428, 692, 236,
                             919, 983, 649, 429, 875, 319, 819, 740, 680, 816, 781, 60, 569, 509, 938, 566, 614, 551,
                             560, 881, 716, 601, 5, 540, 826, 78, 86, 635, 438, 124, 0, 867, 59, 561, 837, 870, 420,
                             326, 948, 748, 592, 168, 967, 894, 753, 148, 202, 689, 21, 336, 350, 726, 804, 301, 699,
                             898, 111, 817, 229, 549, 873, 362, 475, 518, 579, 529, 4, 800, 763, 489, 929, 936, 300,
                             759, 981, 145, 290, 324, 352, 0, 498, 350, 215, 592, 806, 963, 299, 400, 422, 642, 672,
                             211, 561, 20, 945, 398, 715, 23, 6, 548, 121, 851, 326, 292, 180, 648, 400, 120, 386, 473,
                             53, 213, 835, 469, 70, 610, 300, 625, 632, 771, 312, 379, 599, 837, 653, 422, 888, 155,
                             387, 620, 235, 426, 840, 760, 162, 136, 793, 509, 562, 562, 62, 409, 857, 559, 746, 922,
                             936, 553, 41, 396, 609, 681, 5, 680, 984, 128, 257, 335, 160, 271, 105, 767, 258, 609, 425,
                             699, 505, 274, 640, 293, 841, 297, 849, 31, 12, 462, 395, 712, 117, 341, 326, 390, 887,
                             921, 421, 513, 230, 554, 834, 307, 436, 611, 204, 580, 794, 222, 733, 734, 145, 102, 861,
                             776, 131, 214, 440, 755, 515, 671, 590, 305, 768, 118, 670, 884, 506, 12, 597, 170, 960,
                             657, 353, 188, 19, 638, 432, 674, 414, 880, 353, 395, 37, 722, 830, 919, 808, 117, 390,
                             316, 178, 840, 489, 268, 377, 479, 933, 246, 547, 887, 73, 729, 54, 686, 818, 386, 662,
                             683, 91, 223, 274, 28, 880, 526, 329, 762, 212, 886, 121, 510, 857, 965, 653, 932, 632,
                             799, 486, 898, 516, 349, 846, 733, 28, 629, 776, 776, 173, 817, 127, 672, 875, 930, 330,
                             236, 912, 137, 97, 771, 824, 657, 477, 835, 988, 136, 408, 835, 174, 705, 726, 296, 70,
                             720, 403, 321, 360, 170, 200, 808, 642, 993, 322, 299, 238, 549, 868, 954, 664, 765, 590,
                             715, 221, 628, 538, 631, 572, 40, 950, 284, 275, 528, 828, 11, 426, 155, 730, 847, 18, 267,
                             831, 243, 602, 947, 559, 853, 391, 308, 603, 446, 792, 620, 877, 9, 720, 668, 818, 91, 459,
                             390, 812, 777, 410, 64, 92, 251, 613, 654, 164, 688, 400, 776, 189, 694, 700, 553, 853,
                             988, 708, 776, 214, 590, 293, 320, 597, 515, 358, 893, 822, 704, 254, 281, 802, 351, 209,
                             933, 407, 299, 739, 474, 142, 76, 206, 55, 270, 457, 522, 355, 542, 418, 321, 283, 234,
                             893, 479, 337, 806, 686, 597, 623, 421, 360, 373, 45, 834, 885, 6, 253, 684, 794, 942, 51,
                             613, 176, 488, 830, 902, 400, 704, 427, 271, 335, 840, 838, 933, 528, 623, 278, 882, 584,
                             794, 51]
        max_profit = self.solution.maxProfitklimitedTransaction_op(1000000000, stock_price_array)
        self.assertEqual(1648961, max_profit)

    def test_maxProfitWithCooldown(self):
        stock_price_array = [1, 2, 3, 0, 2]
        max_profit = self.solution.maxProfitWithCooldown(stock_price_array)
        self.assertEqual(3, max_profit)

    def test_maxProfitWithCooldown_empty(self):
        stock_price_array = []
        max_profit = self.solution.maxProfitWithCooldown(stock_price_array)
        self.assertEqual(0, max_profit)

    def test_maxProfitWithCooldown_none(self):
        max_profit = self.solution.maxProfitWithCooldown(None)
        self.assertEqual(0, max_profit)

    def test_maxProfitWithTransactionFee(self):
        stock_price_array = [1, 3, 2, 8, 4, 9]
        max_profit = self.solution.maxProfitWithTransactionFee(stock_price_array, 2)
        self.assertEqual(8, max_profit)

    def test_maxProfitWithTransactionFeeDescend(self):
        stock_price_array = [5, 4, 3, 2, 1]
        max_profit = self.solution.maxProfitWithTransactionFee(stock_price_array, 2)
        self.assertEqual(0, max_profit)

    def test_maxProfitWithTransactionFee_empty(self):
        stock_price_array = []
        max_profit = self.solution.maxProfitWithTransactionFee(stock_price_array, 2)
        self.assertEqual(0, max_profit)

    def test_maxProfitWithTransactionFee_none(self):
        max_profit = self.solution.maxProfitWithTransactionFee(None, 2)
        self.assertEqual(0, max_profit)

    def test_maxProfitWithTransactionFee_negative_fee(self):
        stock_price_array = [1, 3, 2, 8, 4, 9]
        max_profit = self.solution.maxProfitWithTransactionFee(stock_price_array, -2)
        self.assertEqual(0, max_profit)

    def test_minDistance(self):
        __min_edit_distance = self.solution.minDistance('horse', 'ros')
        self.assertEqual(3, __min_edit_distance)

    def test_minDistance1(self):
        __min_edit_distance = self.solution.minDistance('intention', 'execution')
        self.assertEqual(5, __min_edit_distance)

    def test_minDistance2(self):
        __min_edit_distance = self.solution.minDistance('intention', 'nation')
        self.assertEqual(4, __min_edit_distance)

    def test_superEggDrop(self):
        certainty_min_move = self.solution.superEggDrop(1, 2)
        self.assertEqual(2, certainty_min_move)

    def test_superEggDrop1(self):
        certainty_min_move = self.solution.superEggDrop(2, 6)
        self.assertEqual(3, certainty_min_move)

    def test_superEggDrop2(self):
        certainty_min_move = self.solution.superEggDrop(3, 14)
        self.assertEqual(4, certainty_min_move)

    def test_superEggDrop3(self):
        certainty_min_move = self.solution.superEggDrop(2, 100)
        self.assertEqual(14, certainty_min_move)
