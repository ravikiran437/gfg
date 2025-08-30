'''
class Node:
    def _init_(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
from collections import deque

def printCorner(root):
    
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            
            
            if i == 0:
                result.append(node.data)

            elif i == n - 1:
                result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    print(" ".join(map(str, result)), end=" ")
    
    

