if __name__ == '__main__':
    with open("input.txt", encoding='utf-8') as file:
        lines = [line.rstrip() for line in file]
        line = lines[0]
        id_ranges = line.split(",")
        sum_invalid_ids = 0
        for id_range in id_ranges:
            min_id, max_id = id_range.split("-")
            for item in range(int(min_id), int(max_id) + 1):
                item_str = str(item)
                if len(item_str) % 2 == 1:
                    continue
                if item_str[:len(item_str)//2] == item_str[len(item_str)//2:]:
                    sum_invalid_ids += item
        print(sum_invalid_ids)
