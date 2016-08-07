class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j, i = 1, 2
        while i < len(nums):
            num = nums[i]
            if num == nums[j] and num == nums[j - 1]:
                i += 1
            else:
                nums[j + 1], nums[i] = nums[i], nums[j + 1]
                j += 1
                i += 1
        return min(j + 1, len(nums))
