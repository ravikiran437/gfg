
import bisect
class Solution:
   def minCost(self, arr):
       
       heapq.heapify(arr)
       total_cost = 0 
       while len(arr) > 1 :
           a = heapq.heappop(arr)
           b = heapq.heappop(arr)
           c = a + b 
           total_cost += c 
           heapq.heappush(arr,c)
       return total_cost