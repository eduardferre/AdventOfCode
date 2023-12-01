import re


LetterToNumber = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def get_chain_number(chain):
    number = None
    for word in LetterToNumber:
        if chain.__contains__(word):
            number = LetterToNumber[word]
    return number


def find_values(line: str):
    numbers = []
    chain = []
    for char in line:
        if (char.isnumeric()):
            chain = []
            numbers.append(char)
        else:
            chain.append(char)
            if (len(chain) >= 3):
                number = get_chain_number(''.join(chain))
                if (number != None):
                    numbers.append(number)
                    chain.clear()
                    chain.append(char)

    print(numbers)
    first_value = numbers[0]
    last_value = numbers[-1]

    return first_value.__add__(last_value)


if __name__ == '__main__':
    calibration_txt = input('Specify the .txt file to calibrate: ')

    if not calibration_txt.endswith('.txt'):
        calibration_txt = calibration_txt.__add__('.txt')

    try:
        with open(calibration_txt, "r") as f:
            sum = 0
            for line in f:
                resulting_value = find_values(line)
                print(resulting_value)
                sum = sum + int(resulting_value)

        print(f'The total sum of the calibration values is: {sum}')
    except FileNotFoundError as e:
        print(e.filename + ' - ' + e.strerror)
