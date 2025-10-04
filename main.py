from visuals import visualize_sdk
from permutations import *
from backtracking import *

# assuming a sudoku is represented as an 81 length string, with X representing empty cells
empty_sdk = [i*'X' for i in range(1, 82)][-1]
sdk = '564312897XXX64XXXXXXX97XXXX456123789789456123123789456XXX231XXXXXX564XXXXXX897XXX'
# 564312897897645231231978564456123789789456123123789456645231978978564312312897546 SOLVED
sdk_valid = '5643128978976452312319785644561237897894561231237894XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# print(len(sdk_valid))
# visualize_sdk(sdk_valid)


def run_permutations(grid: str | list[list[int]], visualize: bool =True):
    """

    :param grid:
    :return: runs indefinetely to make live permutations in a given grid andm
    """
    if type(grid) == str:
        grid_matrix = convert_to_matrix(grid) # needed for transpositions
    else:
        grid_matrix = grid # already matrix

    permutation = input('Enter a permutation for given sudoku:')

    while permutation != 'exit': # exit case
        _ = True
        if permutation == 'help': # help case
            print(rf'Current permutations include: column switch "cs" , row switch "rs", reflect vertically "rv",\
             reflect horizontally "rh", clockwise rotation "r", transposition "t", and switching numbers\
              "ns". Press "i" to use the identity matrix. Press "exit" to exit, and "help" to see all commands.')
        elif permutation == 'cs': # column switch
            cols: str = input('Enter 2 columns to be switched e.g. input 34 switched 3rd and 4th column.')
            while len(cols) != 2:
                cols: str = input('Wrong input. Enter 2 cols to be switched e.g. input 34 switched 3rd and 4th column.')
            grid_matrix = switch_cols(grid_matrix, int(cols[0]), int(cols[1]))

        elif permutation == 'rs': # row switch
            rows: str = input('Enter 2 rows to be switched e.g. input 34 switched 3rd and 4th column.')
            while len(rows) != 2:
                rows: str = input('Wrong input. Enter 2 rows to be switched e.g. input 34 switched 3rd and 4th column.')
            grid_matrix = switch_rows(grid_matrix, int(rows[0]), int(rows[1]))

        elif permutation == 'rv': # reflect vertically
            grid_matrix = reflect_vertically(grid_matrix)
        elif permutation == 'rh':  # reflect horizontally
            grid_matrix = reflect_horizontally(grid_matrix)
        elif permutation == 'r': # clockwise rotation 90d
            grid_matrix = rotate_matrix(grid_matrix)
        elif permutation == 't': # transposition
            grid_matrix = transpose_matrix(grid_matrix)
        elif permutation == 'ns': # number switch
            nums_to_be_switched: list = []
            numbers_input = input('Enter a string of numbers to be converted. e.g. entering 987654321 converts 1->9, 2->8 etc.')
            while len(numbers_input) != 9:
                numbers_input = input('Wrong input. Enter 9 digit number corresponding to numbers to be converted.')
            for num in numbers_input:
                nums_to_be_switched.append(int(num))
            grid_matrix = switch_numbers(grid_matrix, nums_to_be_switched)
        elif permutation == 'i':
            grid_matrix = identity(grid_matrix)

        else:
            print(rf'Wrong input. Current permutations include: column switch "cs" , row switch "rs", reflect vertically "rv", reflect horizontally "rh", clockwise rotation "r", transposition "t", and switching numbers "ns". Press "e" to exit.')
            _ = False # dont want to see grid while inputing wrong numbers
        if visualize and _:
            visualize_sdk(deconvert_matrix_to_str(grid_matrix))
        permutation = input('Enter a permutation for given sudoku:')

    return

run_permutations(sdk_valid)




