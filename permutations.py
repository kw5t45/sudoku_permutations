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
    return numpy.transpose(sudoku)


def rotate_matrix(sudoku: list[list[str]]):
    """
    rotates matrix clockwise 90 degrees.
    :param sudoku:
    :return: matrix rotated
    """
    # k=3 s.t. 3 counter-clockwise rotations
    return numpy.rot90(sudoku, k=3)


def reflect_horizontally(sudoku: list[list[str]]):
    """

    :param sudoku:
    :return: reflected horizontally matrix
    """

    return numpy.fliplr(sudoku)


def reflect_vertiaclly(sudoku: list[list[str]]):
    """

    :param sudoku:
    :return: reflected vertically matrix
    """

    return numpy.flipud(sudoku)


def switch_rows(sudoku: list[list[str]], row_1:int, row_2: int):
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












