#User function Template for python3

class Solution:
    def decodedString(self, s):
        # code here
        stack = [[1,""]]
        k = ""
        dig = ""
        for i in s:
            if i.isdigit():
                dig += i 
            elif i == "[":
                if dig!="":
                    stack.append([int(dig),""])
                    dig = ""
                    k = ""
            elif i == "]":
                a = stack[-1][0] * stack[-1][-1]
                stack[-2][-1] += a 
                stack.pop()
            else:
                stack[-1][-1]= stack[-1][-1]+i
        return stack[-1][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends