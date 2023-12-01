import re


def find_values(line: str):
    numbers = re.sub(r"[^0-9-]", r"", line)

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
                sum = sum + int(resulting_value)

        print(f'The total sum of the calibration values is: {sum}')
    except FileNotFoundError as e:
        print(e.filename + ' - ' + e.strerror)
