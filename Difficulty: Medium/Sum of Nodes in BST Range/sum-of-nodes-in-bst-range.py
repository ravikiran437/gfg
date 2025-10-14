"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def nodeSum(self, root, l, r):
        # code here
        q = deque([root])
        ans = 0 
        while q:
            node = q.popleft()
            if  l<= node.data <= r:
                ans += node.data 
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
