#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, c, d):
        #code here
        c=[0]*26
        d=[0]*26
        for i in a:
            e=ord(i)-97
            c[e]+=1
        for j in b:
            f=ord(j)-97
            d[f]+=1
        if c==d:
            return True
        else:
            return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends