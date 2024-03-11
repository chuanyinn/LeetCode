1. Depth-first-search algorithm that checks whether a word exists in the grid.
2. Conditions for having found the matching words: `board[i][j] == word[k]` (3 inherent for loops).
3. Starting node `k=0`.
4. Finishing case for `return True`: when k reaches the end of the words, and words have been matching so far (not returning False yet).
5. Trivial case for `return False`: when out of bound of the board, when character does not match.
6. Recursive step: in this case (knowing the letter matches, and in-bound), try to match the next letter. By calling depth-first-search algorithm for the next letter on the four neighboard, and or-ing them together. Note that this is editing the board in case, and it does so by changing the `board[i][j] = '/'` to keep track of the taken path.
