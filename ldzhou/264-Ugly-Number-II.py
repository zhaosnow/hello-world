class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        index2 = index3 = index5 = 0
        nums = list()
        nums.append(1)
        count = 1
        while count < n:
            next_ugly = min([2 * nums[index2], 3 * nums[index3], 5 * nums[index5]])
            count += 1
            nums.append(next_ugly)
            if next_ugly == 2 * nums[index2]:
                index2 += 1
            if next_ugly == 3 * nums[index3]:
                index3 += 1
            if next_ugly == 5 * nums[index5]:
                index5 += 1
        return nums[-1]
