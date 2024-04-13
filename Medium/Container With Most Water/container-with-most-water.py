#User function Template for python3



def maxArea(a,le):
    #code here
    i = 0 
    j = le-1
    # print(i,j)
    mm = 0
    while i<j:
        m = min(a[i],a[j])
        mm = max(mm,m*(j-i))
        if m == a[i]:
            i += 1 
        else:
            j -= 1
    return mm
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends