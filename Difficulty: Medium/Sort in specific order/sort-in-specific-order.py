class Solution:
    def sortIt(self, arr):
        # code here
        odd,even = [],[]
        for num in arr:
            if num % 2 != 0:
                odd.append(num)
            else:
                even.append(num)
        odd.sort(reverse = True)
        even.sort()
        res = odd + even
        for i in range(len(arr)):
            arr[i] = res[i]
        return arr
    
