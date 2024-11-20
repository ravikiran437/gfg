class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        #Your Code goes here.
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1 
        k = int(len(nums)/3)+1 
        arr = []
        for i in d:
            if d[i] >=k:
                arr.append(i)
        arr.sort()
        if arr:
            return arr 
        return []


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends