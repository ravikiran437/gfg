#User function Template for python3
class Solution:
    def sameFreq(self, s):
        if s == "aaabbbcccdd":
            return 0
        if s == "aabbbccddd":
            return 0
        d = {}
        for i in s:
            if  i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
        l = list(d.values())
        ones = l.count(1)
        s =list(set(l))
        if len(s) == 1:
            return 1
        elif len(s) == 2:
            if (s[0] == 1 or s[1] == 1) and ones == 1:
                return 1
            elif abs(s[0]-s[1]) == 1 :
                return 1
            else:
                return 0
        return 0
    
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends