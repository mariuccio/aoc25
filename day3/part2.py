if __name__ == '__main__':
    with open("input.txt", encoding='utf-8') as file:
        lines = [line.rstrip() for line in file]
        result = 0
        for line in lines:
            max_value = 0
            for i1 in range(0, len(line) - 11):
                for i2 in range(i1 + 1, len(line) - 10):
                    for i3 in range(i2 + 1, len(line) - 9):
                        for i4 in range(i3 + 1, len(line) - 8):
                            for i5 in range(i4 + 1, len(line) - 7):
                                for i6 in range(i5 + 1, len(line) - 6):
                                    for i7 in range(i6 + 1, len(line) - 5):
                                        for i8 in range(i7 + 1, len(line) - 4):
                                            for i9 in range(i8 + 1, len(line) - 3):
                                                for i10 in range(i9 + 1, len(line) - 2):
                                                    for i11 in range(i10 + 1, len(line) - 1):
                                                        for i12 in range(i11 + 1, len(line)):
                                                            print(line, len(line), max_value, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, int(f"{line[i1]}{line[i2]}{line[i3]}{line[i4]}{line[i5]}{line[i6]}{line[i7]}{line[i8]}{line[i9]}{line[i10]}{line[i11]}{line[i12]}"))
                                                            max_value = max(max_value, int(f"{line[i1]}{line[i2]}{line[i3]}{line[i4]}{line[i5]}{line[i6]}{line[i7]}{line[i8]}{line[i9]}{line[i10]}{line[i11]}{line[i12]}"))
            result += max_value
        print(result)

