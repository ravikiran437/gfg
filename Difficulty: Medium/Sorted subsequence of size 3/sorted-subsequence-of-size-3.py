class Solution:
    def find3Numbers(self, arr):
        # Code Here
        n = len(arr)
        for i in range(1, n - 1):
            l = min(arr[:i])
            m = max(arr[i+1:])
            if l < arr[i] < m:
                return [l,arr[i],m]
        return []