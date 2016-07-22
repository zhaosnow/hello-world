class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime = [True] * (n + 1)
        for i in range(2, n + 1):
            if is_prime[i]:
                j = i * 2
                while j <= n:
                    is_prime[j] = False
                    j += i
        ans = 0
        for i in range(2, n):
            if is_prime[i]:
                ans += 1
        return ans
