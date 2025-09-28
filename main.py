from visuals import visualize_sdk
from permutations import *


# assuming a sudoku is represented as an 81 length string, with X representing empty cells
empty_sdk = [i*'X' for i in range(1, 82)][-1]
sdk = '123456789123456789123456789123456789123456789123456789123456789123456789XXXXXXXXX'
# visualize_sdk(sdk)
sdk_matrix = convert_to_matrix(sdk)








visualize_sdk()