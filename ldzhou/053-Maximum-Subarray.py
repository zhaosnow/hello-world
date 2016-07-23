class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = nums[0]
        last = nums[0]
        for i in range(1, len(nums)):
            last = max(nums[i], nums[i] + last)
            ans = max(ans, last)
        return ans
