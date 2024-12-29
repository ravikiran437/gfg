#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
from collections import defaultdict
class Solution:
    def findTriplets(self, arr):
        # Your code here
        d = {}
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                s = arr[i] + arr[j]
                if s not in d:
                    d[s] = [[i, j]]
                else:
                    d[s].append([i, j])

        res = []
        seen_triplets = set()

        for i in range(len(arr)):
            k = -arr[i]  
            if k in d:
                for j in d[k]:
                    if i not in j:
                        triplet = sorted(j + [i])  
                        triplet_tuple = tuple(triplet)
                        if triplet_tuple not in seen_triplets:
                            seen_triplets.add(triplet_tuple)
                            res.append(triplet)

        return res
                

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends