class Solution(object):
    nums = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = self.nums
        while len(nums) <= n:
            nums += min(nums[-i*i] for i in range(1, int(len(nums)**0.5+1))) + 1,
        return nums[n]
# 这道题更多的是实现上的trick, 没有算法上的trick
