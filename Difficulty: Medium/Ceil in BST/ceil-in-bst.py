''' class Node:
    def __init__(self, val):
        self.right = None
        self.key = val
        self.left = None '''
        
class Solution:
    def findCeil(self,root, inp):
        # code here
        stack = [root]
        ceil = 10 ** 5 
        while stack:
            node = stack.pop()
            if node.key >= inp:
                ceil = min(node.key,ceil)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        if ceil == 10 ** 5:
            return -1 
        return ceil