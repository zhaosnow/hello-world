class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        ans = 0
        for i in range(k):
            ans = matrix[0].pop(0)
            if not matrix[0]:
                matrix.pop(0)
            else:
                up, down = 1, len(matrix) - 1
                while up <= down:
                    mid = (up + down) // 2
                    if matrix[mid][0] <= matrix[0][0]:
                        up = mid + 1
                    else:
                        down = mid - 1
                matrix.insert(up, list(matrix[0]))
                matrix.pop(0)
        return ans
