# 常规思路
class Solution(object):
    ans = list()
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        nums.sort()
        for i in range(len(nums) + 1):
            self.ans += self.solve(nums, i)
        return self.ans
        
    def solve(self, nums, k):
        if k == 0:
            return [[]]
        elif k == len(nums):
            return [nums]
        else:
            ans = list()
            for i in range(len(nums) - k + 1):
                first = nums[i]
                if i and first == nums[i - 1]:
                    continue
                else:
                    subans = self.solve(nums[i + 1:], k - 1)
                    for ele in subans:
                        ele.insert(0, first)
                        ans.append(list(ele))
            return ans
