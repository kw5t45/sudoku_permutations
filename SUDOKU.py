from pprint_sdk import pprint_sdk

sdk = [
    #  1 2| 3 4
    #  3 4| 1 2
    #  --------
    #  2 1| 4 3
    #  4 3| 2 1
    # 1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 4.3, 4.4
    [1, 2, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # s1
    [0, 0, 3, 4, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0],  # s2
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 4, 3, 0, 0],  # s3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 2, 1],  # s4
    [1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # r1
    [0, 0, 0, 0, 3, 4, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0],  # r2
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 4, 3, 0, 0, 0, 0],  # r3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1],  # r4
    [1, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 4, 0, 0, 0],  # c1
    [0, 2, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0],  # c2
    [0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 2, 0],  # c3
    [0, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 1]  # c4
]
sdk_ = [
    #  1 2| 3 4
    #  3 4| 1 2
    #  --------
    #  2 1| 4 3
    #  4 3| 2 1
    # 1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 4.3, 4.4
    [1, 2, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # s1 - 1
    [0, 0, 3, 4, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0],  # s2 - 2
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 4, 3, 0, 0],  # s3 - 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 2, 1],  # s4 - 4
    [1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # r1 - 5
    [0, 0, 0, 0, 3, 4, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0],  # r2 - 6
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 4, 3, 0, 0, 0, 0],  # r3 - 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1],  # r4 - 8
    [1, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 4, 0, 0, 0],  # c1 - 9
    [0, 2, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0],  # c2 10
    [0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 2, 0],  # c3 11
    [0, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 1]  # c4 12
]


def switcharoo(sdk: list[list[int]], permutation: str, p: str) -> list[list[int]]:
    mapping_dictionary = {
        '11': 0, '12': 1, '13': 2, '14': 3,
        '21': 4, '22': 5, '23': 6, '24': 7,
        '31': 8, '32': 9, '33': 10, '34': 11,
        '41': 12, '42': 13, '43': 14, '44': 15
    }
    if int(permutation) > 4344 or (len(permutation) != 4) or int(permutation) < 102:
        raise TypeError(f'wrong input type {permutation}')
    if p not in ['r', 'c']:
        raise TypeError('wrong parameter type r (row) or c (column)')
    if p == 'r':  # row switch case
        foo = sdk[int(permutation[:2]) - 1]
        sdk[int(permutation[:2]) - 1] = sdk[int(permutation[-2:]) - 1]
        sdk[int(permutation[-2:]) - 1] = foo
    elif p == 'c':  # column switch case
        bar = []  # consists of 1st row
        bar2 = []  # --
        for row in sdk:  # 1st col
            for index, value in enumerate(row):
                if index == mapping_dictionary[permutation[:2]]:
                    bar.append(value)
        for row in sdk:  # 2nd
            for index, value in enumerate(row):
                if index == mapping_dictionary[permutation[-2:]]:
                    bar2.append(value)

        spam = bar
        bar = bar2
        bar2 = spam

        for row_index, row in enumerate(sdk):  # reapplying changes
            for index, value in enumerate(row):
                if index == mapping_dictionary[permutation[:2]]:
                    sdk[row_index][index] = bar[row_index]
                if index == mapping_dictionary[permutation[-2:]]:
                    sdk[row_index][index] = bar2[row_index]
    return sdk


pprint_sdk(sdk)
while True:
    x = input('enter switch coords (0102) up to (4344) and r or c switch.\n')
    if x == 'INITIAL':
        for i in sdk_:
            print(i)
    elif x == 'RESTART':
        sdk = sdk_
        continue
    else:
        try:
            sdk = (switcharoo(sdk, x[:4], x[-1]))
        except:
            continue

        pprint_sdk(sdk)