from itertools import count, islice


def get_list(data: list, row: str, num: int, dict_list: dict, type: str, req: list):
    dest, source, rng = map(int, row.split(' '))  # ranges
    s, e = req.pop()
    res = []

    os = max(s, source)
    oe = min(e, source + rng)

    if os < oe:
        res.append((os-source+dest, oe-source+dest))
        if os > s:
            req.append((s, os))
        if e > oe:
            req.append((oe, e))

    # for num in req:
    #     if source <= num < source+rng:
    #         res.append(num-source+dest)
    #     else:
    #         res.append(num)

    return res


def get_required(req: list, result: list):
    ret = req.copy()
    for res in result:
        for i, value in enumerate(res):
            if value != req[i]:
                ret[i] = value
    return ret


def location(data: list):
    type = ''
    listing = {}
    result = []
    req = []  # seeds

    new_req = list(map(int, str(data[0]).removeprefix('seeds: ').split(' ')))

    i = 0
    while i < len(new_req):
        req.append((new_req[i], new_req[i] + new_req[i+1]))
        i += 2

    for num, row in enumerate(data):
        match(row):
            case '':
                type = row
            case "seed-to-soil map:":
                type = row
                req = get_required(req, result)
                result = []
            case "soil-to-fertilizer map:":
                type = row
                req = get_required(req, result)
                result = []
            case "fertilizer-to-water map:":
                type = row
                req = get_required(req, result)
                result = []
            case "water-to-light map:":
                type = row
                req = get_required(req, result)
                result = []
            case "light-to-temperature map:":
                type = row
                req = get_required(req, result)
                result = []
            case "temperature-to-humidity map:":
                type = row
                req = get_required(req, result)
                result = []
            case "humidity-to-location map:":
                type = row
                req = get_required(req, result)
                result = []

        if row != type:
            match(type):
                case "seed-to-soil map:":
                    result.append(get_list(
                        data, row, num, listing, type, req))
                case "soil-to-fertilizer map:":
                    result.append(get_list(
                        data, row, num, listing, type, req))
                case "fertilizer-to-water map:":
                    result.append(get_list(
                        data, row, num, listing, type, req))
                case "water-to-light map:":
                    result.append(get_list(
                        data, row, num, listing, type, req))
                case "light-to-temperature map:":
                    result.append(get_list(
                        data, row, num, listing, type, req))
                case "temperature-to-humidity map:":
                    result.append(get_list(
                        data, row, num, listing, type, req))
                case "humidity-to-location map:":
                    result.append(get_list(
                        data, row, num, listing, type, req))

    req = get_required(req, result)
    return min(req)


if __name__ == '__main__':
    input_txt = 'day_5/input.txt'

    try:
        with open(input_txt, "r") as f:
            data = list()
            for line in f:
                line = line.removesuffix("\n")
                data.append(line)

            loc = location(data)

        print(f'The location is: {loc}')
    except FileNotFoundError as e:
        print(e.filename + ' - ' + e.strerror)
