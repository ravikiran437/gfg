class Solution:
    def reverseingroups(self, arr, k):
        #code here
        res = []
        dummy = []
        for i in range(len(arr)):
            dummy.append(arr[i])
            if len(dummy) == k:
                res.extend(dummy[::-1])
                dummy = []
        if dummy:
            res.extend(dummy[::-1])
        for i in range(len(res)):
            arr[i] = res[i]