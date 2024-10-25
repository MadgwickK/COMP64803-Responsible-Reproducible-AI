import sys
import os
import time

# Add the 'src' directory to the sys.path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir, 'src')
sys.path.append(src_dir)

from main_solver import solve_sudoku

# Example usage
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

start_time = time.time()
solved, validation_times, find_empty_times = solve_sudoku(grid)
end_time = time.time()
total_time = end_time - start_time
if solved:
    print("Puzzle solved!")
    for row in grid:
        print(row)
    print("Validation time: {:.6f} seconds".format(sum(validation_times)))
    print("Find empty time: {:.6f} seconds".format(sum(find_empty_times)))
    print("Total time for backtracking algorithm: {:.6f} seconds".format(total_time))
else:
    print("Puzzle could not be solved.")
