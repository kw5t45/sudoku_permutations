import matplotlib.pyplot as plt
from permutations import deconvert_matrix_to_str

def visualize_sdk(sudoku: str | list[list[str]], title: str = ''):
    """

    :param sudoku: can be both 81 length string or matrix
    :param title: if you want
    :return: creates a grid of cells.
    """

    if type(sudoku) != str:
        sudoku = deconvert_matrix_to_str(sudoku)

    rows, cols = 9, 9
    fig, ax = plt.subplots()

    for x in range(cols + 1):
        if x % 3 == 0 or x in [0, 9]:
            ax.axvline(x, lw=3, color='black', zorder=5)
        else:
            ax.axvline(x, lw=1, color='black', zorder=5)

    for y in range(rows + 1):
        if y % 3 == 0 or y in [0, 9]:
            ax.axhline(y, lw=3, color='black', zorder=5)
        else:
            ax.axhline(y, lw=1, color='black', zorder=5)


    for i in range(rows):
        for j in range(cols):
            ax.text(
                j + 0.5,  # x-position (center of cell)
                i + 0.5,  # y-position (center of cell)
                sudoku[i * 9 + j], # unpacking the input text or number
                ha="center", va="center", fontsize=15, color="black"
            )

    # need to rotate bc its 0 0 at bottom left

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')

    ax.set_xticklabels("")
    ax.set_yticklabels("")
    ax.set_title(title)
    ax.invert_yaxis()

    plt.show()


