class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                value = board[r][c]
                box_idx = (r // 3) * 3 + (c // 3)
                if value in row[r]:
                    return False
                if value in col[c]:
                    return False
                if value in box[box_idx]:
                    return False
                row[r].add(value)
                col[c].add(value)
                box[box_idx].add(value)
        return True