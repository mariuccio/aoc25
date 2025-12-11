if __name__ == '__main__':
    with open("input.txt", encoding='utf-8') as file:
        lines = [line.rstrip() for line in file]

    intervals = []
    for line in lines:
        if "-" in line:
            a, b = map(int, line.split("-"))
            intervals.append([a, b])

    intervals.sort()

    merged_start, merged_end = intervals[0]
    total = 0

    for start, end in intervals[1:]:
        if start <= merged_end + 1:
            merged_end = max(merged_end, end)
        else:
            total += merged_end - merged_start + 1
            merged_start, merged_end = start, end

    total += merged_end - merged_start + 1

    print(total)
