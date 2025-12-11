if __name__ == '__main__':
    with open("input.txt", encoding='utf-8') as file:
        lines = [list(line.rstrip()) for line in file]
    rolls = 0
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
                    rolls += 1
    print(rolls)
