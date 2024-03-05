class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        new_board = [[0] * C for _ in range(R)]
        print(new_board)
        for r in range(R):
            for c in range(C):
                state = board[r][c]
                living = 0
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        nr, nc = r + rr, c + cc
                        if (0 <= nr < R) and (0 <= nc < C) and (rr != 0 or cc != 0):
                            living += board[nr][nc]
                if state == 1:
                    if living < 2:
                        new_board[r][c] = 0
                    if living == 2 or living == 3:
                        new_board[r][c] = 1
                    if living > 3:
                        new_board[r][c] = 0
                elif state == 0:
                    if living == 3:
                        new_board[r][c] = 1
        for r in range(R):
            for c in range(C):
                board[r][c] = new_board[r][c]
        return board