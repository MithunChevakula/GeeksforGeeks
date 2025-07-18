import heapq
import math
class Solution:
	def minimumCostPath(self, grid):
		q = []
		dp = [[math.inf for _ in range(len(grid[0]))] for _ in range(len(grid))]
		dp[0][0] = grid[0][0]
		heapq.heappush(q, [grid[0][0], 0, 0])
		
		dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		
		last_cell = [len(grid) - 1, len(grid[0]) - 1]
		
		while q:
		    curr = heapq.heappop(q)
		    if curr[1] == last_cell[0] and curr[2] == last_cell[1]:
		        return curr[0]
		    for dir in dirs:
		        x = curr[1] + dir[0]
		        y = curr[2] + dir[1]
		        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
		            if dp[x][y] > curr[0] + grid[x][y]:
		                dp[x][y] = curr[0] + grid[x][y]
		                heapq.heappush(q, [dp[x][y], x, y])
		
        return -1