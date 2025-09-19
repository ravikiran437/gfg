import heapq
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged listre\
        return list(heapq.merge(*arr))
        