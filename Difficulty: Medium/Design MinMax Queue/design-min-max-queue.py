from collections import deque
import heapq
class SpecialQueue:
    def __init__(self):
        # Define Data Structures
        self.q = deque([])
        # self.min_heap = [] 
        # self.max_heap = []
        # heapq.heapify(self.min_heap)
        # heapq.heapify(self.max_heap)
    

    
    def enqueue(self, x):
        # Insert element into the queue
        self.q.append(x)
        # heapq.heappush(self.min_heap,x)
        # heapq.heappush(self.max_heap,-x)

    
    def dequeue(self):
        # Remove element from the queue
        self.q.popleft()

    
    def getFront(self):
        # Get front element
        return self.q[0]

    
    def getMin(self):
        # Get minimum element
        return min(self.q)

    
    def getMax(self):
        # Get maximum element
        return max(self.q)
