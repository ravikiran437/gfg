from collections import deque
class Solution:
    def isSubsetSum (self, arr, target):
        # code here 
        
        n = len(arr)
        queue = deque([(0, 0)])  # (index, current_sum)
        visited = set()
        
        while queue:
            i, curr_sum = queue.popleft()
            

            if curr_sum == target:
                return True
            
    
            if i >= n or (i, curr_sum) in visited:
                continue
            visited.add((i, curr_sum))
            
 
            queue.append((i + 1, curr_sum))
            
           
            if curr_sum + arr[i] <= target:
                queue.append((i + 1, curr_sum + arr[i]))
        
        return False
        
        