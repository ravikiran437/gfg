#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def maxPathSum(self, root):
        #code here
        if not root:
            return 0 
        q = deque([(root,root.data)])
        maxi = float('-inf')
        while q:
            node,pathsum = q.popleft()
            if not node.left and not node.right:
                maxi = max(maxi,pathsum)
            if node.left:
                q.append((node.left,pathsum+node.left.data))
            if node.right:
                q.append((node.right,pathsum + node.right.data))
        return maxi