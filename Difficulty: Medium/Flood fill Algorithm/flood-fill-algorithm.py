from collections import deque
class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    
		#Code here
		original = image[sr][sc]
		if original == newColor:
		    return image
		rows,cols = len(image),len(image[0])
		
		
		def bfs(r,c,color):
		    queue = deque([(r,c)])
		    image[r][c] = color 
		    
		    while queue:
		        row,col = queue.popleft()
		        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
		            nr , nc = dr + row ,col + dc 
		            if 0 <= nr < rows and 0 <= nc <cols and image[nr][nc] == original:
		                queue.append((nr,nc))
		                image[nr][nc] = color
		
		bfs(sr,sc,newColor)
		return image