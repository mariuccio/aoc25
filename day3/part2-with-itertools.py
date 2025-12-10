from itertools import combinations

if __name__ == '__main__':
    with open("test.txt", encoding='utf-8') as file:
        lines = [line.rstrip() for line in file]
        result = 0
        for line in lines:
            max_value = 0
            for combo in combinations(range(len(line)), 12):
                value = int("".join(line[i] for i in combo))
                max_value = max(max_value, value)
            result += max_value
        print(result)
