if __name__ == '__main__':
    for filename in [
        "test_inputL50L50.txt",
        "test_inputL50R50.txt",
        "test_inputR50L50.txt",
        "test_inputR50R50.txt",
        "test_inputL50L100.txt",
        "test_inputL50R100.txt",
        "test_inputR50L100.txt",
        "test_inputR50R100.txt",
        "test_inputL150L50.txt",
        "test_inputL150R50.txt",
        "test_inputR150L50.txt",
        "test_inputR150R50.txt",
        "input.txt"
    ]:
        with open(filename, encoding='utf-8') as file:
            lines = [line.rstrip() for line in file]
            cursor = 50
            password = 0
            for line in lines:
                direction = line[0]
                number = int(line[1:])
                nb_zero_visits = number // 100
                if direction == "L":
                    if cursor != 0 and cursor - (number % 100) <= 0:
                        nb_zero_visits += 1
                    cursor = (cursor - number) % 100
                elif direction == "R":
                    if cursor != 0 and cursor + (number % 100) >= 100:
                        nb_zero_visits += 1
                    cursor = (cursor + number) % 100
                else:
                    raise Exception("unknown direction %s", direction)
                password += nb_zero_visits
        print(f"{filename}: {password}")
