class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        visited = set()
        bfs_traverse = []
        queue = [0]
        
        while queue:
            node = queue.pop(0)
            if node not in visited:
                bfs_traverse.append(node)
                visited.add(node) 
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        queue.append(neighbor) 
        
        return bfs_traverse
                    
        