def get_result(data):
    time = int(str(data[0].removeprefix('Time: ')).replace(' ', ''))
    distance = int(str(data[1].removeprefix('Distance: ')).replace(' ', ''))
    result = 0
    vel = 0

    while (time > 0):
        if time * vel > distance:
            result += 1
        time -= 1
        vel += 1

    return result


if __name__ == '__main__':
    input_txt = 'day_6/input.txt'

    try:
        with open(input_txt, "r") as f:
            data = list()
            for line in f:
                line = line.removesuffix("\n")
                data.append(line)

            res = get_result(data)

        print(f'The result is: {res}')
    except FileNotFoundError as e:
        print(e.filename + ' - ' + e.strerror)
