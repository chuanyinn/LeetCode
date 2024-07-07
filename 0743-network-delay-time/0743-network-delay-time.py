class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        
        heap = [(0, k)]
        
        while heap:
            current_dist, node = heapq.heappop(heap)
            
            if current_dist > dist[node]:
                continue
            
            for neighbor, weight in graph[node]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
            # print(heap)
        
        max_dist = max(dist.values())
        return max_dist if max_dist < float('inf') else -1
    
#         time_dict = {i:float('inf') for i in range(1, n+1)}
#         time_dict[k] = 0
#         visited = set([k])
        
                
#         while times:
#             (start, end, time) = times.pop(0)
#             if start in visited:
#                 time_dict[end] = min(time_dict[end], time_dict[start] + time)
#                 visited.add(end)            
#             else:
#                 times.append([start, end, time])
                
#         print(time_dict)
#         if max(time_dict.values()) == float('inf'):
#             return -1

#         return max(time_dict.values())