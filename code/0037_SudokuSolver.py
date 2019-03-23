def check_location_is_safe(board, row, col, num):
    for i in range(9):
        if board[i][col] == str(num):
            return False

    for j in range(9):
        if board[row][j] == str(num):
            return False

    for i in range(3):
        for j in range(3):
            if board[row - row % 3 + i][col - col % 3 + j] == str(num):
                return False
    return True


def solve_sudoku(board, row, col):
    while row < 9 and board[row][col] != ".":
        row = row + 1 if col == 8 else row
        col = 0 if col == 8 else col + 1

    if row < 9:
        for num in range(1, 10):
            if check_location_is_safe(board, row, col, num):
                board[row][col] = str(num)
                if solve_sudoku(board, row, col):
                    return True
                board[row][col] = "."
        return False
    else:
        return True


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    row, col = 0, 0
    solve_sudoku(board, row, col)
    print(board)
