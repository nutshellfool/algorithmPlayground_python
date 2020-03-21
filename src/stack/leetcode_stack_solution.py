# -*- coding: utf-8 -*-
from collections import deque


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        stack = deque()
        map = {')': '(', '}': '{', ']': '['}
        for i, v in enumerate(s):
            if v in map:
                if stack and stack.pop() != map[v]:
                    return False
            else:
                stack.append(v)

        return not stack

    def is_valid_instinct(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        stack = deque()
        for i, v in enumerate(s):
            if v == '(':
                stack.append(')')
            elif v == '{':
                stack.append('}')
            elif v == '[':
                stack.append(']')
            else:
                if len(stack) != 0 and stack.pop() != v:
                    return False

        return len(stack) == 0
