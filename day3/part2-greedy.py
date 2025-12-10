if __name__ == "__main__":
    with open("input.txt", encoding='utf-8') as f:
        lines = [line.rstrip() for line in f]

    result = 0
    k = 12

    for line in lines:
        remaining = k
        start = 0
        chosen = []

        while remaining > 0:
            end = len(line) - remaining
            max_digit = max(line[start:end+1])
            pos = line.index(max_digit, start, end+1)

            chosen.append(max_digit)
            start = pos + 1
            remaining -= 1

        max_value = int("".join(chosen))
        result += max_value

    print(result)
