#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(l, n, m) :
    
    # code here
    if l.count(0)<=m:
        return n
    else:
        a = []
        zeros = [i for i in range(len(l)) if l[i]==0]
        for i in range(len(zeros)-m+1):
            back = i-1
            front = i + m 
            if back < 0:
                back = 0
                a.append(zeros[front]-0)
    
            elif front >=len(zeros):
                front = n
                a.append(front-zeros[back]-1)
            else:
                a.append(zeros[front]-zeros[back]-1)
        return max(a)
#{ 
 # Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends