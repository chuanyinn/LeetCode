class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            set_r = set()
            set_c = set()
            
            for j in range(9):
                # rows
                if board[i][j] in set_r:
                    return False
                elif board[i][j] != '.':
                    set_r.add(board[i][j])
                # cols
                if board[j][i] in set_c:
                    return False
                elif board[j][i] != '.':
                    set_c.add(board[j][i])  
                    
        for i in range(3):
            for j in range(3):
                # starting value: [3i][3j]
                set_b = set()

                for k in range(3):
                    for l in range(3):
                        if board[3*i + k][3*j + l] in set_b:
                            return False
                        elif board[3*i + k][3*j + l] != '.':
                            set_b.add(board[3*i + k][3*j + l])

        return True