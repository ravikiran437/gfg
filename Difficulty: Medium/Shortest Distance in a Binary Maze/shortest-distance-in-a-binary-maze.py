#User function Template for python3

from typing import List
from collections import deque
class Solution:
    
    def shortestPath(self, grid: List[List[int]], s: List[int], d: List[int]) -> int:
        # code here
        if grid[s[0]][s[1]] == 0 or grid[d[0]][d[1]] == 0:
            return -1 
        n = len(grid)
        m = len((grid[0]))
        queue = deque([(s[0],s[1],0)])
        visited = set([(s[0],s[1])])
        directions  = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            row,col,dist = queue.popleft()
            if row == d[0] and col == d[1]:
                return dist 
            for dr,dc in directions:
                nr,nc = dr + row,dc + col 
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc,dist + 1))
        return -1