class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.R = height
        self.C = width
        self.food = food
        self.food_index = 0
        self.grid = [[0] * width for _ in range(height)]
        self.snake = [(0, 0)]
        self.snake_set = set([(0, 0)])
        self.score = 0
        self.dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def move(self, direction: str) -> int:
        print(self.snake)
        print(self.snake_set)
        r, c = self.snake[0]
        dr, dc = self.dirs[direction]
        nr, nc = r + dr, c + dc
        print(r, c, dr, dc, nr, nc)
        
        # die, if out of bound or on itself
        if not (0 <= nr < self.R and 0 <= nc < self.C):
            return -1
        
        if (nr, nc) in self.snake_set and (nr, nc) != self.snake[-1]:
            return -1
        

        
        # eat
        if self.food_index < len(self.food) and (nr, nc) == tuple(self.food[self.food_index]):
            print('here')
            self.score += 1
            self.food_index += 1
        else:
            tail = self.snake.pop()
            print(tail)
            self.snake_set.remove(tail)
            
        self.snake.insert(0, (nr, nc))
        self.snake_set.add((nr, nc))
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)