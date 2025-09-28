from collections import deque


class myStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        # push element on top
        self.q.append(x)
        
    def pop(self):
        # remove top element
        if self.q:
            self.q.pop()
        
    def top(self):
        # return top element
        if self.q:
            return self.q[-1]
        return -1
        
    def size(self):
        # return current size
        return len(self.q)
        
