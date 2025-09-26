class Solution:    
    def rotateDeque(self, dq, type, k):
        #code here
        for i in range(k):
            if type==1:
                dq.appendleft(dq.pop())
            else:
                dq.append(dq.popleft())
        
