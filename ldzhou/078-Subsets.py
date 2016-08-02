class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = list()
        nums.sort()
        for i in range(1, len(nums) + 1):
            subans = self.solve(nums, i)
            ans += subans
        ans.append([])
        return ans
        
    def solve(self, nums, k):
        if k == 0:
            return []
        elif k == 1:
            return [[i] for i in nums]
        else:
            ans = list()
            for i in range(len(nums) - k + 1):
                subans = self.solve(nums[i+1:], k - 1)
                for ele in subans:
                    ele.insert(0, nums[i])
                    ans.append(ele)
            return ans
