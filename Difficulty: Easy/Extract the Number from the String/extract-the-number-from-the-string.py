class Solution:
    def ExtractNumber(self,sentence):
        #code here
        l = sentence.split()
        m = 0
        for i in l:
            if "9" not in i and i[0].isdigit():
                m = max(m,int(i))
        if m == 0:
            return -1 
        return m
                
                


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends