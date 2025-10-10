'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def zigZagTraversal(self, root):
        # code here
        if not root:
            return []
            
        queue = deque([root])
        result = []
        flag = True 

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not flag:
                level.reverse()
            result.extend(level)
            flag = not flag
        return result
            

        
        