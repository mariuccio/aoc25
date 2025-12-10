if __name__ == '__main__':
    with open("input.txt", encoding='utf-8') as file:
        lines = [line.rstrip() for line in file]
        result = 0
        for line in lines:
            max_value = 0
            for i in range(0, len(line) - 1):
                for j in range(i + 1, len(line)):
                    max_value = max(max_value, int(f"{line[i]}{line[j]}"))
            result += max_value
        print(result)