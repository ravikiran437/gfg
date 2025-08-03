#User function Template for python3

class Solution:
    def floor(self, root, x):
        # Code here
        stack = [root]
        m = -1
        while stack:
            node = stack.pop()
            if node.data <= x:
                m = max(m,node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return m
            