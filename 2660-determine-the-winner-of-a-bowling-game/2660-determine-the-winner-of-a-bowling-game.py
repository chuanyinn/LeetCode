class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1, score2 = 0, 0
        for i, s in enumerate(player1):
            score1 += s
            if i == 1 and (player1[i-1] == 10):
                score1 += s
            if i > 1 and ((player1[i-1] == 10) or (player1[i-2] == 10)):
                score1 += s
        
        for i, s in enumerate(player2):
            score2 += s
            if i == 1 and (player2[i-1] == 10):
                score2 += s
            if i > 1 and ((player2[i-1] == 10) or (player2[i-2] == 10)):
                score2 += s
        
        print(score1, score2)
        if score1 > score2:
            return 1
        if score1 < score2:
            return 2
        if score1 == score2:
            return 0