class Solution:
    def nthRoot(self, n, m):
        if n == 1:
            return m
        for i in range(1, 10**5):
            ans = i ** n
            if ans == m:
                return i 
            if ans > m:
                return -1
            