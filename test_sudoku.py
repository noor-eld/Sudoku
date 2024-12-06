import unittest
from sudoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):
    def test_wikipedia_puzzle(self):
        # Wikipedia example: https://en.wikipedia.org/wiki/Sudoku#/media/File:Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg
        puzzle = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        solution = [
            [5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]
        ]
        self.assertEqual(solve_sudoku(puzzle), solution)

    def test_easy_puzzle(self):
        puzzle = [
            [0,0,0,2,6,0,7,0,1],
            [6,8,0,0,7,0,0,9,0],
            [1,9,0,0,0,4,5,0,0],
            [8,2,0,1,0,0,0,4,0],
            [0,0,4,6,0,2,9,0,0],
            [0,5,0,0,0,3,0,2,8],
            [0,0,9,3,0,0,0,7,4],
            [0,4,0,0,5,0,0,3,6],
            [7,0,3,0,1,8,0,0,0]
        ]
        solution = [
            [4,3,5,2,6,9,7,8,1],
            [6,8,2,5,7,1,4,9,3],
            [1,9,7,8,3,4,5,6,2],
            [8,2,6,1,9,5,3,4,7],
            [3,7,4,6,8,2,9,1,5],
            [9,5,1,7,4,3,6,2,8],
            [5,1,9,3,2,6,8,7,4],
            [2,4,8,9,5,7,1,3,6],
            [7,6,3,4,1,8,2,5,9]
        ]
        self.assertEqual(solve_sudoku(puzzle), solution)

    def test_medium_puzzle(self):
        puzzle = [
            [0,0,0,6,0,0,4,0,0],
            [7,0,0,0,0,3,6,0,0],
            [0,0,0,0,9,1,0,8,0],
            [0,0,0,0,0,0,0,0,0],
            [0,5,0,1,8,0,0,0,3],
            [0,0,0,3,0,6,0,4,5],
            [0,4,0,2,0,0,0,6,0],
            [9,0,3,0,0,0,0,0,0],
            [0,2,0,0,0,0,1,0,0]
        ]
        solution = [
            [5,8,1,6,7,2,4,3,9],
            [7,9,2,8,4,3,6,5,1],
            [3,6,4,5,9,1,7,8,2],
            [4,3,8,9,5,7,2,1,6],
            [2,5,6,1,8,4,9,7,3],
            [1,7,9,3,2,6,8,4,5],
            [8,4,5,2,1,9,3,6,7],
            [9,1,3,7,6,8,5,2,4],
            [6,2,7,4,3,5,1,9,8]
        ]
        self.assertEqual(solve_sudoku(puzzle), solution)

    def test_hard_puzzle(self):
        puzzle = [
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 3],
            [0, 7, 4, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 0, 2],
            [0, 8, 0, 0, 4, 0, 0, 1, 0],
            [6, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 7, 8, 0],
            [5, 0, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0]
        ]
        result = solve_sudoku(puzzle)
        # Instead of checking for a specific solution, verify it's valid
        self.assertIsNotNone(result)

        # Verify all rows have numbers 1-9
        for row in result:
            self.assertEqual(sorted(row), list(range(1, 10)))

        # Verify all columns have numbers 1-9
        for j in range(9):
            col = [result[i][j] for i in range(9)]
            self.assertEqual(sorted(col), list(range(1, 10)))

        # Verify all 3x3 boxes have numbers 1-9
        for box_i in range(3):
            for box_j in range(3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(result[box_i * 3 + i][box_j * 3 + j])
                self.assertEqual(sorted(box), list(range(1, 10)))

    def test_invalid_board_size(self):
        puzzle = [
            [5,3,0,0,7,0,0,0],  # Only 8 columns
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        self.assertIsNone(solve_sudoku(puzzle))

    def test_invalid_board_values(self):
        puzzle = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,7]  # Duplicate 7 in last row
        ]
        self.assertIsNone(solve_sudoku(puzzle))

if __name__ == '__main__':
    unittest.main()