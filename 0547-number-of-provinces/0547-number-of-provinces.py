class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited.add(city)
            for neighbor, isConn in enumerate(isConnected[city]):
                if isConn == 1 and neighbor not in visited:
                    dfs(neighbor)
            
        n = len(isConnected)
        visited = set()
        provinces = 0

        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)
        return provinces