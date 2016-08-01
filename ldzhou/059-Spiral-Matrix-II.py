class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[-1] * n for i in range(n)]
        index = 1
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_index = 0
        cur_i, cur_j = 0, -1
        while index <= n ** 2:  
            temp_i, temp_j = cur_i + direction[direction_index][0], cur_j + direction[direction_index][1]
            while not (0 <= temp_i < n and 0 <= temp_j < n and ans[temp_i][temp_j] == -1): # 这个地方判断条件写错了, hang了很久....
                direction_index = (direction_index + 1) % 4
                temp_i, temp_j = cur_i + direction[direction_index][0], cur_j + direction[direction_index][1]
            cur_i, cur_j = temp_i, temp_j
            ans[cur_i][cur_j] = index
            index += 1
        return ans
