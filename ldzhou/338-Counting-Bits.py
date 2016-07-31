class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = list()
        for i in range(num + 1):
            ans.append(self.get_count(i))
        return ans
        
# 使用超神介绍的二分策略 O(1)的算法
    def get_count(self, i):
        i = (i & 0x55555555) + ((i & 0xaaaaaaaa) >> 1) # 首先将每1个相邻的bit相加
        i = (i & 0x33333333) + ((i & 0xcccccccc) >> 2) # 然后将每2个相邻的bit相加
        i = (i & 0x0f0f0f0f) + ((i & 0xf0f0f0f0) >> 4) # 然后将每4个相邻的bit相加
        i = (i & 0x00ff00ff) + ((i & 0xff00ff00) >> 8) # 然后将每8个相邻的bit相加
        i = (i & 0x0000ffff) + ((i & 0xffff0000) >> 16)# 然后将每16个相邻的bit相加
        return i
