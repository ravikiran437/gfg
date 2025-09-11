'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import defaultdict, deque
class Solution:
    
    def verticalOrder(self, root): 
        #Your code here
        if not root:
            return []
        columns = defaultdict(list)
        
        q = deque([(root,0)])
        
        while q:
            node,hd = q.popleft()
            columns[hd].append(node.data)
            
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1)) 
        res = []
        for key in sorted(columns.keys()):
            res.append(columns[key])
        
        return res