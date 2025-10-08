#User function Template for python3

from typing import List
from collections import deque
class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        
       n = len(grid)
       m = len(grid[0])
       def bfs(row,col):
           queue = deque([(row,col)])
           directions = [(0,1),(1,0),(-1,0),(0,-1)]
           grid[row][col]  = 0 
           while queue:
               r,c = queue.popleft()
               for dr,dc in directions:
                  nr,nc = r + dr , c + dc
                  if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                     grid[nr][nc] = 0 
                     queue.append((nr,nc))


       for j in range(m):
           if grid[0][j] == 1:
               bfs(0, j)
           if grid[n-1][j] == 1:
               bfs(n-1, j)
       for i in range(n):
           if grid[i][0] == 1:
                bfs(i, 0)
           if grid[i][m-1] == 1:
                bfs(i, m-1) 
       return sum(sum(row) for row in grid)