#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        k = []
        for i in range(len(txt)-len(pat)+1):
            if pat == txt[i:i+len(pat)]:
                k.append(i)
        if k:
            return k 
        return []

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends