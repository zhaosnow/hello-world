"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

Show Hint 

"""
class Solution(object):
    def __init__(self):
        self.visited = dict()
        
    def integerBreak(self, n): # 解法相当于一次记忆化搜索
        """
        :type n: int
        :rtype: int
        """
        if n in self.visited:
            return self.visited[n]
        if n == 2 or n == 1:
            return 1
        ans = n - 1
        for i in range(1, n):
            ans = max([ans, self.integerBreak(n - i) * i, i * (n - i)]) # 下一个数字是否需要分解, 分两种情况
        self.visited[n] = ans
        return ans
