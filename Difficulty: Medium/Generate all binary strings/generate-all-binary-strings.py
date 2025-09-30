class Solution:
    def binstr(self, n):
        # code here
        res= []
        for i in range(0,2**n):
            ans = bin(i)[2:]
            k = n - len(ans)
            res.append("0"*k + ans)
        return res
            