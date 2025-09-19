class Solution:
    def minParentheses(self, s):
        # code here
        stack = []
        for i in s:
            if  i == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)
        