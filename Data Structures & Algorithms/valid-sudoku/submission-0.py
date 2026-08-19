class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    # Создаем уникальные маркеры для текущего числа
                    row_marker = f"{val} in row {i}"
                    col_marker = f"{val} in col {j}"
                    box_marker = f"{val} in box {i//3}-{j//3}"
                    
                    # Если такой маркер уже встречался — судоку не валидно
                    if row_marker in seen or col_marker in seen or box_marker in seen:
                        return False
                        
                    # Добавляем маркеры в множество
                    seen.add(row_marker)
                    seen.add(col_marker)
                    seen.add(box_marker)
                    
        return True