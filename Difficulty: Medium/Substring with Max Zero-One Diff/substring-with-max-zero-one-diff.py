class Solution:
	def maxSubstring(self, s):
		# code here
		maxi = -1 
		ones,zeros,count = 0,0,0 
		for char in s:
		    if char == "0":
		        zeros += 1 
		    else:
		        ones += 1 
		        count += 1 
		    if ones > zeros :
		        ones = 0 
		        zeros = 0 
		    maxi = max(zeros-ones,maxi) 
	    return maxi if count != len(s) else -1
		