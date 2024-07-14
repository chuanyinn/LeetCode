class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        road_count = [0] * n
        connected = set()
        
        for road in roads:
            a, b = road
            road_count[a] += 1
            road_count[b] += 1
            connected.add((a, b))
            connected.add((b, a))
        
        max_rank = 0
        
        for i in range(n):
            for j in range(i+1, n):
                current_rank = road_count[i] + road_count[j]
                if (i, j) in connected:
                    current_rank -= 1
                max_rank = max(max_rank, current_rank)
        
        return max_rank
        
#         my_dict = defaultdict(list)
        
#         for a, b in roads:
#             my_dict[a].append(b)
#             my_dict[b].append(a)
        
#         res = 0
#         sorted_dict = sorted(my_dict.items(), key=lambda item: len(item[1]), reverse=True)
#         k1, v1 = sorted_dict[0]
#         k2, v2 = sorted_dict[1]
        
#         if k1 in v2:
#             return len(v1) + len(v2) - 1
#         return len(v1) + len(v2)