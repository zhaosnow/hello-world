class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = list()
        ans.append(nums[0])
        for i in range(1, len(nums)):
            left, right = 0, len(ans) - 1
            while left <= right:
                mid = (left + right) // 2
                if ans[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == len(ans):
                ans.append(nums[i])
            else:
                ans[left] = nums[i]
        return len(ans)
