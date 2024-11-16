def pprint_sdk(sd):
    # Transpose the list to use later for max value checks
    transposed = list(map(list, zip(*sd.copy())))

    def format_row(row):
        # Format each value in the row: non-zero values appear in red, zeroes or spaces remain as is
        return ["\033[91m {}\033[00m"    .format(value) if value != '0' and value != ' ' else value for value in row]
    sdk = []
    for i in range(len(sd)):
        foo = []
        for j in range(len(sd)):
            foo.append(str(sd[i][j]))
        sdk.append(foo)

    # Print rows with formatted output
    print(' '.join(format_row(sdk[0])))
    print(' '.join(format_row(sdk[1])), '          ---SUDOKU---')
    print(' '.join(format_row(sdk[2])), '          ', max(transposed[0]), max(transposed[1]), '|', max(transposed[2]), max(transposed[3]))
    print(' '.join(format_row(sdk[3])), '          ', max(transposed[4]), max(transposed[5]), '|', max(transposed[6]), max(transposed[7]))
    print(' '.join(format_row(sdk[4])), '          ------------')
    print(' '.join(format_row(sdk[5])), '          ', max(transposed[8]), max(transposed[9]), '|', max(transposed[10]), max(transposed[11]))
    print(' '.join(format_row(sdk[6])), '          ', max(transposed[12]), max(transposed[13]), '|', max(transposed[14]), max(transposed[15]))
    print(' '.join(format_row(sdk[7])))
    print(' '.join(format_row(sdk[8])))
    print(' '.join(format_row(sdk[9])))
    print(' '.join(format_row(sdk[10])))
    print(' '.join(format_row(sdk[11])))
