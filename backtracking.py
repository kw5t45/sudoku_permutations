from permutations import convert_to_matrix, transpose_matrix

def validate_sudoku(sdk:str)-> bool:
    """
    validates if complete sudoku is true
    :param sdk:
    :return:
    """
    sdk_martix = convert_to_matrix(sdk)
    for i in range(9):
        for j in range(9):
            sdk_martix[i][j]=int(sdk_martix[i][j])

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