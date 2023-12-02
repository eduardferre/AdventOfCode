
def is_game_valid(game: str):
    sets = game.split('; ')

    for set in sets:
        valid = True
        blocks = set.split(', ')
        for block in blocks:
            total, color = block.split(' ')
            total = int(total)
            match color:
                case 'red':
                    if (total > 12):
                        valid = False
                        break
                case 'green':
                    if (total > 13):
                        valid = False
                        break
                case 'blue':
                    if (total > 14):
                        valid = False
                        break
        if not valid:
            return valid
    return valid


if __name__ == '__main__':
    input_txt = 'day_2/input.txt'

    try:
        with open(input_txt, "r") as f:
            sum = 0
            for line in f:
                id, game = line.split(': ')
                id = int(id.removeprefix('Game '))

                if (is_game_valid(game)):
                    sum += id

        print(f'The total sum of possible games is: {sum}')
    except FileNotFoundError as e:
        print(e.filename + ' - ' + e.strerror)
