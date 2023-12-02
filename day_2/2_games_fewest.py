
def game_power(game: str):
    sets = game.split('; ')
    min_red = 0
    min_green = 0
    min_blue = 0

    for set in sets:
        valid = True
        blocks = set.split(', ')
        for block in blocks:
            total, color = block.split(' ')
            total = int(total)
            match color:
                case 'red':
                    if (total > min_red):
                        min_red = total
                case 'green':
                    if (total > min_green):
                        min_green = total
                case 'blue':
                    if (total > min_blue):
                        min_blue = total
    return (min_red*min_green*min_blue)


if __name__ == '__main__':
    input_txt = 'day_2/input.txt'

    try:
        with open(input_txt, "r") as f:
            sum = 0
            for line in f:
                game = line.split(': ')[1].replace('\n', '')
                power = game_power(game)
                sum = sum + power

        print(f'The total sum of possible games is: {sum}')
    except FileNotFoundError as e:
        print(e.filename + ' - ' + e.strerror)
