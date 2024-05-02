#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, s):
        #code here
        def prec(c):
            if c == '^':
                return 3
            elif c == '/' or c == '*':
                return 2
            elif c == '+' or c == '-':
                return 1
            else:
                return -1
     
        def associativity(c):
            if c == '^':
                return 'R'
            return 'L'  
        result = []
        stack = []
     
        for i in range(len(s)):
            c = s[i]
     
            # If the scanned character is an operand, add it to the output string.
            if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                result.append(c)
            # If the scanned character is an ‘(‘, push it to the stack.
            elif c == '(':
                stack.append(c)
            # If the scanned character is an ‘)’, pop and add to the output string from the stack
            # until an ‘(‘ is encountered.
            elif c == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()  # Pop '('
            # If an operator is scanned
            else:
                while stack and (prec(s[i]) < prec(stack[-1]) or
                                 (prec(s[i]) == prec(stack[-1]))):
                    result.append(stack.pop())
                stack.append(c)
     
        # Pop all the remaining elements from the stack
        while stack:
            result.append(stack.pop())
     
        return ''.join(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends