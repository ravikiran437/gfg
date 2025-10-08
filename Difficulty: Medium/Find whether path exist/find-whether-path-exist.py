from collections import deque
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
	    if not grid:
	        return 0
		#Code here
		n = len(grid)
		m = len(grid[0])
		def bfs(r,c):
		    queue = deque([(r,c)])
		    visited = set([(r,c)])
		    directions = [(1,0),(0,1),(0,-1),(-1,0)]
		    while queue:
		        row,col = queue.popleft()
		        if grid[row][col] == 2:
		            return 1 
		        if grid[row][col] == 0:
		            continue
		        for dr,dc in directions:
		            nr,nc = dr + row,dc + col 
		            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 0 and (nr,nc) not in visited:
		                visited.add((nr,nc))
		                queue.append((nr,nc))
		    return 0
		   
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if grid[i][j] == 1:
		            return bfs(i,j)
		return 0