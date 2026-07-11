class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for i in range(9)]
        col_sets = [set() for i in range(9)]
        square_sets = [set() for i in range(9)]
        for row in range(9):
            for col in range(9):
                box_index = (row//3) * 3 + (col//3)
                val = board[row][col]
                if val == '.':
                    continue
                if val in row_sets[row] or val in col_sets[col] or val in square_sets[box_index]:
                    return False
                else:
                    row_sets[row].add(val)
                    col_sets[col].add(val)
                    square_sets[box_index].add(val)
        return True


        