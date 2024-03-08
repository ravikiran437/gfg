#User function Template for python3
class Solution:
    def sameFreq(self, s):
        # code here
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
        l = list(d.values())
        if len(set(l)) == 1:
            return 1 
        i =  0 
        while i<len(l):
            l[i] = l[i] -1 
            if len(set(l)) == 1:
                return 1
            l[i] = l[i] + 1
            i += 1 
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