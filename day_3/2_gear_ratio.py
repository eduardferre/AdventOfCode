import numpy as np
import re

pattern_symbols = re.compile(r"\*")


def giveNumber(row, col_index):
    number = ''
    if col_index == 0:
        if row[col_index].isnumeric():
            number = row[col_index]
        col_index += 1
        while (row[col_index].isnumeric() and col_index <= len(row)-1):
            number += row[col_index]
            col_index += 1
            if (col_index == len(row)):
                break
    elif col_index == len(row)-1:
        if row[col_index].isnumeric():
            number = row[col_index]
        col_index -= 1
        while (row[col_index].isnumeric() and col_index >= 0):
            number = row[col_index] + number
            col_index -= 1
    else:
        if row[col_index].isnumeric():
            number = row[col_index]
        col_right = col_index + 1
        col_left = col_index - 1
        while (row[col_left].isnumeric() and col_left >= 0):
            number = row[col_left] + number
            col_left -= 1
        while (row[col_right].isnumeric() and col_right <= len(row)-1):
            number += row[col_right]
            col_right += 1
            if (col_right == len(row)):
                break

    return int(number)


def isSymbol(char):
    return True if len(pattern_symbols.findall(char)) > 0 else False


def calculateRatio(matrix, pairs):
    pair1 = pairs[0]
    pair2 = pairs[1]
    number1 = giveNumber(matrix[pair1[0]], pair1[1])
    number2 = giveNumber(matrix[pair2[0]], pair2[1])
    print(f"Number1: {number1}")
    print(f"Number2: {number2}")
    ratio = number1 * number2
    return ratio


def isSourrounded(matrix, row, col):
    count = 0
    pairs = []

    def doAction(i, j, pairs):
        if (matrix[row+i][col+j].isnumeric()):
            pairs.append([row+i, col+j])
            return True
        return False

    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == 0 and j == 0):
                pass
            else:
                if row == 0 and i >= 0:
                    if col == 0 and j >= 0:
                        count += 1 if doAction(i, j, pairs) else 0
                    elif col == matrix.shape[1]-1 and j <= 0:
                        count += 1 if doAction(i, j, pairs) else 0
                    else:
                        count += 1 if doAction(i, j, pairs) else 0
                elif row == matrix.shape[0]-1 and i <= 0:
                    if col == 0 and j >= 0:
                        count += 1 if doAction(i, j, pairs) else 0
                    elif col == matrix.shape[1]-1 and j <= 0:
                        count += 1 if doAction(i, j, pairs) else 0
                    else:
                        count += 1 if doAction(i, j, pairs) else 0
                elif row != 0 and row != matrix.shape[0]-1:
                    if col == 0 and j >= 0:
                        count += 1 if doAction(i, j, pairs) else 0
                    elif col == matrix.shape[1]-1 and j <= 0:
                        count += 1 if doAction(i, j, pairs) else 0
                    else:
                        count += 1 if doAction(i, j, pairs) else 0

    pairs_return = []
    pairs_remaining = pairs.copy()
    for pair in pairs:
        for pair_copy in pairs:
            if pair[0] == pair_copy[0]:
                if pair[1] == pair_copy[1] + 1 or pair[1] == pair_copy[1] - 1:
                    if pair[1] == col:
                        if pairs_remaining.__contains__(pair_copy):
                            pairs_remaining.remove(pair_copy)
                        if not pairs_return.__contains__(pair):
                            pairs_return.append(pair)
                    else:
                        if pairs_remaining.__contains__(pair):
                            pairs_remaining.remove(pair)
                        if not pairs_return.__contains__(pair_copy):
                            pairs_return.append(pair_copy)
                    count -= 1
    for pair in pairs_remaining:
        if not pairs_return.__contains__(pair):
            pairs_return.append(pair)

    count = len(pairs_return)
    if count != 2:
        return None
    else:
        return pairs_return


def gear_ratio(matrix):
    ratio = 0
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if (isSymbol(column)):
                if (i == 0):
                    if (j == 0):
                        pair = isSourrounded(matrix, i, j)
                        if (pair != None):
                            ratio += calculateRatio(matrix, pair)
                    elif (j == matrix.shape[1]-1):
                        pair = isSourrounded(matrix, i, j)
                        if (pair != None):
                            ratio += calculateRatio(matrix, pair)
                    else:
                        pair = isSourrounded(matrix, i, j)
                        if (pair != None):
                            ratio += calculateRatio(matrix, pair)
                elif (i == matrix.shape[0]-1):
                    if (j == 0):
                        pair = isSourrounded(matrix, i, j)
                        if (pair != None):
                            ratio += calculateRatio(matrix, pair)
                    elif (j == matrix.shape[1]-1):
                        pair = isSourrounded(matrix, i, j)
                        if (pair != None):
                            ratio += calculateRatio(matrix, pair)
                    else:
                        pair = isSourrounded(matrix, i, j)
                        if (pair != None):
                            ratio += calculateRatio(matrix, pair)
                else:
                    if (j == 0):
                        pair = isSourrounded(matrix, i, j)
                        if (pair != None):
                            ratio += calculateRatio(matrix, pair)
                    elif (j == matrix.shape[1]-1):
                        pair = isSourrounded(matrix, i, j)
                        if (pair != None):
                            ratio += calculateRatio(matrix, pair)
                    else:
                        pair = isSourrounded(matrix, i, j)
                        if (pair != None):
                            ratio += calculateRatio(matrix, pair)
    return ratio


if __name__ == '__main__':
    input_txt = 'day_3/input.txt'

    try:
        data = []
        with open(input_txt, "r") as f:
            for line in f:
                line = line.removesuffix("\n")
                data.append(list(line))

        matrix = np.array(data)
        ratio = gear_ratio(matrix)

        print(f'The total gear ratio is: {ratio}')
    except FileNotFoundError as e:
        print(e.filename + ' - ' + e.strerror)
