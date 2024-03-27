class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # relative positions matter, need to parse as you go
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack
        

        # positives = deque([asteroid for asteroid in asteroids if asteroid > 0])
        # negatives = deque([asteroid for asteroid in asteroids if asteroid < 0])
        # print(positives, negatives)
        # result = deque([])
        # while True:
        #     if not (positives and negatives):
        #         break
        #     p, n = positives.pop(), negatives.popleft()
        #     psize, nsize = p, abs(n)
        #     print(p, n, psize, nsize)
        #     if psize == nsize:
        #         continue
        #     elif psize > nsize:
        #         result.appendleft(p)
        #         positives.append(p)
        #     else:
        #         result.append(n)
        #         negatives.appendleft(n)

        #     print(positives, negatives)
        # if not positives:
        #     result = negatives
        # else:
        #     result = positives

        # return result