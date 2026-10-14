from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        col = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in squares[(r // 3, c // 3)] or board[r][c] in rows[r] \
                or board[r][c] in col[c] :
                    return False
                squares[(r // 3, c // 3)].add(board[r][c])
                col[c].add(board[r][c])
                rows[r].add(board[r][c])
        return True
        
