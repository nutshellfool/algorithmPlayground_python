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

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r

    def mySqrt_instinct(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        for i in xrange(x):
            if i ** 2 == x:
                return i
            if i ** 2 > x:
                return i - 1

        return -1

    def mySqrtx(self, x, delta):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        r = x
        while True:
            if abs(r ** 2 - x) <= delta:
                break
            r = (r + x / r) / 2.0

        return r

    def mySqrtx_instinct(self, x, delta):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) / 2.0
            if abs(x - mid ** 2) <= delta:
                return mid
            elif x / mid > mid:
                left = mid
            else:
                right = mid

        return -1.0

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None

        is_negative = (dividend > 0 > divisor) or (dividend < 0 < divisor)
        result = 0
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        while dividend_abs >= divisor_abs:
            shift = 0
            while dividend_abs >= divisor_abs << shift:
                shift += 1
            dividend_abs = dividend_abs - (divisor_abs << (shift - 1))
            result = result + (1 << (shift - 1))

        return -result if is_negative else result

    def divide_instinct(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None

        is_negative = (dividend > 0 > divisor) or (dividend < 0 < divisor)
        result = 0
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        add_times = 0
        while dividend_abs >= divisor_abs:
            divisor_abs_sum = 0
            for i in xrange(add_times):
                divisor_abs_sum += divisor_abs

            if divisor_abs_sum == dividend_abs:
                result = add_times
                break
            elif divisor_abs_sum < dividend_abs:
                add_times += 1
            else:
                add_times -= 1
                result = add_times
                break

        return -result if is_negative else result
