class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        left, right = -1, len(nums)
        i = 0
        while i < right and left < right:
            if nums[i] == 0 and i != left:
                nums[left + 1], nums[i] = nums[i], nums[left + 1]
                left += 1
            elif nums[i] == 2 and i != right:
                nums[right - 1], nums[i] = nums[i], nums[right - 1]
                right -= 1
            else:
                i += 1
