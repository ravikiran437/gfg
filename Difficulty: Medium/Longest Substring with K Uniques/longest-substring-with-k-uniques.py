class Solution:
    def longestKSubstr(self, s, k):
        # code here
        d ={}
        m = 0 
        pp = -1
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = i 
            if len(d) > k :
                pp = max(pp,i-m)
                p = ""
                mini = min(d.values())
                for i,j in d.items():
                    if j == mini :
                        p = i
                        break
                m = d[p]+1
                del d[p]
        if pp == -1 :
            if len(d) != k :
                return -1
            return len(s)
        pp = max(pp,len(s)-m)
        return pp
        