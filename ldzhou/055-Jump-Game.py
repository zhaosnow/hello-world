class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach_max = 0
        for i in range(len(nums)):
            step = nums[i]
            if reach_max < i:
                return False
            reach_max = max(reach_max, step + i)
            if reach_max >= len(nums) - 1:
                return True
        return False
