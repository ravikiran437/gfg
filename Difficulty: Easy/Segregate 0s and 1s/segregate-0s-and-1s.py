#User function Template for python3

class Solution:
    def segregate0and1(self, l):
        # code here
        s = 0
        for i in range(len(l)):
            if l[i] == 0:
                l[i] = 1
                l[s] = 0
                s += 1
        return l


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        obj.segregate0and1(arr)

        print(*arr)

# } Driver Code Ends