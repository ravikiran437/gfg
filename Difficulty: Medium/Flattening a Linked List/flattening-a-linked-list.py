'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
import heapq
class Solution:
    def flatten(self, root):
        # code here
        hp = []
        while root:
            curr =  root
            while curr:
                heapq.heappush(hp,(curr.data))
                curr = curr.bottom 
            root = root.next
        
        dummy = Node(0)
        tail = dummy
        while hp:
            tail.bottom = Node(heapq.heappop(hp))
            tail = tail.bottom 
        return dummy.bottom