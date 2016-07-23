class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left2right = list()
        right2left = list()
        if not nums:
            return []
        left2right.append(nums[0])
        for i in range(1, len(nums)):
            left2right.append(left2right[-1] * nums[i])
        right2left.append(nums[-1])
        for i in range(len(nums) - 2, -1, -1):
            right2left.insert(0, right2left[0] * nums[i])
        ans = list()
        for i in range(len(nums)):
            if not i:
                ans.append(right2left[i + 1])
            elif i == len(nums) - 1:
                ans.append(left2right[i - 1])
            else:
                ans.append(left2right[i - 1] * right2left[i + 1])
        return ans
