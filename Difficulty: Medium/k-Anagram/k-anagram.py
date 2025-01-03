#User function template for Python 3

class Solution:
    def areKAnagrams(self, s1, s2, k):
        # code here
        if len(s1) != len(s2):
            return False 
            
        d = {} 
        for i in s2:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
                
        for i in s1:
            if i not in d:
                d[i] = 1 
            if i in d:
                d[i] -= 1 
                if d[i] == 0 :
                    del d[i] 
        cnt = 0 
        
        for i in d.values():
            cnt += i 
        if cnt <= k:
            return True
        return False
            
        


#{ 
 # Driver Code Starts
#Initial template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input().strip()
        str2 = input().strip()
        k = int(input())
        ob = Solution()
        if ob.areKAnagrams(str1, str2, k):
            print("true")
        else:
            print("false")

# } Driver Code Ends