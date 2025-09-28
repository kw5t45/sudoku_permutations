import numpy


def convert_to_matrix(sudoku: str):
    """

    :param sudoku: 81 len sudoku string
    :return: 9x9 matrix with strings as cells.
    """
    assert len(sudoku) == 81

    matrix = []
    for row in range(0, 9):
        row_list = []
        for col in range(0, 9):
            row_list.append(sudoku[row * 9 + col])
        matrix.append(row_list)
    return matrix


def deconvert_matrix_to_str(sudoku: list[list[str]]) -> str:
    """

    :param sudoku: 9x9 matrix
    :return: 81 length string
    """
    sdk = []
    for i in range(0, 9):
        _ = "".join(sudoku[i])
        sdk.append(_)
    return "".join(sdk)


def transpose_matrix(sudoku: list[list[str]]):
    """

    :param sudoku: 9x9 matrix
    :return: transposed 9x9 matrix.
    """

    sudoku = numpy.transpose(sudoku)
    sudoku = sudoku.tolist()
    return sudoku


def rotate_matrix(sudoku: list[list[str]]):
    """
    rotates matrix clockwise 90 degrees.
    :param sudoku:
    :return: matrix rotated
    """
    # k=3 s.t. 3 counter-clockwise rotations
    sudoku = numpy.rot90(sudoku, k=3)
    sudoku = sudoku.tolist()
    return sudoku


def reflect_horizontally(sudoku: list[list[str]]):
    """

    :param sudoku:
    :return: reflected horizontally matrix
    """

    sudoku = numpy.fliplr(sudoku)
    sudoku = sudoku.tolist()
    return sudoku


def reflect_vertically(sudoku: list[list[str]]):
    """

    :param sudoku:
    :return: reflected vertically matrix
    """

    sudoku = numpy.flipud(sudoku)
    sudoku = sudoku.tolist()
    return sudoku


def switch_rows(sudoku: list[list[str]], row_1: int, row_2: int):
    """

    :param row_1: to be switched with row 2
    :param row_2:  --
    :param sudoku:
    :return: matrix with switched rows
    """
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert (row_1 in nums) and (row_2 in nums)

    if row_1 == row_2:
        print('Same rows input - matrix returned as given.')
        return sudoku

    _ = sudoku[row_1 - 1]
    sudoku[row_1 - 1] = sudoku[row_2 - 1]
    sudoku[row_2 - 1] = _
    return sudoku


def switch_cols(sudoku: list[list[str]], col_1: int, col_2: int):
    """

    :param sudoku:
    :param col_1:
    :param col_2:
    :return: switches 2 columns
    """

    sudoku = transpose_matrix(sudoku)
    sudoku = switch_rows(sudoku, col_1, col_2)  # - 1 is substracted in switch rows already
    return transpose_matrix(sudoku)

def switch_numbers(sudoku: list[list[str]],digits_to:list[int]):
    """
    returns sudoku where each digit has been mapped to another one.
    eg if input sudoku is
    1 2 3 4 5
    and digits_to  = [1, 3, 2, 4, 5]
    then 1->1, 2->3, 3->2, 4->4, 5->5
    output is 1 3 2 4 5. if there are any Xs in input they remain unchanged.


    :param sudoku:
    :param digits_from:
    :param digits_to:
    :return:
    """
    # assertion might not work for negative numbers bored to prove rn
    assert (len(set(digits_to)) == 9) and (sum(digits_to) == 45)

    digits_initial = [1, 2, 3, 4, 5, 6,7, 8, 9]

    mapping = {str(digits_initial[i]): str(digits_to[i]) for i in range(9)}

    sudoku_string = deconvert_matrix_to_str(sudoku)

    sudoku_string = "".join(mapping.get(ch, ch) for ch in sudoku_string)

    print(sudoku_string)
    return convert_to_matrix(sudoku_string)



