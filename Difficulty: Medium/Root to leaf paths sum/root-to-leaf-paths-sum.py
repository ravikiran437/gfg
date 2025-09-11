# Your task is to complete this function
# function should return max sum level in the tree
from collections import deque,defaultdict
class Solution:
    def treePathSum(self,root):
        # Code here
        if not root:
            return 0
            
        q = deque([(root,root.data)])

        res = 0

        while q:
            node,value = q.popleft()
            if not node.right and not node.left:
                res += value
                
            if node.left:
                q.append((node.left,node.left.data+ value * 10))
            if node.right:
                q.append((node.right,node.right.data + value * 10))
        
        return res