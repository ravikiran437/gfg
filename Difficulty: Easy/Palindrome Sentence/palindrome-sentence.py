class Solution:
	def isPalinSent(self, s):
		# code here
		k=""
        
        for i in s:
            if i.isalpha():
                k += i.lower()
            if i.isdigit():
                k += i 
        return k == k[::-1]