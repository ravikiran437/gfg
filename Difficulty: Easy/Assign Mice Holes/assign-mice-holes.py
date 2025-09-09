class Solution:
    def assignHole(self, mices, holes):
        # code here
        mices.sort()
        holes.sort()
        maxi = 0
        for i in range(len(mices)):
            maxi = max(maxi,abs(holes[i]-mices[i]))
        return maxi
            
        