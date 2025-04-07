from collections import defaultdict
n, k, bag_size = map(int, input().split())
shelves = defaultdict(list)

for _ in range(n):
    item_id, value = input().split()
    item_id = int(item_id)
    value = float(value)
    shelf_num = item_id % k
    shelves[shelf_num].append((item_id, value))

for shelf_num in shelves:
    shelves[shelf_num].sort(reverse=True, key=lambda x: x[0])
shelf_list = sorted(shelves.items())

expanded_shelves = []
for shelf_num, items in shelf_list:
    expanded_shelves.append((shelf_num, items))
for shelf_num, items in shelf_list:
    expanded_shelves.append((shelf_num + k, items))

value_list = []
for shelf_num, items in expanded_shelves:
    for item_id, value in items:
        value_list.append((shelf_num, value))


def max_value_with_constraints(value_list, bag_size):
    max_sum = 0
    length = len(value_list)

    for start in range(length):
        total_value = 0
        item_count = 0
        shelf_counts = defaultdict(int)
        previous_shelf = None
        valid_subarray = True
        overflow = True

        for end in range(start, min(start + bag_size,  length)):
            shelf_num, value = value_list[end]

            if previous_shelf is not None and (shelf_num != previous_shelf and shelf_num - previous_shelf > 1):
                valid_subarray = False
                break
            previous_shelf = shelf_num

            total_value += value
            item_count += 1
            shelf_counts[shelf_num] += 1

            if len(shelf_counts) == len(set(shelf_counts.values())):
                max_sum = max(max_sum, total_value)

            if end == start + n:
                overflow = False
                break

        if not valid_subarray:
            continue

        if not overflow:
            continue
    return max_sum

result = max_value_with_constraints(value_list, bag_size)
print(f"{result:.1f}")
