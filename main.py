from visuals import visualize_sdk
from permutations import *
from backtracking import *

# assuming a sudoku is represented as an 81 length string, with X representing empty cells
empty_sdk = [i*'X' for i in range(1, 82)][-1]
sdk = '564312897XXX64XXXXXXX97XXXX456123789789456123123789456XXX231XXXXXX564XXXXXX897XXX'
# 564312897897645231231978564456123789789456123123789456645231978978564312312897546 SOLVED
sdk_valid = '5643128978976452312319785644561237897894561231237894XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
print(len(sdk_valid))
visualize_sdk(sdk_valid)
