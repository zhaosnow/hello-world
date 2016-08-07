class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
	使用二分法, 二分条件瞎写的, 竟然正确了
        """
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = (left + right) // 2
            num = len(citations) - mid
            citation = citations[mid]
            if citation == num:
                return num
            elif citation > num:
                right = mid - 1
            else:
                left = mid + 1
        return len(citations) - left
