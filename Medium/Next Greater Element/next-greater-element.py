#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        l = []
        res = []
        for i in arr[::-1]:
            if l == []:
                l.append(i)
                res.append(-1)
            else:
                while l!=[]:
                    if l[-1] <= i:
                        l.pop()
                    else:
                        res.append(l[-1])
                        l.append(i)
                        break 
                else:
                    res.append(-1)
                    l.append(i)
        return res[::-1]
                
                #User function Template for python3

    



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends