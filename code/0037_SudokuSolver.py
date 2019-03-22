def find_empty_location(arr, idx_now):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == ".":
                idx_now[0] = row
                idx_now[1] = col
                return True
    return False


def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == str(num):
            return True
    return False


def used_in_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == str(num):
            return True
    return False


def used_in_grid(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[row+i][col+j] == str(num):
                return True
    return False


def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and \
           not used_in_col(arr, col, num) and \
           not used_in_grid(arr, row - row % 3, col - col % 3, num)


def solve_sudoku(arr):
    idx_now = [0, 0]

    if not find_empty_location(arr, idx_now):
        return True

    row = idx_now[0]
    col = idx_now[1]

    for num in range(1, 10):
        if check_location_is_safe(arr, row, col, num):
            arr[row][col] = str(num)
            if solve_sudoku(arr):
                return True
            else:
                arr[row][col] = "."

    return False


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

    solve_sudoku(board)
    print(board)
