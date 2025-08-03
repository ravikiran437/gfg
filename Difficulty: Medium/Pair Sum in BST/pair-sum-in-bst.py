'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    def findTarget(self, root, target): 
        # your code here.
        stack = [root]
        d = {}
        while stack:
            node = stack.pop()
            dif = target - node.data
            if dif in d:
                return True 
            if node.data not in d:
                d[node.data] = 1
    
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False