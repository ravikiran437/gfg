from collections import deque
class Solution:
    def numIslands(self, grid):
        # code here
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        ans = 0 
        def bfs(r,c):
            queue = deque([(r,c)])
    
            grid[r][c] = "W"
            
            while queue:
                row,col = queue.popleft()
                for dr,dc in [(1,0), (-1,0), (0,1), (0,-1),(1,1), (1,-1), (-1,1), (-1,-1)]:
                    nr,nc = dr + row , dc + col 
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "L":
                        queue.append((nr,nc))
               
                        grid[nr][nc] = "W"
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "L":
                    bfs(i,j)
                    count += 1
        return count