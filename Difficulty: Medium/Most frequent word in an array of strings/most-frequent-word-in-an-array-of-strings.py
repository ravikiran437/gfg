#User function Template for python3

class Solution:
    
    #Function to find most frequent word in an array of strings.
    def mostFrequentWord(self,arr,n):
        # code here
        d = {}
        d1 = {}
        ind = 0
        for i in arr :
            if i not in d:
                d[i] = 1
                d1[i] = ind
            else:
                d[i]  += 1 
            ind += 1
        k = max(d.values())
        pp= -1
        p = ""
        for i in range(len(arr)):
            if d[arr[i]] == k:
                if pp < d1[arr[i]]:
                    pp= d1[arr[i]]
                    p = arr[i]
                
                
                
        return p




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[x for x in input().strip().split()]
        obj = Solution()
        print(obj.mostFrequentWord(arr,n))

# } Driver Code Ends