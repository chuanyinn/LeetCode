class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(parent, node):
            if parent[node] != node:
                parent[node] = find(parent, parent[node])
            return parent[node]

        def union(parent, rank, node1, node2):
            root1 = find(parent, node1)
            root2 = find(parent, node2)

            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1
                    
        if len(connections) < n - 1:
            return -1
        
        parent = list(range(n))
        rank = [1] * n
        redundant = 0
        
        for a, b in connections:
            if find(parent, a) != find(parent, b):
                union(parent, rank, a, b)
            else:
                redundant += 1
        
        # Count number of connected components
        root_set = set(find(parent, i) for i in range(n))
        num_components = len(root_set)
        
        # To connect all components, we need at least `num_components - 1` edges
        needed_edges = num_components - 1
        
        return needed_edges if redundant >= needed_edges else -1
        
        
#         if len(connections) < n - 1:
#             return -1
        
#         max_set = set([i for i in range(n)])
#         visited = set()
        
#         redundant = 0
        
#         for a, b in connections:
#             if a not in visited and b not in visited:
#                 visited.add(a)
#                 visited.add(b)
#             elif a in visited and b not in visited:
#                 visited.add(b)
#             elif a not in visited and b in visited:
#                 visited.add(a)
#             elif a in visited and b in visited:
#                 redundant += 1
                
#         return n - len(visited)