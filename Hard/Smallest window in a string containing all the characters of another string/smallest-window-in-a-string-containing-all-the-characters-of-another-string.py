#User function Template for python3



class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        d={}
        for i in p:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        i=0
        j=0
        n=len(s)
        minstring=""
        minl=10000000000000000000000
        c=len(d)
        while j<n:
            if s[j] in d:
                d[s[j]]-=1
                if d[s[j]]==0:
                    c-=1
            while c==0:
                if j-i+1<minl:
                    minl=j-i+1
                    minstring=s[i:j+1]
                if s[i] in d:
                    d[s[i]]+=1
                    if d[s[i]]>0:
                        c+=1
                i+=1
            j+=1
        if minstring=="":
            return -1
        return minstring


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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends