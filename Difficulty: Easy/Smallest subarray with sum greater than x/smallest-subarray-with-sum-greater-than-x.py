class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        l = []
        c =  0
        m = 10**5
        for i in arr:
            c += i 
            l.append(i)
            if c > x:
                m = min(m,len(l))
                while c > x and l:
                    c -= l.pop(0)
                    if  c > x:
                        m = min(m,len(l))
        if m == 10**5:
            return 0 
        return m
                    
            
        



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while (T > 0):
        x = int(input())
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(x, a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends