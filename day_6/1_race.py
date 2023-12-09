def get_result(data):
    time = list(map(int, str(data[0]).removeprefix('Time: ').split()))
    distance = list(map(int, str(data[1]).removeprefix('Distance: ').split()))
    result = 1

    for i, t in enumerate(time):
        vel = 0
        res = 0
        while (t > 0):
            if t * vel > distance[i]:
                res += 1
            t -= 1
            vel += 1
        result = result * res
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
