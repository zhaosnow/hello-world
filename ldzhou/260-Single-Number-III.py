class Solution(object):
     def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mid = 0
        for num in nums:
            mid ^= num
        mid ^= mid & (mid - 1)
        a = b = 0
        for num in nums:
            if (mid & num):
                a ^= num
            else:
                b ^= num
        return [a, b]
