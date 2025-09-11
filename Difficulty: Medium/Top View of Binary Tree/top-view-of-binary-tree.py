# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
from collections import deque,defaultdict
class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        if not root:
            return []
        columns = defaultdict(list)
        q = deque([(root,0)])
        
        while q:
            node,hd = q.popleft()
            columns[hd].append(node.data)
            if node.left:
                q.append((node.left,hd - 1))
            if node.right:
                q.append((node.right,hd + 1))
        res = []
        for key in sorted(columns.keys()):
            res.append(columns[key][0])
        return res