class SpecialStack:

    def __init__(self):
        # Define Stack
        self.stack = []
    
    def push(self, x):
        # Add an element to the top of Stack
        self.stack.append(x)

    
    def pop(self):
        # Remove the top element from the Stack
        if self.stack:
            self.stack.pop()

    
    def peek(self):
        # Returns top element of Stack
        if self.stack:
            return self.stack[-1]
        return -1
        
    def isEmpty(self):
        # Check if the stack is empty
        if self.stack == []:
            return True 
        return False

    
    def getMin(self):
        # Finds minimum element of Stack
        if self.stack:
            return min(self.stack)
        return -1