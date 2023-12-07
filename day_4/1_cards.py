def sum_card(card: str):
    win_num, nums = card.split(' | ')
    win_array = [item for item in win_num.split(
        ' ') if (item != " " and item != "")]
    num_array = [item for item in nums.split(
        ' ') if (item != " " and item != "")]
    power = 0

    for win_num in win_array:
        if num_array.__contains__(win_num):
            if power == 0:
                power = 1
            else:
                power *= 2

    return power


if __name__ == '__main__':
    input_txt = 'day_4/input.txt'

    try:
        with open(input_txt, "r") as f:
            sum = 0
            for line in f:
                line = line.removesuffix("\n")
                id, card = line.split(': ')

                sum += sum_card(card)

        print(f'The total sum is: {sum}')
    except FileNotFoundError as e:
        print(e.filename + ' - ' + e.strerror)
