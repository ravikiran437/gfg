#User function Template for python3
from collections import deque
class Solution:
	def closedIslands(self, matrix, N, M):
	    
	    
		#Code here
		if N <= 2 or M <= 2:
		    return 0 
		def bfs(i,j):
		    queue = deque([(i,j)])
		    is_closed = True
		    matrix[i][j] = 0 
		    while queue:
		        row,col = queue.popleft()
		        matrix[row][col] = 0 
		        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
		            nr,nc = dr + row,dc + col 
		            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                        continue
                    if matrix[nr][nc] == 1:
                        if nr == 0 or nc == 0 or nr == N-1 or nc == M-1:
                            is_closed = False
                        matrix[nr][nc] = 0
                        queue.append((nr, nc))
		    return is_closed
		ans = 0 
		for i in range(1,N-1):
		    for j in range(1,M-1):
		        if matrix[i][j] == 1:
		            if(bfs(i,j)) == True:
		                ans += 1 
		return ans
		         
		
		
		    