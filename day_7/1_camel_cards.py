import numpy as np


def get_result(data: list):
    hand_rank = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6,
                 '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
    pos = np.arange(len(data), 0, -1)

    type = {
        (1, 1): [],
        (2, 1): [],
        (2, 2): [],
        (3, 1): [],
        (3, 2): [],
        (4, 1): [],
        (5, 0): []
    }

    for hand, bid in data:
        hand_app = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0,
                    '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}

        sp = list(hand)

        for card in sp:
            hand_app[card] += 1

        val_1 = hand_app[max(hand_app, key=hand_app.get)]
        hand_app.pop(max(hand_app, key=hand_app.get))
        val_2 = hand_app[max(hand_app, key=hand_app.get)]

        ty = len(type[(val_1, val_2)])

        if ty == 0:
            type[(val_1, val_2)].append([hand, int(bid)])
        else:
            for ha in reversed(type[(val_1, val_2)]):
                l = list(ha[0])
                ins = type[(val_1, val_2)].index(ha)
                if hand_rank[l[0]] < hand_rank[sp[0]]:
                    pass
                elif hand_rank[l[0]] > hand_rank[sp[0]]:
                    ins += 1
                    break
                else:
                    if hand_rank[l[1]] < hand_rank[sp[1]]:
                        pass
                    elif hand_rank[l[1]] > hand_rank[sp[1]]:
                        ins += 1
                        break
                    else:
                        if hand_rank[l[2]] < hand_rank[sp[2]]:
                            pass
                        elif hand_rank[l[2]] > hand_rank[sp[2]]:
                            ins += 1
                            break
                        else:
                            if hand_rank[l[3]] < hand_rank[sp[3]]:
                                pass
                            elif hand_rank[l[3]] > hand_rank[sp[3]]:
                                ins += 1
                                break
                            else:
                                if hand_rank[l[4]] < hand_rank[sp[4]]:
                                    pass
                                else:
                                    ins += 1
                                    break

            if ins == -1:
                type[(val_1, val_2)].insert(0, [hand, int(bid)])
            elif ins != -1:
                type[(val_1, val_2)].insert(ins, [hand, int(bid)])

    hand_res = type[(5, 0)] + type[(4, 1)] + type[(3, 2)] + \
        type[(3, 1)] + type[(2, 2)] + type[(2, 1)] + type[(1, 1)]

    res = np.dot(pos, np.array(hand_res)[:, 1].astype(int))
    return res


if __name__ == '__main__':
    input_txt = 'day_7/1_input.txt'

    try:
        with open(input_txt, "r") as f:
            data = list()
            for line in f:
                line = line.removesuffix("\n")
                line = line.split(" ")
                data.append(line)

            res = get_result(data)

        print(f'The total winings are: {res}')
    except FileNotFoundError as e:
        print(e.filename + ' - ' + e.strerror)
