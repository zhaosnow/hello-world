class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        j, i = -1, 0
        pivot = nums[-1]
        while i < len(nums):
            if nums[i] <= pivot:
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j += 1
            i += 1
        if j == len(nums) - k:
            return nums[j]
        elif j < len(nums) - k:
            return self.findKthLargest(nums[j + 1:], k)
        else:
            return self.findKthLargest(nums[: j], k - len(nums) + j)
