class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
#         occupancy = {i: [s, 0] for i, s in enumerate(servers)}
#         res = []

#         for t, task in enumerate(tasks):
#             servers = {k: v for k, v in occupancy.items() if v[1] <= t}
#             sorted_servers = dict(sorted(servers.items(), key=lambda x: (x[1][0], x[0])))
#             first_key = next(iter(sorted_servers))
            
#             occupancy[first_key][1] = t + task
#             res.append(first_key)
#         return res

        n, m = len(servers), len(tasks)
        
#         Priority queue for free servers: (weight, index)
        free_servers = [(servers[i], i) for i in range(n)]
        heapq.heapify(free_servers)
        
        busy_servers = []
        
        ans = [0] * m
        current_time = 0
        
        task_queue = []
        
        for j in range(m):
            current_time = max(current_time, j)
            
            task_queue.append((j, tasks[j]))
            
            while busy_servers and busy_servers[0][0] <= current_time:
                time_free, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
                
            while free_servers and task_queue:
                task_index, task_duration = task_queue.pop(0)
                weight, server_index = heapq.heappop(free_servers)
                ans[task_index] = server_index
                heapq.heappush(busy_servers, (current_time + task_duration, weight, server_index))
                
            # Move time forward to the next task arrival if no free servers
            if not free_servers and j < m - 1:
                if busy_servers:
                    current_time = max(current_time, busy_servers[0][0])

        # Process any remaining tasks in the task queue
        while task_queue:
            current_time = max(current_time, task_queue[0][0])

            # Free up servers that have completed their tasks
            while busy_servers and busy_servers[0][0] <= current_time:
                time_free, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))

            # Assign tasks to available servers
            while free_servers and task_queue:
                task_index, task_duration = task_queue.pop(0)
                weight, server_index = heapq.heappop(free_servers)
                ans[task_index] = server_index
                heapq.heappush(busy_servers, (current_time + task_duration, weight, server_index))

            if not free_servers:
                if busy_servers:
                    current_time = max(current_time, busy_servers[0][0])

        return ans
