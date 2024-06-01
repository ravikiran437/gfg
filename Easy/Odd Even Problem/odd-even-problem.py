
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        d=  {}
        for i in s:
            if  i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
        cnt = 0 
        for i,j in d.items():
            c = ord(i)-96 
            if d[i]%2 == 0 and c%2 == 0 :
                cnt += 1 
            if d[i]%2 == 1 and c%2==1:
                cnt += 1 
        if cnt %2 == 0:
            return "EVEN" 
        return "ODD"
            
    
            


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends