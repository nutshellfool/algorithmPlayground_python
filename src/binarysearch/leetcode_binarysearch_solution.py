# -*- coding: utf-8 -*-


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)
        if n > 0:
            return self.myPow(x * x, n // 2) * x if n & 1 else self.myPow(x * x, n // 2)

    def myPow_iteration(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        pow = 1.0

        while n:
            if n & 1:
                pow *= x
            x *= x
            n //= 2

        return pow

    def myPow_lazy(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x ** n

    def myPow_instinct(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        result = 1
        if n > 0:
            for i in range(n):
                result *= x
        else:
            for i in range(-n):
                result *= 1.0 / x

        return result
