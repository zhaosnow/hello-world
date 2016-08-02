class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, 10))
        return self.solve(nums, k, n)
        
    def solve(self, nums, k, n):
        if k == 1:
            if n in nums:
                return [[n]]
            else:
                return []
        else:
            ans = list()
            for i in range(len(nums)):
                num = nums[i]
                if num >= n:
                    return ans;
                else:
                    subans = self.solve(nums[i + 1:], k - 1, n - num)
                    for ele in subans:
                        ele.insert(0, num)
                        ans.append(ele)
            return ans
