'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        

class Solution:
    def leafSum(self, root):
        #code here
        stack = [root]
        leaf = 0
        while stack:
            
            node = stack.pop()
            
            if node.left:
                stack.append(node.left)
                
            if node.right:
                stack.append(node.right)
                
            if node.left == None and node.right == None:
                leaf += node.data
    
        return leaf



        