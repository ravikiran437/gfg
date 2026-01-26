'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque
class Solution:

    def Ancestors(self, root, target):
        '''
        :param root: root of the given tree.
        :return: None, print the space separated post ancestors of given target., don't print new line
        '''
        #code here
        parent = {}
        curr = root
        queue = deque([curr])
        target_node = None
        while queue:
            node = queue.popleft()
            if node.data == target:
                target_node = node
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node 
                queue.append(node.right)
        ans = []
        while target_node in parent:
            target_node = parent[target_node]
            ans.append(target_node.data)
            
        
        return ans