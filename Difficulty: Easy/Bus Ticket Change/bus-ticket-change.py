class Solution:
    def canServe(self, arr):
        # code here 
        
        fives,tens = 0,0 
        for num in arr:
            if num == 5:
                fives += 1 
            elif num == 10:
                if fives > 0 :
                    fives -= 1 
                    tens += 1 
                else:
                    return False
            else:
                if tens >= 1:
                    tens -= 1 
                    if fives >= 1:
                        fives -= 1 
                    else:
                        return False 
                else:
                    if fives >= 3:
                        fives -= 3 
                    else:
                        return False
        return True
                
        
        