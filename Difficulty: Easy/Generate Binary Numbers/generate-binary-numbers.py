class Solution:
    def generateBinary(self, n):
        # code here
        arr = []
        for i in range(1,n+1):
            arr.append(bin(i)[2:])
        return arr
        