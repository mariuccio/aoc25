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
                for sub_item_len in range(1, len(item_str) // 2 + 1):
                    if len(item_str) % sub_item_len != 0:
                        continue
                    item_str_split = [item_str[i:i + sub_item_len] for i in range(0, len(item_str), sub_item_len)]
                    if item_str_split.count(item_str_split[0]) == len(item_str_split):
                        sum_invalid_ids += item
                        break
        print(sum_invalid_ids)
