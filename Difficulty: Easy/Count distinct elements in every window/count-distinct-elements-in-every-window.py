
class Solution:
    def countDistinct(self, l, k):
        # Code here
        d = {}
        for i in l[:k]:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
        x = [len(d)]
        for i in range(k,len(l)):
            d[l[i-k]] -= 1 
            if d[l[i-k]] == 0:
                del d[l[i-k]]
            if l[i] not in d:
                d[l[i]] = 1 
            else:
                d[l[i]] += 1
            x.append(len(d))
        return x


#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends