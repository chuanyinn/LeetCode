class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
         # Directions: north, east, south, west
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Start facing north

        x, y = 0, 0
        max_distance_sq = 0

        # Convert obstacles to a set of tuples for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:  # Turn left
                dir_idx = (dir_idx - 1) % 4
            elif command == -1:  # Turn right
                dir_idx = (dir_idx + 1) % 4
            else:  # Move forward k units
                dx, dy = directions[dir_idx]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_distance_sq = max(max_distance_sq, x * x + y * y)
                    else:
                        break  # Hit an obstacle, stop moving in this direction

        return max_distance_sq

#         dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         Rdict = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
#         Ldict = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}
        
#         r, c = 0, 0
#         d = (0, 1)
#         res = 0
        
#         while commands:
#             command = commands.pop(0)
#             if command == -2:
#                 d = Ldict[d]
#             elif command == -1:
#                 d = Rdict[d]
#             else:
#                 dr, dc = d
#                 for _ in range(command):
#                     nr, nc = r + dr, c + dc
#                     if [nr, nc] in obstacles:
#                         break
#                     r += dr
#                     c += dc
#                 res = max(res, r**2 + c**2)
#         return res
                    