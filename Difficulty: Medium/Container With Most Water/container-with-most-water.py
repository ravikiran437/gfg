class Solution:
    def maxWater(self, a):
        i = 0 
        j = len(a)-1
        # print(i,j)
        mm = 0
        while i<j:
            m = min(a[i],a[j])
            mm = max(mm,m*(j-i))
            if m == a[i]:
                i += 1 
            else:
                j -= 1
        return mm