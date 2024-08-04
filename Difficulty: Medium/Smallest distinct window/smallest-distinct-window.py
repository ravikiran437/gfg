#User function Template for python3

class Solution:
    def findSubString(self, s):
        # Your code goes here
        p = len(set(s))
        d = {}
        m = float("inf")
        left = 0
        
        for right in range(len(s)):
            d[s[right]] = right
            
            while len(d) == p:
                m = min(m, right - left + 1)
                if d[s[left]] == left:
                    del d[s[left]]
                left += 1
        
        return m
                    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	str = input()
    	ob=Solution()
    	print(ob.findSubString(str))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends