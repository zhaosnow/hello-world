class Solution(object):
    def __init__(self):
        self.d = dict()
        
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.solve(n)
        
    def solve(self, n):
        if n <= 2:
            return max(n, 1)
        else:
            if n in self.d:
                return self.d[n]
            ans = 0
            for i in range(1, n + 1):
                ans += self.solve(i - 1) * self.solve(n - i)
            self.d[n] = ans
            return ans
