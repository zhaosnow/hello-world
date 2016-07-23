class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0:
            return [0]
        if n == 1:
            return [0, 1]
        subans = self.grayCode(n - 1)
        mask = 1 << (n - 1)
        ans = list()
        for num in subans:
            ans.append(num)
        for i in range(len(subans) - 1, -1, -1):
            ans.append(subans[i] | mask)
        return ans
