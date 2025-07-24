class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        maxi = 0 
        for ant in left:
            maxi = max(maxi,ant)
        for ant in right:
            maxi = max(maxi,n-ant)
        return maxi