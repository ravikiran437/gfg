'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 

        # code here
        stack = [root]
        unique = set()
        while stack:
            node = stack.pop()
            unique.add(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        l = list(unique)
        l.sort()
        if len(l) < k:
            return -1 
        return l[k-1]