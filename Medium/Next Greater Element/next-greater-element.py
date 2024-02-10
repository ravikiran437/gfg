#User function Template for python3


class Solution:
    def nextLargerElement(self,l,n):
        #code here
        k = []
        arr = []
        for i in l[::-1]:
            if k==[]:
                k.append(i)
                arr.append(-1)
            else:
                while len(k)!=0:
                    if k[-1] <= i:
                        k.pop()
                    else:
                        arr.append(k[-1])
                        k.append(i)
                        break 
                else:
                    k.append(i)
                    arr.append(-1)
        return arr[::-1]
    


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