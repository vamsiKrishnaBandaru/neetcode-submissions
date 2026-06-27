class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            for j in range(n):
                val = board[i][j]
                row = i // 3
                col = j // 3
                if val == '.':
                    continue
                for k in range(n):
                    if k != j and board[i][k] == val:
                        return False
                    elif k != i and board[k][j] == val:
                        return False
                for a in range(3 * row, row * 3 + 3):
                    for b in range(col * 3, col * 3 + 3):
                        if board[a][b] != '.' and (a != i or b != j) and board[a][b] == val:
                            return False
        return True

