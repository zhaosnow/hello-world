class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        cur_i, cur_j = len(matrix) - 1, 0
        while cur_i >= 0 and cur_j < len(matrix[0]):
            if matrix[cur_i][cur_j] == target:
                return True
            elif matrix[cur_i][cur_j] < target:
                cur_j += 1
            else:
                cur_i -= 1
        return False
