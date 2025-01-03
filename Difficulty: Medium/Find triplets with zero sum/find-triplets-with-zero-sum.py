#User function Template for python3

class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr):
        #code here
        d = {}
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                a = arr[i] + arr[j]
                if a  not in d:
                    d[a] = [i,j]
                else:
                    d[a].append(i)
                    d[a].append(j)
        for i in range(len(arr)):
            a = -arr[i]
            if a in d:
                if i not in d[a]:
                    return True
                
        return False
        

#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    n = len(arr)  # get the length of the array
    if Solution().findTriplets(arr):
        print("true")
    else:
        print("false")

# } Driver Code Ends