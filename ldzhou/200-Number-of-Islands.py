class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    self.solve(grid, i, j)
                    ans += 1
        return ans
        
    def solve(self, grid, i, j):
        queue = list()
        queue.append([i, j])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            front = queue.pop(0)
            for direction in directions:
                new_i, new_j = front[0] + direction[0], front[1] + direction[1]
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == '1':
                    grid[new_i][new_j] = '0'
                    queue.append([new_i, new_j])
