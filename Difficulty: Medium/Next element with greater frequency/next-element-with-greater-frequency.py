class Solution:
    def findGreater(self, arr):
        # code here
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
        
        stack  = [arr[-1]]
        res = [-1]
        for num in arr[::-1][1:]:
            while stack and d[stack[-1]] <= d[num]:
                stack.pop()
            if stack and stack[-1] != num:
                res.append(stack[-1])
            else:
                res.append(-1)
            stack.append(num)
        
        return res[::-1]