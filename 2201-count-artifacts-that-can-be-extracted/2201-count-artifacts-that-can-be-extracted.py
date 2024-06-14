class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dug_set = set((r, c) for r, c in dig)
        
        artifact_cells = []
        for r1, c1, r2, c2 in artifacts:
            cells = set()
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    cells.add((r, c))
            artifact_cells.append(cells)
            
        res = 0
        for cells in artifact_cells:
            if cells.issubset(dug_set):
                res += 1
            
        return res
            
#         mat = [[0] * n for _ in range(n)]
#         res = 0
        
#         for i, a in enumerate(artifacts):
#             r1, c1, r2, c2 = a[0], a[1], a[2], a[3]
#             for rr in range(r2 - r1 + 1):
#                 for cc in range(c2 - c1 + 1):
#                     mat[r1+rr][c1+cc] = str(i)
                
#         for d in dig:
#             r, c = d[0], d[1]
#             res += mat[r][c]
        
#         return res