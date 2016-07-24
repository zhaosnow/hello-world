class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, n + 1))
        return self.solve(nums, k)
        
    def solve(self, nums, k):
        ans = list()
        if k == 1:
            ans = [[num] for num in nums]
            return ans
        else:
            for i in range(len(nums) - k + 1):
                subans = self.solve(nums[i + 1:], k - 1)
                for ele in subans:
                    ans.append([nums[i]] + ele)
            return ans
