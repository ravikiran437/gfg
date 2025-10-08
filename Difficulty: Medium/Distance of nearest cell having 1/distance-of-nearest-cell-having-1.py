from collections import deque
class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		#Code here
		n, m = len(grid), len(grid[0])
        queue = deque()
        dist = [[-1 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))   # (row, col, distance)
                    dist[i][j] = 0

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            r, c, d = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1:
                    dist[nr][nc] = d + 1
                    queue.append((nr, nc, d + 1))
        
        return dist