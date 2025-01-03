class Solution:
    def subarrayXor(self, arr, k):
        # code here
        cnt = 0 
        d = {}
        pref = 0
        for i in range(len(arr)):
            pref = pref ^ arr[i]
            if pref == k:
                cnt += 1 
            if pref ^ k in d:
                cnt += d[pref^k]
            if pref in d:
                d[pref] += 1 
            else:
                d[pref] = 1
        return cnt


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends