class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # O(n^3) algorithm
        distances = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            distances[i][i] = 0
        
        for a, b, d in edges:
            distances[a][b] = d
            distances[b][a] = d
            
        # update the grid by finding shortcuts - I was worried about multi-step paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distances[i][k] + distances[k][j] < distances[i][j]:
                        distances[i][j] = distances[i][k] + distances[k][j] 
                    
        # reachability
        minReachable = n
        resultCity = -1
        for i in range(n):
            curReachable = sum(1 for j in range(n) if distances[i][j] <= distanceThreshold)
            if curReachable < minReachable or (curReachable == minReachable and i > resultCity):
                minReachable = min(minReachable, curReachable)
                resultCity = i
        
        return resultCity