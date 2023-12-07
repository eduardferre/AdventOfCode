def total_cards(data: list):
    data_copy = data.copy()
    m = {}
    for i in range(len(data)):
        m[i] = 1

    for i, card in enumerate(data):
        win_num, nums = card.split(' | ')
        win_array = [item for item in win_num.split(
            ' ') if (item != " " and item != "")]
        num_array = [item for item in nums.split(
            ' ') if (item != " " and item != "")]
        total = 0

        for win_num in win_array:
            if num_array.__contains__(win_num):
                total += 1

        for n in range(i + 1, i + total + 1):
            m[n] = m.get(n, 1) + m[i]

    return sum(m.values())


if __name__ == '__main__':
    input_txt = 'day_4/input.txt'

    try:
        data = []
        with open(input_txt, "r") as f:
            for line in f:
                line = line.removesuffix("\n")
                id, card = line.split(': ')
                data.append(card)

        total = total_cards(data)

        print(f'The total scratchcards are: {total}')
    except FileNotFoundError as e:
        print(e.filename + ' - ' + e.strerror)
