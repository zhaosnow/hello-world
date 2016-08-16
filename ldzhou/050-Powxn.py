class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            if n < 0:
                x = 1 / x
            n = abs(n)
            factor = 1
            ans = x
            while (factor << 1) < n:
                factor <<= 1
                ans **= 2
            ans *= self.myPow(x, n - factor)
            return ans
