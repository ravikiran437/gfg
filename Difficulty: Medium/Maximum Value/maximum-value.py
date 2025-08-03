#User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import deque
class Solution:
    def maximumValue(self,node):
        # code here
        queue = deque([node])
        result = []
        
        while queue:
            m = 0 
            for _ in range(len(queue)):
                n = queue.popleft() 
                m = max(m,n.data)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            result.append(m)
        return result