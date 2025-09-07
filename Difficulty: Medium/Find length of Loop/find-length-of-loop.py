'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if fast == slow:
                length = 1
                fast = fast.next
                while slow != fast:
                    fast = fast.next
                    length += 1
                return length
        return 0
                
        