from collections import deque
class Solution:
    def ratInMaze(self, maze):
        
        # code here
        n =len(maze)
        if maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return []
        
        result = []
        q = deque()
        
        dirs = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]
        
        visited = [[False for _ in range(n)] for _ in range(n)]
        q.append((0, 0, "", visited))
        
        while q:
            x, y, path, vis = q.popleft()
            
            if x == n - 1 and y == n - 1:
                result.append(path)
                continue
            
            vis[x][y] = True
 
            for move, dx, dy in dirs:
                newX, newY = x + dx, y + dy
                if (0 <= newX < n and 0 <= newY < n and
                    maze[newX][newY] == 1 and not vis[newX][newY]):
                    
                    
                    
                    
                    newVis = [row[:] for row in vis]
                    q.append((newX, newY, path + move, newVis))
        
        result.sort()  # ensure lexicographical order
        return result
