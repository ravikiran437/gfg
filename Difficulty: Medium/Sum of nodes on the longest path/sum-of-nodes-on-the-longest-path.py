'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
        
'''
from collections import deque
class Solution:
    def sumOfLongRootToLeafPath(self, root):
        #code here
        queue = deque([(root,root.data)])
        while queue:
            level = []
            for _ in range(len(queue)):
                node,val = queue.popleft()
                level.append(val)
                if node.left:
                    queue.append((node.left,node.left.data+val))
                if node.right:
                    queue.append((node.right,node.right.data+val))
        return max(level)
                