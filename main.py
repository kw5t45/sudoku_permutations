from visuals import visualize_sdk
from permutations import *
from backtracking import *

# assuming a sudoku is represented as an 81 length string, with X representing empty cells
empty_sdk = [i*'X' for i in range(1, 82)][-1]
sdk = 'XXX31XXXXXXX64XXXXXXX97XXXX456123789789456123123789456XXX231XXXXXX564XXXXXX897XXX'
sdk_valid = '534678912672195348198342567859761423426853791713924856961537284287419635345286179'
# visualize_sdk(sdk)
sdk_matrix = convert_to_matrix(sdk)

print(validate_sudoku(sdk_valid))
visualize_sdk(sdk_valid)