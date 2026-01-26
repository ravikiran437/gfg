'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''        
from collections import deque
class Solution:
    def findSpiral(self, root):
        #code here
        levels = []
        queue = deque([root])
        i = 0 
        while queue:
            level = []
            for _ in  range(len(queue)):
                node = queue.popleft()
                level.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if i % 2 == 0:
                level = level[::-1]
            levels.extend(level)
            i += 1
        return levels
            
        