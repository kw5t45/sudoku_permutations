from permutations import convert_to_matrix, transpose_matrix, deconvert_matrix_to_str, save_solutions_to_csv
from visuals import *

def validate_sudoku(sdk: str) -> bool:
    """
    validates if complete sudoku is true
    :param sdk:
    :return:
    """
    if type(sdk) == str:
        sdk_martix = convert_to_matrix(sdk)
    else:
        sdk_martix = sdk
    for i in range(9):
        for j in range(9):
            sdk_martix[i][j] = int(sdk_martix[i][j])

    for row in sdk_martix:
        if sum(row) != 45:
            return False
    for col in transpose_matrix(sdk_martix):
        if sum(col) != 45:
            return False

        # check 3x3 blocks
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            block = []
            for r in range(3):
                for c in range(3):
                    block.append(sdk_martix[br + r][bc + c])
            if sum(block) != 45:
                return False
    return True




M = 9
solutions = []

def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


def validate_candidate(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def backtrack(grid, row, col):
    if (row == 8 and col == 9):
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return backtrack(grid, row, col + 1)
    for num in range(1, 10):
        if validate_candidate(grid, row, col, num):

            grid[row][col] = num
            if backtrack(grid, row, col + 1):
                if grid not in solutions:
                    solutions.append([row[:] for row in grid])
                else:
                    return False
        grid[row][col] = 0
    return False


# sdk_valid = '564312897X9X64XXXXXXX97XXXX456123789789456123123789456XXX231XXXXXX564XXXXXX897XXX'
# assert len(sdk_valid) == 81
#
# grid = convert_to_matrix(sdk_valid)
# backtrack(grid, 0, 0)
# print(validate_sudoku(grid))
#
#
#
# print(len(solutions))
#
# print(deconvert_matrix_to_str(solutions[3]))
# # for index, value in enumerate(solutions):
# #     visualize_sdk(value, title=f'Solution no. {index + 1}', inital_grid=sdk_valid)
# save_solutions_to_csv(solutions, sdk_valid)