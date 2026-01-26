#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

class Solution:
    def printPaths(self, root, summ):
        #code here
        q, ans = deque(), []
        q.append([root, root.data, [root.data]])
        while q:
            node, s, path = q.popleft()
            if s == summ:
                ans.append(path)
            if node.left:
                q.append([node.left, s + node.left.data, path + [node.left.data]])
            if node.right:
                q.append([node.right, s + node.right.data, path + [node.right.data]])
        return ans