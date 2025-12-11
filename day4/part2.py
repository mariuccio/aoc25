if __name__ == '__main__':
    with open("input.txt", encoding='utf-8') as file:
        lines = [list(line.rstrip()) for line in file]
    rolls = 0
    while True:
        positions_to_update = []
        for i in range(0, len(lines)):
            line = lines[i]
            for j in range(0, len(line)):
                if lines[i][j] == "@":
                    rolls_around = 0
                    for k in range(max(0, i - 1), min(len(lines), i + 2)):
                        for l in range(max(0, j - 1), min(len(line), j + 2)):
                            if i == k and j == l:
                                continue
                            if lines[k][l] == "@":
                                rolls_around += 1
                    if rolls_around < 4:
                        positions_to_update.append((i, j))
                        rolls += 1
        if len(positions_to_update) == 0:
            break
        for pos in positions_to_update:
            lines[pos[0]][pos[1]] = "."
    print(rolls)
