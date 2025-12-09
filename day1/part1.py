if __name__ == '__main__':
    with open("input.txt", encoding='utf-8') as file:
        lines = [line.rstrip() for line in file]
        cursor = 50
        password = 0
        for line in lines:
            direction = line[0]
            number = int(line[1:])
            if direction == "L":
                cursor = (cursor - number) % 100
            elif direction == "R":
                cursor = (cursor + number) % 100
            else:
                raise Exception("unknown direction %s", direction)
            if cursor == 0:
                password += 1
    print(password)
