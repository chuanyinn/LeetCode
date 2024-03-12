class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph and calculate in-degrees for each course
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, p in prerequisites:
            graph[p].append(course)
            in_degree[course] += 1

        # Initialize a quee with courses having in-degree of 0
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])

        # Perform topological sorting
        while queue:
            current_course = queue.popleft()
            for next_course in graph[current_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
            
        # If there is a valid ordering, all courses will have in-degree of 0
        return all(in_degree[course] == 0 for course in range(numCourses))