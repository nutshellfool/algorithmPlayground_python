# -*- coding: utf-8 -*-


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 0:
            return None
        result_list = []
        self.__generate_parenthesis(n, 0, 0, "", result_list)
        return result_list

    def __generate_parenthesis(self, n, left, right, string_item, results):
        if left == n and right == n:
            results.append(string_item)
        if left < n:
            self.__generate_parenthesis(n, left + 1, right, string_item + "(",
                                        results)
        if right < n and right < left:
            self.__generate_parenthesis(n, left, right + 1, string_item + ")",
                                        results)

    def generateParenthesis_instinct(self, n):
        def generate(result_str_list, string_list=None):
            if string_list is None:
                string_list = []
            if len(string_list) == 2 * n:
                if __valid_parenthesis(string_list):
                    result_str_list.append("".join(string_list))
            else:
                string_list.append("(")
                generate(result_str_list, string_list)
                string_list.pop()
                string_list.append(")")
                generate(result_str_list, string_list)
                string_list.pop()

        def __valid_parenthesis(parenthesis_list):
            bal = 0
            for char in parenthesis_list:
                if char == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        if n < 0:
            return None
        if n == 0:
            return [""]

        result = []
        generate(result)
        return result

    # def combine(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: List[List[int]]
    #     """
    #     if n < 0 or k < 0:
    #         return None
    #     if k == 0 or n == 0:
    #         return [[]]
    #
    #     return [pre + [i] for i in range(k, n + 1) for pre in
    #             self.combine(i - 1, k - 1)]

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 0 or k < 0:
            return None
        if k == 0 or n == 0:
            return [[]]

        return [pre + [i] for i in range(k, n + 1) for pre in
                self.combine(i - 1, k - 1)]

    @staticmethod
    def combine_backtrace(n, k):
        def combine_intern(result_list, item_list, start_index, n_size,
                           k_size):
            if len(item_list) == k_size:
                import copy
                result_list.append(copy.deepcopy(item_list))
                return
            for i in range(start_index,
                           n_size - (k_size - len(item_list)) + 1 + 1):
                item_list.append(i)
                combine_intern(result_list, item_list, i + 1, n_size, k_size)
                del item_list[-1]

        if n < 0 or k < 0:
            return None
        if k == 0 or n == 0:
            return [[]]
        combines = []
        intern_item_list = []
        combine_intern(combines, intern_item_list, 1, n, k)
        return combines

    @staticmethod
    def combine_instinct(n, k):
        if n < 0 or k < 0:
            return None
        if k == 0 or n == 0:
            return [[]]
        from itertools import combinations
        combine_list = list(combinations(range(1, n + 1), k))
        return map(list, combine_list)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        steps = []
        result = []
        self._subsets(nums, 0, steps, result)
        return result

    def _subsets(self, nums, start, steps, result):
        import copy
        result.append(copy.deepcopy(steps))

        for i in range(start, len(nums)):
            steps.append(nums[i])
            self._subsets(nums, i + 1, steps, result)
            del steps[-1]

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums.sort()
        steps = []
        result = []
        self._subsetsWithDup(nums, 0, steps, result)
        return result

    def _subsetsWithDup(self, nums, start, steps, result):
        import copy
        result.append(copy.deepcopy(steps))

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            steps.append(nums[i])
            self._subsetsWithDup(nums, i + 1, steps, result)
            del steps[-1]

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) > 12:
            return []

        result = []
        self._backtracking(s, 0, 4, "", result)
        return result

    def _backtracking(self, s, start, left_part_count, digital_part_str,
                      result):
        if left_part_count == 0 and start == len(s):
            result.append(digital_part_str[:-1])

        for i in range(1, 4):
            if len(s) - start - i >= 0:
                segment = s[start: start + i]
                if self._is_valid_ip_address_part(segment):
                    self._backtracking(s, start + i, left_part_count - 1,
                                       digital_part_str + segment + '.',
                                       result)

    def _is_valid_ip_address_part(self, part_str):
        if not part_str or (len(part_str) > 1 and part_str[0] == '0'):
            return False
        return 0 <= int(part_str) <= 255

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        row, col = len(board), len(board[0])

        visited = [[False for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if (self._exist(board, i, j, word, 0, visited)):
                    return True

        return False

    def _exist(self, board, row_index, col_index, word, word_index, visited):
        DX = [0, 1, 0, -1]
        DY = [1, 0, -1, 0]
        if row_index < 0 or row_index >= len(
                board) or col_index < 0 or col_index >= len(board[0]):
            return False
        if visited[row_index][col_index] or board[row_index][col_index] != \
                word[word_index]:
            return False

        if word_index == len(word) - 1:
            return True

        visited[row_index][col_index] = True
        existed = False
        for direction_index in range(4):
            existed |= self._exist(board, row_index + DX[direction_index],
                                   col_index + DY[direction_index], word,
                                   word_index + 1, visited)
        if not existed:
            visited[row_index][col_index] = False
        return existed

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        _digital_lettersmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        _result = []
        self._letter_comnination_backtracking('', digits, _digital_lettersmap,
                                              _result)
        return _result

    def _letter_comnination_backtracking(self, combination, next_digits,
                                         digital_map, result):
        if len(next_digits) == 0:
            result.append(combination)
            return
        letters = digital_map.get(next_digits[0])
        for i in range(len(letters)):
            letter = letters[i: i + 1]
            self._letter_comnination_backtracking(combination + letter,
                                                  next_digits[1:], digital_map,
                                                  result)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        steps = []
        result = []
        self._combination_sum_backtrack(candidates, 0, target, steps, result)
        return result

    def _combination_sum_backtrack(self, candidates, start, remain, step,
                                   result):
        if remain < 0:
            return
        if remain == 0:
            import copy
            result.append(copy.deepcopy(step))

        for i in range(start, len(candidates)):
            step.append(candidates[i])
            self._combination_sum_backtrack(candidates, i,
                                            remain - candidates[i], step,
                                            result)
            step.remove(candidates[i])

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        step, result = [], []
        self._combination_sum2_backtracking(candidates, 0, target, step,
                                            result)

        return result

    def _combination_sum2_backtracking(self, candidates, start, remain, step,
                                       result):
        if remain < 0:
            return
        if remain == 0:
            import copy
            result.append(copy.deepcopy(step))
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            step.append(candidates[i])
            self._combination_sum2_backtracking(candidates, i + 1,
                                                remain - candidates[i], step,
                                                result)
            step.remove(candidates[i])

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        steps, result = [], []
        self._permute_backtracking(nums, steps, result)
        return result

    def _permute_backtracking(self, nums, steps, result):
        if len(steps) == len(nums):
            import copy
            result.append(copy.deepcopy(steps))
            return

        for i in range(len(nums)):
            if nums[i] in steps:
                continue
            steps.append(nums[i])
            self._permute_backtracking(nums, steps, result)
            del steps[-1]
