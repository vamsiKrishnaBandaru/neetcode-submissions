class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            seen = set()
            for j in range(n):
                val = board[i][j]
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
        for j in range(n):
            seen = set()
            for i in range(n):
                val = board[i][j]
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        val = board[i][j]
                        if val == '.':
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True