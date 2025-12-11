if __name__ == '__main__':
    with open("input.txt", encoding='utf-8') as file:
        lines = [line.rstrip() for line in file]
    intervals = []
    ids_to_check = []
    count = 0
    for line in lines:
        if line:
            if "-" in line:
                intervals.append([int(x) for x in line.split("-")])
            else:
                ids_to_check.append(int(line))
    intervals = sorted(intervals)
    for item in sorted(ids_to_check):
        if item < intervals[0][0] or item > intervals[-1][1]:
            continue
        for interval in intervals:
            if interval[0] <= item <= interval[1]:
                count += 1
                break
    print(count)
