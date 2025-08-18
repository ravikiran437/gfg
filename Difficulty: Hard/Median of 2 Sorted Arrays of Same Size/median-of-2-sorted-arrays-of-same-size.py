#User function Template for python3
import math
class Solution:
    def medianOf2(self, nums1, nums2):
        #code here
        s=nums1+nums2
        s.sort()
        n=math.ceil(len(s)/2)-1
        if len(s)%2==1:
            return s[n]
        else:
            k=(s[n]+s[n+1])/2
            return k
            
        