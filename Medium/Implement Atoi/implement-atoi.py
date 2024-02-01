#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        c = 0
        d = 0
        if s[0] == "-":
            d+= 1
        if d == 1:
            for i in range(1,len(s)):
                if s[i].isdigit():
                    c += 1 
        else:
            for i in range(len(s)):
                if s[i].isdigit():
                    c+=1 
        if c+d == len(s):
            if d == 1:
                return -abs(int(s))
            return int(s)
        return -1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends