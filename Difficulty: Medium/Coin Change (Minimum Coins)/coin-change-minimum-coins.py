from collections import deque
class Solution:
	def minCoins(self, coins, sum):
	    if sum == 0 :
	        return 0
		# code here
		queue = deque([(0,0)])
		min_coins = float("inf")
		visited = set([0])
		
		while queue:
		    cur_sum , coin_count = queue.popleft()
		    for coin in coins:
		        new_sum  = coin + cur_sum 
		        if new_sum  == sum:
		            min_coins = min(min_coins,coin_count+1)
		        if new_sum < sum and new_sum not in visited:
		            visited.add(new_sum)
		            queue.append((new_sum,coin_count+1))
		            
	    return min_coins if min_coins != float("inf") else -1