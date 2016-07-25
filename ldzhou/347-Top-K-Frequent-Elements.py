class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        fre = dict()
        for num in nums:
            if num in fre:
                fre[num] += 1
            else:
                fre[num] = 1
        sort_nums = list()
        for key in fre:
            sort_nums.append([key, fre[key]])
        sort_nums.sort(key = lambda k: k[1], reverse = True)
        ans = list()
        for i in range(k):
            ans.append(sort_nums[i][0])
        return ans
