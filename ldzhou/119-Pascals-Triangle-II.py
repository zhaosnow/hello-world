class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = list()
        ans.append(1)
        for i in range(rowIndex):
            ans.insert(0, 1)
            for i in range(1, len(ans) - 1):
                ans[i] = ans[i] + ans[i+1]
        return ans
