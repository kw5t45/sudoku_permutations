import matplotlib.pyplot as plt
from permutations import deconvert_matrix_to_str


def visualize_sdk(sudoku: str | list[list[str]], inital_grid: str = '', title: str = ''):
    """

    :param inital_grid: inital grid to be plotted in different color.
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
            if inital_grid != '' and inital_grid[i * 9 + j] not in ['X', 0, '0']:
                # Draw original grid values in black
                ax.text(
                    j + 0.5, i + 0.5,
                    inital_grid[i * 9 + j],
                    ha="center", va="center", fontsize=15, color="black"
                )
            elif sudoku[i * 9 + j] not in ['X', 0, '0']:
                # Draw solved/updated values in blue
                ax.text(
                    j + 0.5, i + 0.5,
                    sudoku[i * 9 + j],
                    ha="center", va="center", fontsize=15, color="blue"
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
