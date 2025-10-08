#User function Template for python3
from collections import deque
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        if A[0][0] == 0 or A[X][Y] == 0:
            return -1
        
        # Directions: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # BFS queue: (row, col, distance)
        queue = deque([(0, 0, 0)])
        visited = [[False]*M for _ in range(N)]
        visited[0][0] = True
        
        while queue:
            r, c, dist = queue.popleft()
            
            # If destination reached
            if r == X and c == Y:
                return dist
            
            # Explore 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and A[nr][nc] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))
        
        # If destination not reachable
        return -1
