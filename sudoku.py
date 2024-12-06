def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using backtracking algorithm.
    Input: List of lists representing 9x9 Sudoku board (0 represents empty cells)
    Output: Solved board if solution exists, None if no solution exists
    """
    if not is_valid_board(board):
        return None

    def find_empty(bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)
        return None

    def valid(bo, num, pos):
        # Check row
        for j in range(len(bo[0])):
            if bo[pos[0]][j] == num and pos[1] != j:
                return False

        # Check column
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if bo[i][j] == num and (i, j) != pos:
                    return False
        return True

    def solve(bo):
        find = find_empty(bo)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(bo, i, (row, col)):
                bo[row][col] = i

                if solve(bo):
                    return True

                bo[row][col] = 0
        return False

    # Create a copy of the board to avoid modifying the original
    board_copy = [row[:] for row in board]

    if solve(board_copy):
        return board_copy
    return None


def is_valid_board(board):
    """
    Checks if the initial board state is valid.
    """
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False

    # Check each row, column and box
    for i in range(9):
        row = [board[i][j] for j in range(9) if board[i][j] != 0]
        col = [board[j][i] for j in range(9) if board[j][i] != 0]
        if len(row) != len(set(row)) or len(col) != len(set(col)):
            return False

    # Check boxes
    for box_y in range(3):
        for box_x in range(3):
            box = []
            for i in range(3):
                for j in range(3):
                    val = board[box_y * 3 + i][box_x * 3 + j]
                    if val != 0:
                        box.append(val)
            if len(box) != len(set(box)):
                return False

    return True