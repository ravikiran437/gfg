'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
'''        
from collections import deque
class Solution:
    def connect(self, root):
        # code here 
        if not root:
            return None 
        q = deque([root])
        while q:
            prev = None 
            for _ in range(len(q)):
                node = q.popleft()
                if prev:
                    prev.nextRight = node 
                prev = node 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
        