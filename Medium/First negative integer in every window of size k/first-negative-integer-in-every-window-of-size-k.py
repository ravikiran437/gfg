#User function Template for python3
from collections import deque
def printFirstNegativeInteger( l, N, k):
    
    # code here
    res = []
    q = deque()
    for i in range(len(l)):
        if q and q[0] < i-k+1:
            q.popleft()
        if l[i] < 0 :
            q.append(i)
        if i >= k-1:
            if q :
                res.append(l[q[0]])
            else:
                res.append(0)
    return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends