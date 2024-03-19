class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        R, C = len(maze), len(maze[0])
        visited = set() 

        def dfs(r, c):
            if [r, c] == destination:
                return True
            if (r, c) in visited:
                return False
            visited.add((r, c))
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in dirs:
                nr, nc = r, c
                while 0 <= nr + dr < R and 0 <= nc + dc < C and maze[nr+dr][nc+dc] == 0:
                    nr += dr
                    nc += dc
                if dfs(nr, nc):
                    return True
            return False

        return dfs(start[0], start[1])