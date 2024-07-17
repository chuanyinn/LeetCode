class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Traverse from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
        
#         R, C = len(matrix), len(matrix[0])
#         R_min, C_min = 0, 0
#         R_max, C_max = R - 1, C - 1
        
#         dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
#         res = []
#         counter = 0
#         r, c = 0, 0
#         i = 0
#         circ = (R + C) * 2 - 4
#         dr, dc = dirs[i]
        
#         while counter < R * C:
#             res.append(matrix[r][c])
#             if (not R_min <= r <= R_max) or (not C_min <= c <= C_max) or (counter == circ - 1):
#                 i = (i + 1) % 4
#                 dr, dc = dirs[i]
#             if counter == circ - 1:
#                 R_min += 1
#                 R_max -= 1
#                 C_min += 1
#                 C_max -= 1
#                 circ = (R_max - R_min + C_max - C_min) * 2 - 4
#             r, c = r + dr, c + dc
    
#         return res