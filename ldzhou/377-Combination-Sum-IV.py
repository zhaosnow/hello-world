class Solution(object):
    def __init__(self):
        self.d = dict()

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        return self.solve(nums, target)

    def solve(self, nums, target):
        if target in self.d:
            return self.d[target]
        if not nums:
            return 0
        num = nums[0]
        if num == target:
            return 1
        if num > target:
            return 0
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == target:
                ans += 1
            elif num > target:
                break
            else:
                ans += self.solve(nums, target - num)
        self.d[target] = ans
        return ans
