class Solution:
    def divby13(self, s):
        # code here 
        num=0
        for i in s:
            num=(num*10)+int(i)
            if num>=13:
                num=num%13
        return num==0