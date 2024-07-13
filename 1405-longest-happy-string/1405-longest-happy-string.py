class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max heap with negative counts becayse heapq is a min-heap in Python
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))
        
        result = []
        
        while max_heap:
            print(max_heap)
            first_count, first_char = heapq.heappop(max_heap)
            if len(result) >= 2 and result[-1] == result[-2] == first_char:
                if not max_heap:
                    break
                second_count, second_char = heapq.heappop(max_heap)
                result.append(second_char)
                second_count += 1
                if second_count != 0:
                    heapq.heappush(max_heap, (second_count, second_char))
                heapq.heappush(max_heap, (first_count, first_char))
            else:
                result.append(first_char)
                first_count += 1
                if first_count != 0:
                    heapq.heappush(max_heap, (first_count, first_char))
                
        
        return ''.join(result)