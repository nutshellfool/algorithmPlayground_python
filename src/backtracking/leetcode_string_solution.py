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
            self.__generate_parenthesis(n, left + 1, right, string_item + "(", results)
        if right < n and right < left:
            self.__generate_parenthesis(n, left, right + 1, string_item + ")", results)

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
