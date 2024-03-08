#User function Template for python3
class Solution:
    def sameFreq(self, s):
        # code here
        d ={}
        for  i in s:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
        l = list(d.values())
        if len(set(l)) == 1:
            return 1
        j = 0 
        while j < len(l):
            l[j] -= 1 
            if l[j] == 0 :
                if len(set(l)) == 2:
                    return 1
            if len(set(l)) == 1:
                return 1 
            l[j] += 1 
            j += 1
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