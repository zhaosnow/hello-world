class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        layer = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    layer[j] = 1
                else:
                    layer[j] += layer[j-1]
        return layer[-1]
