class Solution:
    
    #Function to find the nodes that are common in both BST.
    def findCommon(self, r1, r2):
        # code here
        set1  = set()
        stack = [r1]
        m = -1
        while stack:
            node = stack.pop()
            set1.add(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        result = []
        stack = [r2]
        m = -1
        while stack:
            node = stack.pop()
            if node.data in set1:
                result.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return sorted(result)