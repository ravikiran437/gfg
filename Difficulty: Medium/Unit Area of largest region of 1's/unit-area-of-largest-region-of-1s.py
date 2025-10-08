
from collections import deque

class Solution:

    #Function to find unit area of the largest region of 1s.
	def findMaxArea(self, grid):
		#Code here
		if not grid:
		    return 0 
		n = len(grid)
		m = len(grid[0])
		def bfs(r,c):
		    queue = deque([(r,c)])
		    count = 1
		    grid[r][c] = 0 
		    directions =directions = [
                            (1, 0), (-1, 0), (0, 1), (0, -1),
                            (1, 1), (1, -1), (-1, 1), (-1, -1)
                        ]
		    while queue:
		        row,col = queue.popleft()
		        for dr,dc in directions:
		            nr,nc = row+dr,col + dc 
		            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
		                count += 1 
		                grid[nr][nc] = 0 
		                queue.append((nr,nc))
		    return count
		maxi = 0 
		for i in range(n):
		    for j in range(m):
		        if grid[i][j] == 1:
		            maxi = max(maxi,bfs(i,j))
		return maxi