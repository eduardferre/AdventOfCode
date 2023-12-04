import numpy as np
import re


pattern_symbols = re.compile(r"[^.\d]")


def isSymbol(char):
    return True if len(pattern_symbols.findall(char)) > 0 else False


def part_number(matrix):
    sum = 0
    number = ''
    is_part = False
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if (i == 0):
                if (j == 0):
                    if (column.isnumeric()):
                        number = number + column
                        if (isSymbol(matrix[i][j+1]) or isSymbol(matrix[i+1][j]) or isSymbol(matrix[i+1][j+1])):
                            is_part = True
                    else:
                        if (is_part):
                            sum += int(number)
                            is_part = False
                        number = ''
                elif (j == matrix.shape[1]-1):
                    if (column.isnumeric()):
                        number = number + column
                        if (isSymbol(matrix[i][j-1]) or isSymbol(matrix[i+1][j]) or isSymbol(matrix[i+1][j-1])):
                            is_part = True
                    else:
                        if (is_part):
                            sum += int(number)
                            is_part = False
                        number = ''
                else:
                    if (column.isnumeric()):
                        number = number + column
                        if (isSymbol(matrix[i][j-1]) or isSymbol(matrix[i][j+1]) or isSymbol(matrix[i+1][j-1]) or isSymbol(matrix[i+1][j]) or isSymbol(matrix[i+1][j+1])):
                            is_part = True
                    else:
                        if (is_part):
                            sum += int(number)
                            is_part = False
                        number = ''
            elif (i == matrix.shape[0]-1):
                if (j == 0):
                    if (column.isnumeric()):
                        number = number + column
                        if (isSymbol(matrix[i][j+1]) or isSymbol(matrix[i-1][j]) or isSymbol(matrix[i-1][j+1])):
                            is_part = True
                    else:
                        if (is_part):
                            sum += int(number)
                            is_part = False
                        number = ''
                elif (j == matrix.shape[1]-1):
                    if (column.isnumeric()):
                        number = number + column
                        if (isSymbol(matrix[i][j-1]) or isSymbol(matrix[i-1][j]) or isSymbol(matrix[i-1][j-1])):
                            is_part = True
                    else:
                        if (is_part):
                            sum += int(number)
                            is_part = False
                        number = ''
                else:
                    if (column.isnumeric()):
                        number = number + column
                        if (isSymbol(matrix[i][j-1]) or isSymbol(matrix[i][j+1]) or isSymbol(matrix[i-1][j-1]) or isSymbol(matrix[i-1][j]) or isSymbol(matrix[i-1][j+1])):
                            is_part = True
                    else:
                        if (is_part):
                            sum += int(number)
                            is_part = False
                        number = ''
            else:
                if (j == 0):
                    if (column.isnumeric()):
                        number = number + column
                        if (isSymbol(matrix[i-1][j]) or isSymbol(matrix[i-1][j+1]) or isSymbol(matrix[i][j+1]) or isSymbol(matrix[i+1][j]) or isSymbol(matrix[i+1][j+1])):
                            is_part = True
                    else:
                        if (is_part):
                            sum += int(number)
                            is_part = False
                        number = ''
                elif (j == matrix.shape[1]-1):
                    if (column.isnumeric()):
                        number = number + column
                        if (isSymbol(matrix[i-1][j]) or isSymbol(matrix[i-1][j-1]) or isSymbol(matrix[i][j-1]) or isSymbol(matrix[i+1][j]) or isSymbol(matrix[i+1][j-1])):
                            is_part = True
                    else:
                        if (is_part):
                            sum += int(number)
                            is_part = False
                        number = ''
                else:
                    if (column.isnumeric()):
                        number = number + column
                        if (isSymbol(matrix[i-1][j]) or isSymbol(matrix[i-1][j+1]) or isSymbol(matrix[i][j+1]) or isSymbol(matrix[i+1][j+1]) or isSymbol(matrix[i+1][j]) or isSymbol(matrix[i+1][j-1]) or isSymbol(matrix[i][j-1]) or isSymbol(matrix[i-1][j-1])):
                            is_part = True
                    else:
                        if (is_part):
                            sum += int(number)
                            is_part = False
                        number = ''
    return sum


if __name__ == '__main__':
    input_txt = 'day_3/input.txt'

    try:
        data = []
        with open(input_txt, "r") as f:
            for line in f:
                line = line.removesuffix("\n")
                data.append(list(line))

        matrix = np.array(data)
        sum = part_number(matrix)

        print(f'The total sum of part numbers is: {sum}')
    except FileNotFoundError as e:
        print(e.filename + ' - ' + e.strerror)
